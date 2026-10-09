# Drawing procedure and asset use

All paths in this reference start from the skill folder.
The helper uses only the Python standard library.
Replace `python` with the Python executable in your environment.
Find the script from the skill folder.
You can execute it from a different working directory.

## Find icons

```text
python scripts/find_icons.py "Lambda" --kind service --variant 64
python scripts/find_icons.py "S3 bucket" --kind resource
python scripts/find_icons.py "user" --kind general
python scripts/find_icons.py "private subnet" --kind group
python scripts/find_icons.py "Lambda" --kind service --variant 32
```

The helper returns JSON with these values:

- Relative path and absolute path.
- Artwork variant.
- Actual width, height, and `viewBox`.
- Recommended size for an ordinary diagram.

The search matches all query words.
Punctuation does not affect the match.
The helper also recognizes common abbreviations such as S3 and KMS in filenames with full service names.
It does not interpret other informal names.
If a search gives no results, try the official service or resource name.
If several assets match, select the correct asset for the component.

The default search returns up to 20 results.
It excludes dark variants.
Use `--limit` to change the result limit.
Use `--include-dark` to include dark variants.
An unsuccessful search returns `matches: []` and `total_matches: 0` with a successful exit status.
Do not create an unofficial icon because a search gives no results.

Use `assets/icon-index.json` through the helper.
Do not read the full catalog into the agent context.
The folder `assets/presets/groups/` contains exact group header artwork from slide 25.
It includes three headers that the original group icon directory does not contain.
The catalog identifies these assets with `source_slide: 25`.

Use these artwork variants:

| Use | Variant |
| --- | --- |
| Ordinary service icon | 64 |
| Resource icon | 48 |
| Custom group header | 32 service variant |

Use `references/design-tokens.json` for exact group header paths and dimensions.
Keep the supplied release by default.
Get newer assets only when the user requests them or the required icon is missing.

## Prepare the layout

Make a model with stable IDs for groups and nodes.
Record group membership and directed edges.
Keep dimensions and connector waypoints separate from architecture facts.
A layout change must not change a service relationship.

If the input is infrastructure code, separate actual deployments from proposed changes.
Record variables with unknown values.

Find the intended page or screen size before placement.
If no display width is given, use a 1280px-wide preview as a starting point.
Aim for ordinary labels of at least 14px in that fitted preview.
These review values are layout recommendations, not AWS rules.
Use an overview for the main request or data path.
Put placement and configuration details in a separate view when they reduce overview readability.
Preserve membership facts across views.
Show only the boundaries needed to explain each view.
Keep omitted placement detail in a clearly linked detail view.
Do not invent placement or remove facts to simplify a view.
Keep support sections compact.
Reserve more space for the main path and its labels.

Set the canvas size to contain the diagram.
Use the group presets from the design values.
Keep group interiors transparent.
Leave the minimum space between nested boxes.
Leave additional space for headers and labels.
Reserve the complete header height before you place group content.
Leave a clear gap between the header and the first content row.

The **0.05-inch** minimum equals **4.8 CSS pixels** at 96 pixels per inch.
This value specifies the space between boundaries.
It does not give enough space for a header or a node by itself.

## Make an SVG

Use an SVG with embedded assets as the default output.
Add a white background.
Add a title and description for accessibility.
Use editable `<text>` labels.
Use separate layers for groups, connectors, icons, and labels.

Set physical dimensions with the correct unit conversion.
At **96 CSS pixels per inch**, use these values:

| Source value | SVG value |
| --- | --- |
| 12pt label | 16px |
| 1.25pt line | 1.666667px |
| 2pt line | 2.666667px |
| 6.5 by 8.75 inch portrait canvas | 624 by 840 viewBox |

In this coordinate system, `font-size="12"` means 12px, not 12pt.

Embed the original SVG bytes as `data:image/svg+xml;base64,...` images.
Keep the actual icon width and height.
If the tool requires inline paths, give each internal ID a unique prefix.
Update all references to those IDs.
Do not change the artwork.

Put the white page rectangle behind all other objects.
Do not add opaque fills to group boxes.
Opaque fills can hide parent content or connectors.

Use this layer order:

1. Boundary boxes.
2. Connectors.
3. Icons.
4. Labels.
5. Optional callouts.

Keep connector endpoints outside the artwork.
Keep endpoints away from label boxes.
Keep endpoints close enough to identify their visible icons or ports.
Keep paths outside group headers, header icons, and title areas.
Reserve clear corridors where paths cross boundaries.
Use separate attachment points when several connectors share an icon.
Keep each connection label outside every other connector path.
Do not hide a collision with an opaque label background.
If the diagram is too dense, increase the spacing or canvas size.
Do not reduce ordinary diagram icon sizes.
Use the colors and dash styles in the design values.
If an SVG dash pattern differs from the PowerPoint preset, state the difference.
Do not claim an exact match for an approximate pattern.

### Set the arrow style

Use an open chevron marker with no fill.
Point the marker along the connector path.
Keep marker sizes consistent.
Use this example for an ordinary diagram:

```xml
<marker id="open-arrow" viewBox="0 0 8 8" refX="7" refY="4"
        markerWidth="6" markerHeight="6" orient="auto-start-reverse"
        markerUnits="strokeWidth">
  <path d="M 2 1 L 7 4 L 2 7" fill="none" stroke="#000000"
        stroke-width="1" stroke-linejoin="miter"/>
</marker>
```

