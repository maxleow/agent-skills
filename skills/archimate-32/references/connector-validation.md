# Revalidate arrows and lines

Use this procedure for new views and layout revisions.
Keep semantic checks separate from geometry and visual checks.
XML parsing and model validation cannot prove rendered alignment.

## Preserve the relationship

Record each relationship ID, type, source ID, target ID, and label before layout changes.
Include Access mode, Association direction, and Influence signs when used.
Keep this record in the existing model or working data.
For a restyle, compare the result with that record.
For a conversion, compare with the typed ArchiMate model, not the original diagram's request arrows.

Use [relationships.md](relationships.md) to check line patterns, marker shapes, fills, and marker ends.
Check these common cases explicitly:

- Serving points from provider to consumer.
- Access keeps the accessing element as the logical source.
- Read Access has an open arrow at the accessing element.
- Write Access has an open arrow at the passive element.
- Read-write Access has open arrows at both ends.
- Unspecified Access has no arrowhead.
- Composition and Aggregation keep the diamond at the whole.
- Realization and Specialization point to the abstract or general target.
- Assignment keeps its filled circle at the source and filled arrow at the target.
- Undirected Association has no arrowhead.

Do not reverse model endpoints to repair a visual arrow.
Correct the renderer's marker or routing settings instead.
Do not change a relationship type to make routing easier.
Keep exact endpoint admissibility unverified unless a full specification or compatible modeling tool checks it.

## Check geometry

Use the selected editor or renderer to resolve the final connector path.
Stored waypoints do not prove the final path when the editor adds bends or perimeter offsets.

For draw.io, resolve child positions through all parent groups before comparing coordinates.
Resolve edge waypoints in the edge parent's coordinate system.
Check source and target references against visible elements, including supported object wrappers.
Keep connectors attached to element IDs and ports.
Use free endpoint points only for deliberate unattached lines, such as a legend.

Check the following:

- Each endpoint meets the intended visible border or port.
- An arrow tip neither floats in a gap nor enters the element label.
- The start and end segments follow the intended approach direction.
- Orthogonal routes have horizontal or vertical segments after rendering.
- Bends have enough space for the full marker and its line segment.
- Routes have no duplicate points, zero-length segments, or unintended backtracking.
- Comparable ports and parallel lanes align where this helps the reader.
- Separate edges remain traceable through shared or nearby routes.
- Crossings remain distinct from modeled junctions.
- Paths avoid unrelated shapes, corner symbols, captions, and group titles.
- Markers and paths stay inside the export bounds.

Use the chosen grid for comparable bends and lanes.
Do not force a valid diagonal or curved route onto an orthogonal grid.
If a crossing cannot be removed, use a supported crossing treatment that preserves the relationship notation.
Do not add a junction to conceal a crossing.

An SVG image's frame can extend beyond its visible border.
Preserved aspect ratio can add further space inside a frame.
Check the rendered border before selecting perimeter anchors.
Adjust ports or use suitable editable geometry when the frame leaves an endpoint gap.
Preserve the symbol and keep attachment behavior after the change.

## Check labels and stacking

Reserve space for edge labels, element labels, type captions, and group titles.
Measure their rendered bounds with the intended font when possible.
Keep each edge label beside a clear segment of its own path.
Use an explicit label position when automatic placement is ambiguous.

Keep a label's background close to its text bounds.
Do not use a wide opaque caption box that erases another label or connector.
If a background masks a short section of its own line, keep the path traceable on both sides.
Keep backgrounds, group boundaries, connectors, shapes, and labels in a consistent stacking order.
After any stacking change, inspect all nearby text and markers again.
Placing labels above lines does not resolve overlapping labels.

Prefer moving a label or route over reducing text size.
Increase space or split a crowded view when local changes cannot keep paths clear.

## Render and recheck

1. Save the editable source after the last change.
2. Render every affected page with the intended editor, fonts, and export settings.
3. Confirm each preview's page title and content. Do not assume page numbering across tools.
4. Inspect the complete page at its intended display size.
5. Inspect dense areas and both ends of every connector at readable magnification.
6. Trace every connector continuously from its source to its target.
7. Check labels and captions beside the path, including their backgrounds.
8. Correct defects, save, and render the affected pages again.

Check all connectors on a changed page, including connectors you did not edit.
A moved shape or label can affect a nearby path.
After shared style, font, template, or routing changes, recheck all affected pages.
Do not reuse a preview made before the final edit.

When exports run asynchronously, wait for completion before inspecting them.
Confirm successful rendering and newly produced output; an existing output file can be stale.
For scripted exports, compare the source hash before and after rendering when freshness is uncertain.
If the source changes during rendering, export it again.
Do not repair only the preview. Apply the correction to the editable source.

## Completion and review record

Finish when the final previews show correct markers, clear paths, readable labels, and no unresolved connector defects.
Confirm that IDs, endpoint pairs, relationship properties, and group membership still match the model.
Keep a short record in the existing model notes or delivery notes:

| Check | Record |
|---|---|
| Model preservation | Endpoint and relationship-property comparison; any authorized semantic changes. |
| Arrow notation | Checked types, marker ends, fills, and Access modes. |
| Alignment | Checked ports, visible borders, bends, lanes, and crossings. |
| Label clearance | Checked text bounds, backgrounds, captions, and stacking. |
| Final previews | Source revision or hash, page names, renderer, and remaining issues. |
| Full conformance | Verified only with an appropriate full-standard check; otherwise unverified. |

If a renderer is unavailable, mark rendered alignment and label clearance as incomplete.
Report remaining defects plainly. Do not label uninspected pages as visually checked.
