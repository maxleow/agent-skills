# Visual rules

These rules generalize layout principles from the supplied AWS guide.
They do not transfer AWS notation, colors, or fixed icon dimensions.
The numeric values are recommended starting points for this skill.
They are not an external diagram standard.

## Canvas and scale

Set the canvas for the intended medium.
Use the supplied page dimensions when the user gives them.
Keep important content within the page margins.
Make the final preview at the intended display size.

Use **96 CSS pixels per inch** for an SVG with pixel coordinates.
In that coordinate system, **12pt equals 16px**.
Keep a consistent unit system throughout the file.
Do not mix points and pixels without conversion.

If the diagram requires more space, enlarge the canvas or divide the content into views.
Keep text readable in each view.
Increase raster resolution for sharper exports.
Do not change model geometry only to increase export resolution.

## Spacing and alignment

Use an **8px grid** as a starting point.
Snap comparable shapes to common rows or columns.
Use consistent gaps within a related set.
Leave additional space between separate clusters.
Allow enough space for connector labels and endpoint markers.

Use these initial values where no template defines them:

| Setting | Starting value |
| --- | --- |
| Shape padding | 12–16px |
| Gap between comparable shapes | 24–40px |
| Group padding | At least 24px, plus title space |
| Page margin | 24–32px |
| Minimum connector corridor | 16px, more for labels |

These values depend on the font, symbols, and display size.
Increase them when labels or markers need more space.
Do not reduce a required domain dimension to fit the grid.

Use consistent widths for comparable elements when their content permits it.
Allow different heights when content differs.
Do not force every object to the same dimensions.
Keep required symbol proportions unchanged.

## Text

Use **Arial, 16px** for ordinary labels as a starting point.
Use **18px bold** for group titles.
Use **24px bold** for the page title when a title helps.
Keep the font sizes consistent within each role.

Use short labels with direct words.
Keep technical names, IDs, and important qualifiers exact.
Do not shorten a label if the change alters its meaning.
Explain unfamiliar abbreviations in a legend or note.

Avoid line breaks within words.
Use manual line breaks where the text reads naturally.
Widen a shape when the label needs more space.
Put long explanations outside the main shape.

Measure text with the actual font when possible.
Then examine the preview.
A character count cannot confirm text fit.

## Color and hierarchy

Use white or another neutral background.
Use dark text and visible outlines.
Use a small color set with consistent purposes.
Keep the same meaning for a color across views.

Use a legend when color meaning is unfamiliar.
Use labels or other cues in addition to color.
Confirm that the diagram remains understandable without color.

Use color to support the content hierarchy.
Keep ordinary elements quieter than the main focus.
Avoid gradients, shadows, and decorative borders unless the user requests them or a template requires them.

If a notation or brand defines a color, keep that color.
Do not replace required colors with the neutral theme.

## Groups

Use group boxes only for a real relationship or a stated visual organization.
Keep titles at a consistent position.
Leave clear space below each title.
Keep nested content inside its parent boundary.
Leave space between inner boxes and outer borders.

Containment can carry meaning in the selected notation.
Do not add or remove nesting without a basis in the model.
If you need a purely visual cluster, use whitespace or an annotation that cannot imply a new relationship.

Use transparent or very light group fills when they improve readability.
Keep parent content and connectors visible.
Do not use an opaque fill that hides important objects.

## Connectors

Use straight or orthogonal paths when they suit the notation and structure.
Keep the chosen path style consistent within a related set.
Use curved or diagonal paths when the structure or notation requires them.

Connect lines to the intended objects or ports.
Keep lines clear of unrelated shapes and labels.
Avoid long parallel runs that make endpoint identity unclear.
Use extra spacing rather than overlapping arrowheads.

Move secondary paths away from the main reading path where practical.
Reduce crossings without changing the relationships.
If crossings remain, use the crossing treatment that the notation or editor supports.
Do not create a junction where the model has none.

Keep every required arrowhead, endpoint marker, and line pattern.
Do not apply one arrow style to all relationships.
Set line widths consistently within each relationship role.

## Layers

Put backgrounds and group boundaries behind the main objects.
Keep connectors visible between their endpoints.
Put labels above lines when necessary for legibility.
Keep annotations visually distinct from model elements.

After any layer change, examine the preview.
Confirm that no line, marker, or label disappears behind another object.
