#!/usr/bin/env python3
"""Check a typed JSON model or render it with bundled ArchiMate 3.2 SVG templates.

Only the standard library is required. This is not a full conformance validator.
"""
import argparse
import copy
import json
import math
import sys
import textwrap
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)

def tag(name): return '{'+NS+'}'+name
def add(parent, name, attrs=None, text=None):
    child=ET.SubElement(parent,tag(name),{k:str(v) for k,v in (attrs or {}).items()})
    child.text=text
    return child

def finite(value):
    return isinstance(value,(int,float)) and not isinstance(value,bool) and math.isfinite(value)

def point(value):
    return isinstance(value,list) and len(value)==2 and all(finite(x) and 0<=x<=100000 for x in value)

def validate(model, catalog):
    errors, warnings = [], []
    def error(message): errors.append(message)
    if not isinstance(model,dict):
        return {'status':'invalid','errors':['Model must be a JSON object.'],'warnings':[],
                'full_archimate_conformance':'unverified'}
    nodes, edges=model.get('nodes'),model.get('edges')
    if not isinstance(nodes,list): error('nodes must be a list.'); nodes=[]
    if not isinstance(edges,list): error('edges must be a list.'); edges=[]
    if not nodes: error('At least one node is required by this helper.')
    known={e['type']:e for e in catalog['elements']}
    connectors={c['type'] for c in catalog['connectors']}
    reltypes={r['type'] for r in catalog['relationships']}
    def entry(node):
        value=node.get('type')
        return known.get(value) if isinstance(value,str) else None
    def junction(node):
        value=node.get('type')
        return isinstance(value,str) and value in connectors
    ids=set(); indexed={}; valid_edges=[]
    for i,node in enumerate(nodes):
        prefix=f'Node {i+1}'
        if not isinstance(node,dict): error(prefix+' must be an object.');continue
        identifier=node.get('id')
        if not isinstance(identifier,str) or not identifier.strip():
            error(prefix+' needs a nonempty string id.');continue
        prefix=f'Node {identifier}'
        if identifier in ids: error(prefix+' has a duplicate id.');continue
        ids.add(identifier);indexed[identifier]=node
        if not isinstance(node.get('type'),str) or node['type'] not in known.keys()|connectors:
            error(prefix+' has an unknown exact type name.')
        if not junction(node) and (not isinstance(node.get('name'),str) or not node['name'].strip()):
            error(prefix+' needs a nonempty name.')
        for key in ('x','y'):
            if key in node and (not finite(node[key]) or not 0<=node[key]<=100000):
                error(prefix+f' {key} must be a finite, nonnegative coordinate.')
        if 'width' in node and (not finite(node['width']) or not 16<=node['width']<=2000):
            error(prefix+' width must be between 16 and 2000.')
    for i,edge in enumerate(edges):
        prefix=f'Edge {i+1}'
        if not isinstance(edge,dict): error(prefix+' must be an object.');continue
        identifier=edge.get('id')
        if not isinstance(identifier,str) or not identifier.strip(): error(prefix+' needs a string id.');continue
        prefix=f'Edge {identifier}'
        if identifier in ids: error(prefix+' has a duplicate id.');continue
        ids.add(identifier)
        if not isinstance(edge.get('type'),str) or edge['type'] not in reltypes:
            error(prefix+' has an unknown exact relationship type.');continue
        if not all(isinstance(edge.get(k),str) and edge[k] in indexed for k in ('source','target')):
            error(prefix+' source and target must reference node IDs.');continue
        if 'label' in edge and not isinstance(edge['label'],str): error(prefix+' label must be a string.')
        if 'points' in edge and (not isinstance(edge['points'],list) or not all(point(p) for p in edge['points'])):
            error(prefix+' points must be a list of finite [x, y] coordinates.')
        if 'label_position' in edge and not point(edge['label_position']):
            error(prefix+' label_position must contain finite [x, y] coordinates.')
        if 'directed' in edge and (edge['type']!='Association' or not isinstance(edge['directed'],bool)):
            error(prefix+' directed is a boolean used only for Association.')
        if edge['type']=='Access':
            if edge.get('access_mode') not in ('access','read','write','read-write'):
                error(prefix+' needs access_mode: access, read, write, or read-write.')
            source=entry(indexed[edge['source']])
            target=entry(indexed[edge['target']])
            if source and source['aspect'] not in ('active','behavior'):
                error(prefix+' Access source must represent behavior or active structure in this helper.')
            if target and target['aspect']!='passive':
                error(prefix+' Access target must represent passive structure in this helper.')
        elif 'access_mode' in edge: error(prefix+' access_mode is used only for Access.')
        if edge['type']=='Influence':
            target=entry(indexed[edge['target']])
            if target and target['group']!='Motivation': error(prefix+' Influence target must be a motivation element.')
        valid_edges.append(edge)
    for identifier,node in indexed.items():
        if junction(node):
            attached=[e for e in valid_edges if identifier in (e['source'],e['target'])]
            if len(attached)<2: error(f'Junction {identifier} must connect at least two relationships.')
            if len({e['type'] for e in attached})>1: error(f'Junction {identifier} mixes relationship types.')
            if not any(e['source']==identifier for e in attached) or not any(e['target']==identifier for e in attached):
                warnings.append(f'Junction {identifier} has no incoming or no outgoing branch; review its direction.')
    warnings.append('Exact endpoint-pair admissibility, relationship derivation, and full junction rules are unverified.')
    return {'status':'invalid' if errors else 'basic-checks-passed','errors':errors,'warnings':warnings,
            'checks':['exact type names','unique IDs','node references','Access properties and broad categories',
                      'Influence target category','junction relationship-type consistency'],
            'full_archimate_conformance':'unverified'}

