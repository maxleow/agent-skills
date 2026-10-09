# SVG and presentation output

Use the format that the user requests.
Keep the diagram editable where that format permits it.
Do not replace editable model objects with one full-page image unless the user requests that output.

## SVG

Set a `viewBox` that contains all visible content.
Set the required physical or display dimensions.
Keep a consistent coordinate system.
At 96 CSS pixels per inch, 12pt equals 16px.

Use vector shapes and editable `<text>` elements where possible.
Use groups with stable IDs for related objects.
Add a title and description for accessibility.

Embed required images in the SVG.
Keep their aspect ratios and required artwork unchanged.
Do not use local file paths that fail after delivery.
If you insert inline SVG assets, give each internal ID a unique prefix.
Update references to those IDs.

Use the connector markers and line styles from the selected notation.
Keep text clear of connector paths.
Use explicit positions when automatic layout causes overlaps.

Parse the SVG as XML.
Confirm unique IDs and valid internal references.
Make a preview with a compatible renderer.
Examine font substitutions, text fit, clipping, and marker visibility.

If fonts are unavailable, use a suitable substitute.
State any change that affects appearance.
Do not convert all text to outlines when editable text is required.

## Presentation files

Use the presentation tools available in the target environment.
Keep shapes, labels, and connectors as native objects where possible.
Use vector assets for icons and other artwork.
Keep the aspect ratios of those assets.

Arrange the diagram for the slide dimensions and intended audience.
Leave enough space for titles and required notes.
Use consistent fonts and visual roles across slides.

Group objects when that helps editing.
Keep the connector attachment points correct after group changes.
Make slide previews before delivery.
Examine each preview at the expected presentation size.

This skill does not include a PowerPoint source deck.
Use a user-supplied template when the task requires one.

## Image and PDF exports

Export from the editable source.
Use the required physical dimensions and resolution.
Keep all visible content inside the export bounds.
Examine the export for missing assets and font changes.
Keep the editable source available when appropriate.
