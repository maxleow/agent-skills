# Diagram assets and helper

## Design and editable delivery

Use the bundled [diagram-design guidance](diagram-design.md) for layout, style, and final visual checks.
For draw.io output, use [the file reference](diagram-design/drawio-format.md).
For SVG or presentations, use [the output reference](diagram-design/output-formats.md).
The [neutral design values](diagram-design/design-values.json) are starting values, not notation rules.
The [draw.io example](../assets/diagram-design/file-structure.drawio) illustrates file structure only.
Replace its generic shapes and plain connection with the required ArchiMate notation.
The local SVG helper uses a compact preset. Check label size and spacing for the intended display.

## Vector assets

`assets/elements/` contains 60 blank element templates. Each template preserves the main notation and its corner symbol.
`assets/symbols/` contains the 60 alternative symbols shown beside those templates.
Some alternatives are full shapes rather than small corner icons. Use them in accordance with the source notation.

`assets/relationships/` contains 17 symbols, including access variants, association variants, and two junctions.
Influence has an optional sign label. Its extracted SVG contains the line and arrow; add the sign as text when needed.
The read-only Access symbol is a documented mirror of the write symbol.
The directed Association symbol restores a transparent source stroke to complete its open arrow.

All assets are self-contained vectors. They have no raster images or external font dependencies.
The vectors omit the source text labels. Preserve their aspect ratios and add labels separately.
The default fill colors come from the cards. Color can change without changing a concept's type.
Keep the notation, attribution, and a clear legend when adapting the assets.

Use `assets/catalog.json` to select a type and asset. Use `assets/manifest.json` for provenance and source bounds.
You can copy the asset into SVG, draw.io, slides, or another diagram tool that supports SVG.
Do not describe a Mermaid diagram with generic boxes as exact ArchiMate notation.

## JSON model

The helper uses exact type names from the catalog. It is a local working format, not the Open Group exchange format.

```json
{
  "title": "Order processing",
  "nodes": [
    {"id": "process", "type": "Business Process", "name": "Process Order", "x": 30, "y": 70},
    {"id": "order", "type": "Business Object", "name": "Order", "x": 300, "y": 70}
  ],
  "edges": [
    {"id": "update", "type": "Access", "source": "process", "target": "order", "access_mode": "write"}
  ]
}
```

Each node needs a unique string `id`, an exact `type`, and a `name`.
The connector types `AndJunction` and `OrJunction` do not need names.
Each edge needs a unique `id`, an exact `type`, and node IDs in `source` and `target`.
IDs must be unique across nodes and edges.

For rendering, provide nonnegative `x` and `y` values for every node.
`width` is optional. The default width is 180 units for elements and 18 for junctions.
Height follows the template's aspect ratio. The helper preserves the source symbol's geometry.
Place nodes with enough room for their labels and the type captions below them.

An edge can contain `label`, `points`, and `label_position`.
`points` is a list of nonnegative intermediate `[x, y]` waypoints. The helper adds endpoint anchors.
`label_position` is an explicit `[x, y]` label location.
Access requires `access_mode`: `access`, `read`, `write`, or `read-write`.
Association accepts an optional boolean `directed`. Its default is false.
Use an Influence `label` for a sign or strength when needed.

Keep evidence, state, and assumptions as additional model properties when useful.
The helper preserves the input file. It does not draw those extra properties.

## Commands

Run the commands from the skill folder, or use absolute script and input paths:

```text
python scripts/archimate_model.py validate model.json
python scripts/archimate_model.py render model.json diagram.svg
python scripts/archimate_model.py render assets/examples/order-processing.json diagram.svg
```

The helper requires Python 3.10 or later. It uses only the standard library.
`validate` reports errors and the checks that remain unverified. Errors return a nonzero exit code.
`render` validates first. It rejects missing positions and labels that do not fit rather than truncating them.
Rendering uses explicit positions. It does not provide automatic layout or route edges around other nodes.
Inspect the final diagram. Correct overlaps and crossings with node positions or edge waypoints.
Use [connector validation](connector-validation.md) after each layout change and before delivery.
The helper's `validate` command does not check rendered routing, marker clearance, or label overlap.
The helper draws edges before nodes. An edge that passes through another node can become hidden.

The helper supports element-to-element edges and junctions. Relationship endpoints are outside its working-format scope.
Use a full modeling tool when the model needs relationships as endpoints, formal exchange XML, or a complete admissibility check.
Do not confuse this helper's supported subset with the full ArchiMate language.

## Rebuild the vectors

The packaged vectors do not require the PDF or PyMuPDF at runtime.
To rebuild them from the supplied reference cards, install PyMuPDF and run:

```text
python scripts/extract_assets.py path/to/n221p.pdf --skill-dir path/to/archimate-32
```

The extractor checks the source hash and table row counts. It copies vector paths without tracing pixels.
It records source pages, selection bounds, and file hashes in the manifest.
Curve control points can extend beyond the visible shape. The manifest bounds include those control points.