def box_for(node, catalog):
    known={e['type']:e for e in catalog['elements']}
    if node['type'] in ('AndJunction','OrJunction'):
        path=ROOT/'assets/relationships'/('and-junction.svg' if node['type']=='AndJunction' else 'or-junction.svg')
        width=node.get('width',18)
    else:
        path=ROOT/known[node['type']]['template']; width=node.get('width',180)
    asset=ET.parse(path).getroot()
    _,_,w,h=map(float,asset.attrib['viewBox'].split())
    height=width*h/w
    return {'x':node['x'],'y':node['y'],'w':width,'h':height,'asset':asset,
            'junction':node['type'] in ('AndJunction','OrJunction')}

def center(box): return [box['x']+box['w']/2,box['y']+box['h']/2]

def anchor(box,toward):
    cx,cy=center(box);dx,dy=toward[0]-cx,toward[1]-cy
    if dx==dy==0: raise ValueError('Overlapping endpoint centers need explicit routing points.')
    if box['junction']:
        scale=min(box['w'],box['h'])/2/math.hypot(dx,dy)
    else:
        scale=1/max(abs(dx)/(box['w']/2),abs(dy)/(box['h']/2))
    return [cx+dx*scale,cy+dy*scale]

def markers(svg):
    defs=add(svg,'defs')
    forms={
        'open':('M0 -4 L9 0 L0 4','none',9),
        'filled':('M0 -4 L9 0 L0 4 Z','#222',9),
        'triangle':('M0 -6 L11 0 L0 6 Z','white',11),
        'diamond':('M0 0 L8 -4 L16 0 L8 4 Z','#222',0),
        'hollow-diamond':('M0 0 L8 -4 L16 0 L8 4 Z','white',0)}
    for name,(d,fill,ref) in forms.items():
        marker=add(defs,'marker',{'id':'m-'+name,'viewBox':'-1 -7 19 14','refX':ref,'refY':0,
                                 'markerWidth':19,'markerHeight':14,'markerUnits':'userSpaceOnUse',
                                 'orient':'auto-start-reverse' if name in ('open','filled','triangle') else 'auto'})
        add(marker,'path',{'d':d,'fill':fill,'stroke':'#222','stroke-width':1.1})
    marker=add(defs,'marker',{'id':'m-dot','viewBox':'-5 -5 10 10','refX':0,'refY':0,
                             'markerWidth':10,'markerHeight':10,'markerUnits':'userSpaceOnUse','orient':'auto'})
    add(marker,'circle',{'cx':0,'cy':0,'r':3,'fill':'#222'})

