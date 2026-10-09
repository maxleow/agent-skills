# Quality checks

Use these checks before delivery.
For ArchiMate arrows and routing, use [connector validation](../connector-validation.md).
They cover model preservation, appearance, and file behavior.
They do not certify a diagram notation.

## Model preservation

- Compare element IDs and labels with the source.
- Compare relationship endpoints with the source.
- Confirm the original directions and endpoint markers.
- Confirm group membership and required nesting.
- Confirm all required symbols and line patterns.
- Confirm that layout edits did not remove facts or add relationships.
- Record assumptions that affect the model.

For a new model, compare the result with the user requirements.
For a restyle, compare the result with the original model.
Do not use a visual improvement as evidence of semantic correctness.

## Visual inspection

Make a preview with the intended fonts and renderer.
Examine it at the intended display size.
Do these checks:

- Confirm that all text fits.
- Confirm readable labels and clear line breaks.
- Confirm consistent spacing within comparable sets.
- Confirm alignment where alignment helps the reader.
- Confirm enough room for group titles and nested content.
- Confirm that connectors avoid unrelated objects and labels.
- Confirm visible relationship markers at both ends.
- Confirm clear crossings and junctions.
- Confirm that color has a consistent purpose.
- Confirm that labels or other cues support color meanings.
- Confirm that nothing extends beyond the export area.

Examine the reading order from the intended starting point.
Follow each important path to its endpoint.
If you cannot follow a path easily, improve its placement or label.
After a correction, render the affected pages again and inspect all their connectors.
Check both endpoint markers, visible border attachment, and nearby captions.
Confirm that opaque label backgrounds do not hide other text or paths.
Use only previews generated from the final editable source.

## File behavior

- Open the editable source in a compatible tool.
- Confirm that shapes, text, and connectors remain editable.
- Move the source to another folder.
- Confirm that required assets still load.
- Confirm that the export uses the intended fonts and dimensions.
- Confirm that previews contain the same content as the source.

For draw.io, use the checks in [the format reference](drawio-format.md).
For SVG, use the checks in [the output reference](output-formats.md).

If a tool is unavailable, report the affected check as incomplete.
Do not describe XML parsing as a successful editor render.
Do not describe a preview as proof of model standards compliance.
