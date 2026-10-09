# draw.io file reference

Use this reference for file structure and editability.
It does not define diagram symbols or relationship meanings.

The [draw.io XML guide](https://www.drawio.com/docs/manual/advanced/diagram-source-edit/) describes the editable page source.
For full structure details, use the [publisher schema](https://github.com/jgraph/drawio-mcp/blob/main/shared/mxfile.xsd).
For style keys, use the [publisher style reference](https://github.com/jgraph/drawio-mcp/blob/main/shared/style-reference.md).

## File structure

Use uncompressed XML for new files.
Give each page a `diagram` element inside `mxfile`.
Put the page model in `mxGraphModel`.
Put the cells in its `root` element.

Start each page with structural cells `0` and `1`.
Give cell `1` the parent `0`.
Use unique IDs within each page.
Give visible elements a layer or group parent.

The [file example](../../assets/diagram-design/file-structure.drawio) contains two generic labels and one plain connection.
It demonstrates file structure only.
Replace its shapes and relationship styles with those from the supplied notation.

## Elements and connections

Use `vertex="1"` for a shape and `edge="1"` for a connector.
Do not give one cell both roles.
Use `mxGeometry` for position and dimensions.
For a child shape, coordinates are relative to its parent.

For an attached connector, use `source` and `target` IDs.
Use `relative="1"` in its geometry.
Store path waypoints in `Array as="points"`.
Use explicit endpoint points for a deliberately unattached line.

Keep labels in cell values or supported label objects.
Escape XML attribute content with an XML library.
Keep labels, shapes, and connectors separately editable.

## Style

Use semicolon-separated style keys.
Set the font, text size, fills, and line widths consistently.
Use `edgeStyle=orthogonalEdgeStyle` where an orthogonal path suits the model.
Keep the selected notation's markers and line patterns.
Do not treat unknown style keys as a reliable feature.

For embedded SVG images, follow the publisher image style format.
Do not reference temporary local files.
Keep required assets portable.

## Checks

Parse the XML before editor use.
Confirm unique IDs and valid parent references.
Confirm that all attached edge endpoints exist.
Confirm positive shape dimensions and finite coordinates.
Confirm the original model relationships after layout changes.

Open the file in draw.io or a compatible editor.
Make a preview from that editor when available.
Examine text, marker styles, routing, and page bounds.
XML parsing alone does not confirm the final appearance.