def relationship_style(edge):
    kind=edge['type'];result={'stroke':'#222','stroke-width':1.5,'fill':'none'}
    start,end=None,None
    if kind=='Composition': start='diamond'
    elif kind=='Aggregation':start='hollow-diamond'
    elif kind=='Assignment':start,end='dot','filled'
    elif kind in ('Realization','Specialization'):end='triangle'
    elif kind in ('Serving','Influence'):end='open'
    elif kind in ('Triggering','Flow'):end='filled'
    elif kind=='Association' and edge.get('directed'):end='open'
    elif kind=='Access':
        mode=edge['access_mode']
        if mode in ('read','read-write'):start='open'
        if mode in ('write','read-write'):end='open'
    if kind in ('Realization','Access'): result['stroke-dasharray']='1.5 2'
    if kind in ('Influence','Flow'):result['stroke-dasharray']='7 3'
    if start:result['marker-start']='url(#m-'+start+')'
    if end:result['marker-end']='url(#m-'+end+')'
    return result

def polyline_midpoint(points):
    lengths=[math.dist(a,b) for a,b in zip(points,points[1:])]
    remaining=sum(lengths)/2
    for a,b,length in zip(points,points[1:],lengths):
        if length and remaining<=length:
            fraction=remaining/length;return [a[0]+(b[0]-a[0])*fraction,a[1]+(b[1]-a[1])*fraction]
        remaining-=length
    return points[0]