This SVG marker gives a similar appearance to the PowerPoint arrow.
It does not reproduce PowerPoint **Size 4** exactly.
For exact native arrows, copy the connectors from the supplied PowerPoint file.
Set ordinary connector strokes to **1.666667px**.
Attach the marker only to the intended arrow end.
Use explicit waypoints for right-angle paths.

### Add labels

Use Arial for labels.
Add manual line breaks where necessary.
Use the actual font to measure the text, or examine an image of the diagram.
A character count does not confirm that a label fits.
Include text padding and all wrapped lines when you set box height.
Keep labels outside unrelated boundary lines.

Give the full service name before you use a short form.
For a separate diagram, you can give full names in a small legend.
Use black labels for ordinary diagrams.
Use the component name and role as the main label.
Put required ports or paths on the relevant connections when practical.
Put configuration details and caveats in numbered notes or a linked document.
Keep facts needed to understand the view on that view.
Keep qualifiers that distinguish proposed, existing, and unverified components.
For Training and Certification, use the specified text and line colors.

### Export an image

If the user requests PNG or PDF, export it from the vector source.
Make the image at the required physical size.
For more image detail, increase the raster resolution.
Keep the artwork size relative to the diagram unchanged.
Include the editable SVG with the image when appropriate.

## Make a draw.io diagram

Use native vertices for boundary boxes and text.
Use native edges with explicit paths.
Insert the supplied SVG artwork as embedded image vertices.
Keep the aspect ratio.
Use the native display dimensions.
Use the source font, outline colors, and line widths.
Use an open arrow with no fill.
Do not use a library default with a filled arrowhead.
Deliver the editable `.drawio` file and the requested image.

A generic AWS stencil can contain older artwork.
Use the supplied assets unless the user selects that stencil.
Set the page size and unit conversion to match the source dimensions.

If an icon and label share an invisible group, attach edges to the icon vertex or a defined port.
Do not use that group's outer rectangle as the visible connection target.
Keep endpoints outside the artwork and close to the icon boundary.
Keep connection labels attached to their edges when the editor supports this.
Valid endpoint IDs do not prove a clear visual connection.
After moving a vertex, recalculate any explicit edge waypoints.

## Make a PowerPoint diagram

Use the presentation tools in the agent environment.
If the editor supports native objects, copy the groups, arrows, and callouts from the supplied file.
Otherwise, use the extracted design values to reproduce their dimensions.
Keep labels and connectors editable.
Insert icons as SVG objects.
Do not replace an editable slide with one image.

Use these source slides:

| Object | Slide |
| --- | --- |
| Groups | 25 |
| Custom groups | 26 |
| Arrows | 27 |
| Callouts | 18 |

The source permits proportional icon size changes for presentation use.
If this exception helps the requested slide, use a consistent scale.
Keep aspect ratios and artwork unchanged.
Keep the proportions of group headers.
For Training and Certification, keep fixed icon sizes.
For a separate diagram export, use native sizes by default.

## Do the final checks

Make an image with a suitable SVG, browser, diagram, or presentation renderer.
Examine the image at the required display size.
Examine the complete diagram, including any scaling needed to fit the target page or screen.
Use enlarged areas only to investigate details.
Do these checks:

- Confirm the correct service and resource artwork.
- Confirm the complete icon canvas and aspect ratio.
- Compare group membership with the architecture.
- Confirm that all headers, nodes, and labels fit.
- Confirm readable labels and correct line breaks in AWS names.
- Confirm connector endpoints and directions.
- Confirm that every endpoint clearly identifies a visible icon, component, or port.
- Confirm that no endpoint appears to terminate in blank space or a descriptive label.
- Confirm that paths avoid group headers, header icons, and titles.
- Confirm visible arrowheads.
- Confirm that labels do not cover edges.
- Confirm the alignment of repeated components.
- Confirm the minimum space between nested groups.
- Confirm the correct ordinary or Training and Certification profile.
- Move the exported source to another folder.
- Confirm that it opens without external local-file dependencies.

Follow each main path from its source to its destination.
Reject a layout where an important connection appears disconnected.
If the complete view is unreadable, separate the overview from the details.

Record each detected defect by object or connection ID.
Where geometry is available, test paths against unrelated nodes, labels, and header artwork.
Use text bounds from the renderer or the actual font.
Measure the shortest gap from text bounds to each painted group border.
Include border thickness, text padding, and all wrapped lines.
Check titles, captions, node text, and connection labels on either side of every nearby group.
Require at least 16px at the intended display size.
Prefer a 24px gap where space permits.
Reject smaller gaps, even without overlap.
Record the label ID, group ID, and measured gap for each failure.
These clearance values are layout recommendations, not requirements from the AWS source guide.
Compare nested group spacing with the selected presets.
Correct attachment points, label positions, or paths as necessary.
Make another image after each correction.
Repeat the geometry checks for the changed layout.
Examine the exact final exports at the required display size.
Resolve detected overlaps and disconnected flows before delivery.
Record unavailable checks separately from passed checks.

If the format cannot keep an exact native preset, state that limit.
Mermaid can show a preliminary topology.
Ordinary Mermaid nodes do not use the official icons that this skill requires.
Use an icon-based output unless the user requests only Mermaid.
