#!/usr/bin/env python3
"""Rebuild label-free SVG vectors from the supplied N221 PDF. Requires PyMuPDF."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from xml.sax.saxutils import escape

NOTICE = 'Copyright © 2022 The Open Group. All Rights Reserved. ArchiMate® is a registered trademark of The Open Group.'

def number(value):
    return f'{value:.5f}'.rstrip('0').rstrip('.') or '0'

def color(value):
    if value is None:
        return 'none'
    return '#' + ''.join(f'{round(255*max(0,min(1,v))):02x}' for v in value)

def path_data(drawing):
    out, current = [], None
    def point(p):
        return f'{number(p.x)} {number(p.y)}'
    def move(p):
        nonlocal current
        if current is None or abs(current.x-p.x)+abs(current.y-p.y)>0.001:
            out.append('M'+point(p))
        current=p
    for item in drawing['items']:
        kind=item[0]
        if kind=='l':
            move(item[1]); out.append('L'+point(item[2])); current=item[2]
        elif kind=='c':
            move(item[1]); out.append('C'+' '.join(point(p) for p in item[2:])); current=item[4]
        elif kind=='re':
            r=item[1]
            points=[r.top_left,r.top_right,r.bottom_right,r.bottom_left]
            if item[2]<0: points.reverse()
            out.append('M'+point(points[0])+' '+' '.join('L'+point(p) for p in points[1:])+' Z')
            current=None
        elif kind=='qu':
            q=item[1]
            out.append('M'+point(q.ul)+' L'+point(q.ur)+' L'+point(q.lr)+' L'+point(q.ll)+' Z')
            current=None
        else:
            raise ValueError(f'Unsupported PDF path item: {kind}')
    if drawing.get('closePath') and current is not None: out.append('Z')
    return ' '.join(out)

def svg_for(drawings, title, source_page, extra=''):
    if not drawings: raise ValueError(f'Empty crop for {title}')
    # PDF path bounds exclude stroke thickness, including round-cap circles.
    x0=min(d['rect'].x0-(d.get('width') or 0)/2 for d in drawings)-2
    y0=min(d['rect'].y0-(d.get('width') or 0)/2 for d in drawings)-2
    x1=max(d['rect'].x1+(d.get('width') or 0)/2 for d in drawings)+2
    y1=max(d['rect'].y1+(d.get('width') or 0)/2 for d in drawings)+2
    w,h=x1-x0,y1-y0
    paths=[]
    for d in drawings:
        attrs={'d':path_data(d),'fill':color(d.get('fill')),
               'stroke':color(d.get('color')),'stroke-width':number(d.get('width') or 0),
               'fill-rule':'evenodd' if d.get('even_odd') else 'nonzero',
               'stroke-linecap':str(max(d.get('lineCap') or (0,0,0))),
               'stroke-linejoin':str(int(d.get('lineJoin') or 0))}
        attrs['stroke-linecap']={'0':'butt','1':'round','2':'square'}[attrs['stroke-linecap']]
        attrs['stroke-linejoin']={'0':'miter','1':'round','2':'bevel'}[attrs['stroke-linejoin']]
        for key in ('fill','stroke'):
            opacity=d.get(key+'_opacity')
            if opacity is not None and opacity!=1: attrs[key+'-opacity']=number(opacity)
        dash=d.get('dashes') or '[] 0'
        match=re.fullmatch(r'\[\s*(.*?)\s*\]\s*(\S+)',dash)
        if match and match[1]:
            attrs['stroke-dasharray']=match[1]
            attrs['stroke-dashoffset']=match[2]
        paths.append('<path '+' '.join(f'{k}="{escape(v)}"' for k,v in attrs.items())+'/>')
    result=(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {number(w)} {number(h)}" '
            f'width="{number(w)}" height="{number(h)}">\n'
            f'<title>{escape(title)}</title>\n<metadata>{NOTICE} Source: N221, PDF page {source_page}. '
            'Label-free vector extraction; no raster tracing.</metadata>\n'
            f'<g transform="translate({number(-x0)} {number(-y0)})">\n'+
            '\n'.join(paths)+extra+'\n</g>\n</svg>\n')
    return result,[round(v,5) for v in (x0,y0,x1,y1)]

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf',type=Path)
    parser.add_argument('--skill-dir',type=Path,default=Path(__file__).resolve().parents[1])
    args=parser.parse_args()
    import pymupdf
    root=args.skill_dir
    catalog=json.loads((root/'assets/catalog.json').read_text(encoding='utf-8'))
    digest=hashlib.sha256(args.pdf.read_bytes()).hexdigest()
    if digest!=catalog['source']['sha256']:
        raise SystemExit('Source hash differs. Inspect the new PDF and update the catalog before extraction.')
    document=pymupdf.open(args.pdf)
    if len(document)!=14: raise SystemExit('Expected the 14-page N221 personal reference-card PDF.')
    manifest={'source':catalog['source'],'coordinate_system':'PDF points, origin at top left','assets':[]}
    def write(rel,ds,title,page,selection,extra='',correction=None):
        svg,bounds=svg_for(ds,title,page,extra)
        if correction:
            svg=svg.replace('Label-free vector extraction; no raster tracing.',
                            'Label-free vector extraction; no raster tracing. '+escape(correction))
        dest=root/rel; dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_text(svg,encoding='utf-8',newline='\n')
        manifest['assets'].append(dict(path=rel,type=title,pdf_page=page,
                                      selection_box=selection,vector_bounds=bounds,
                                      sha256=hashlib.sha256(svg.encode()).hexdigest()))
        if correction:manifest['assets'][-1]['correction']=correction
    for page_no in range(3,14):
        page=document[page_no-1]; drawings=page.get_drawings()
        entries=[e for e in catalog['elements'] if e['pdf_page']==page_no]
        boundaries=sorted(set(round(d['rect'].y0,3) for d in drawings
                              if d['rect'].width>250 and d['rect'].height<0.01 and 60<d['rect'].y0<390))
        boundaries=boundaries[1:]
        if len(boundaries)!=len(entries)+1:
            raise ValueError(f'Unexpected table rows on page {page_no}: {boundaries}')
        for index,entry in enumerate(entries):
            top,bottom=boundaries[index:index+2]
            for field,left,right in [('template',413,510),('symbol',513,578)]:
                ds=[d for d in drawings if d['rect'].x0>=left and d['rect'].x1<=right
                    and d['rect'].y0>top+1 and top+1<(d['rect'].y0+d['rect'].y1)/2<bottom-1]
                write(entry[field],ds,entry['type'],page_no,[left,top+1,right,bottom-1])
    page=document[1]; ds=page.get_drawings()
    # Tight source regions omit table borders and the illustrative dummy endpoints.
    crops={
        'composition':(486,76,536,88), 'aggregation':(486,94,536,105),
        'assignment':(487,115,536,127), 'realization':(487,138,536,153),
        'serving':(487,178,536,189), 'access':(489,201,534,207),
        'access-write':(489,207,534,213), 'access-read-write':(489,213,534,221),
        'influence':(486,234,535,241), 'association':(489,256,534,261),
        'association-directed':(489,261,534,268), 'triggering':(487,294,535,304),
        'flow':(486,312,534,323), 'specialization':(489,341,535,355),
        'and-junction':(477,371,489,383), 'or-junction':(535,371,547,383)}
    for slug,bounds in crops.items():
        x0,y0,x1,y1=bounds
        chosen=[d for d in ds if d['rect'].x0>=x0 and d['rect'].x1<=x1
                and d['rect'].y0>=y0 and d['rect'].y1<=y1]
        title=slug.replace('-',' ').title()
        correction=None
        if slug=='association-directed':
            # N221 renders only one side: its lower arrow stroke has zero opacity.
            # Restore that existing path to form the documented open-arrow notation.
            for drawing in chosen:
                if drawing.get('stroke_opacity')==0:drawing['stroke_opacity']=1
            correction='Restored the source lower arrow stroke from zero opacity to form a complete open arrow.'
        write(f'assets/relationships/{slug}.svg',chosen,title,2,list(bounds),correction=correction)
    # The reference card omits the read-only arrow variant. Mirror its write symbol.
    from xml.etree import ElementTree as ET
    write_root=ET.fromstring((root/'assets/relationships/access-write.svg').read_text(encoding='utf-8'))
    width=write_root.attrib['viewBox'].split()[2]
    inner=next(e for e in write_root if e.tag.endswith('}g'))
    mirror=ET.Element('{http://www.w3.org/2000/svg}g',{'transform':f'translate({width} 0) scale(-1 1)'})
    write_root.remove(inner); mirror.append(inner); write_root.append(mirror)
    next(e for e in write_root if e.tag.endswith('}title')).text='Access Read'
    next(e for e in write_root if e.tag.endswith('}metadata')).text+= ' Derived read variant: horizontal mirror of Access Write.'
    ET.register_namespace('','http://www.w3.org/2000/svg')
    dest=root/'assets/relationships/access-read.svg'
    payload=ET.tostring(write_root,encoding='unicode')+'\n';dest.write_text(payload,encoding='utf-8',newline='\n')
    manifest['assets'].append(dict(path='assets/relationships/access-read.svg',type='Access Read',
                                  pdf_page=2,derived_from='assets/relationships/access-write.svg',
                                  transformation='horizontal mirror',sha256=hashlib.sha256(payload.encode()).hexdigest()))
    (root/'assets/manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(f'Extracted {len(manifest["assets"])} vector assets.')

if __name__=='__main__': main()