def render(model,catalog,destination):
    for node in model['nodes']:
        if 'x' not in node or 'y' not in node:raise ValueError(f"Node {node['id']} needs x and y for rendering.")
    title=model.get('title','ArchiMate 3.2 view')
    if not isinstance(title,str):raise ValueError('title must be a string.')
    boxes={n['id']:box_for(n,catalog) for n in model['nodes']}
    node_labels={}
    for node in model['nodes']:
        box=boxes[node['id']]
        if box['junction']:continue
        # Reserve room for the corner notation. Never silently truncate a label.
        fontsize=13
        lines=textwrap.wrap(node['name'],width=max(8,int((box['w']-34)/(fontsize*0.57))),
                            break_long_words=False,break_on_hyphens=False)
        available=box['h']-20
        if len(lines)*16>available or any(len(line)*fontsize*0.57>box['w']-25 for line in lines):
            raise ValueError(f"Node {node['id']} label does not fit. Shorten the label or increase width.")
        node_labels[node['id']]=lines
    routes={}
    for edge in model['edges']:
        s,t=boxes[edge['source']],boxes[edge['target']]
        points=edge.get('points',[])
        if edge['source']==edge['target'] and len(points)<2:
            raise ValueError(f"Self-edge {edge['id']} needs at least two external routing points.")
        routes[edge['id']]=[anchor(s,points[0] if points else center(t)),*points,
                            anchor(t,points[-1] if points else center(s))]
    extent_x=[b['x']+b['w'] for b in boxes.values()]
    extent_y=[b['y']+b['h']+28 for b in boxes.values()]
    for edge in model['edges']:
        for p in routes[edge['id']]:extent_x.append(p[0]+100);extent_y.append(p[1]+30)
        if 'label_position' in edge:
            extent_x.append(edge['label_position'][0]+150);extent_y.append(edge['label_position'][1]+30)
    width=max(extent_x)+30;height=max(extent_y)+30
    svg=ET.Element(tag('svg'),{'viewBox':f'0 0 {width:.2f} {height:.2f}',
                               'width':f'{width:.2f}','height':f'{height:.2f}','role':'img'})
    add(svg,'title',text=title)
    add(svg,'desc',text='ArchiMate 3.2 notation. Basic checks only; full language conformance remains unverified.')
    add(svg,'metadata',text=catalog['source']['copyright']+' '+catalog['source']['trademark']+
        ' Element templates extracted from N221. Diagram content supplied by the model author.')
    add(svg,'rect',{'width':'100%','height':'100%','fill':'white'})
    add(svg,'text',{'x':24,'y':27,'font-family':'Arial, sans-serif','font-size':19,'font-weight':'bold'},title)
    markers(svg)
    for edge in model['edges']:
        route=routes[edge['id']]
        group=add(svg,'g',{'data-relationship-id':edge['id']})
        add(group,'title',text=f"{edge['source']} — {edge['type']} → {edge['target']}")
        style=relationship_style(edge)
        style['d']='M'+' L'.join(f'{p[0]:.2f} {p[1]:.2f}' for p in route)
        add(group,'path',style)
        label=edge['type']+(': '+edge['label'] if edge.get('label') else '')
        pos=edge.get('label_position',polyline_midpoint(route))
        add(group,'text',{'x':pos[0],'y':pos[1]-7,'font-family':'Arial, sans-serif','font-size':11,
                         'text-anchor':'middle','fill':'#222','stroke':'white','stroke-width':4,
                         'paint-order':'stroke'},label)
    for node in model['nodes']:
        box=boxes[node['id']];cx,cy=center(box)
        group=add(svg,'g',{'data-element-id':node['id']})
        add(group,'title',text=node.get('name',node['type'])+' — '+node['type'])
        asset=copy.deepcopy(box['asset'])
        asset.attrib.update({'x':str(box['x']),'y':str(box['y']),'width':str(box['w']),'height':str(box['h']),
                             'preserveAspectRatio':'xMidYMid meet'})
        group.append(asset)
        if not box['junction']:
            lines=node_labels[node['id']]
            # Center the label below the corner icon.
            first=cy-(len(lines)-1)*8+5
            for i,line in enumerate(lines):
                add(group,'text',{'x':cx,'y':first+i*16,'font-family':'Arial, sans-serif',
                                 'font-size':13,'text-anchor':'middle','fill':'#111'},line)
            add(group,'text',{'x':cx,'y':box['y']+box['h']+14,'font-family':'Arial, sans-serif',
                             'font-size':10,'text-anchor':'middle','fill':'#555','stroke':'white',
                             'stroke-width':4,'paint-order':'stroke'},node['type'])
    add(svg,'text',{'x':24,'y':height-10,'font-family':'Arial, sans-serif','font-size':10,'fill':'#666'},
        'ArchiMate 3.2 • Exact endpoint-pair conformance unverified • Source symbols: The Open Group N221')
    payload=ET.tostring(svg,encoding='unicode')+'\n'
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(payload,encoding='utf-8')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    check=sub.add_parser('validate');check.add_argument('model',type=Path)
    draw=sub.add_parser('render');draw.add_argument('model',type=Path);draw.add_argument('output',type=Path)
    args=parser.parse_args()
    try:
        model=json.loads(args.model.read_text(encoding='utf-8-sig'))
        catalog=json.loads((ROOT/'assets/catalog.json').read_text(encoding='utf-8'))
        report=validate(model,catalog)
        if args.command=='render' and not report['errors']:
            render(model,catalog,args.output);report['output']=str(args.output.resolve())
        print(json.dumps(report,indent=2,ensure_ascii=False))
        return 1 if report['errors'] else 0
    except (ValueError,OSError,KeyError,ET.ParseError) as exc:
        print(json.dumps({'status':'invalid','errors':[str(exc)],'full_archimate_conformance':'unverified'},indent=2))
        return 1

if __name__=='__main__':sys.exit(main())
