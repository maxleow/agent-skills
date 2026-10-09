# Sources and limits

## Supplied primary source

- Title: **ArchiMate 3.2 Specification Reference Cards — Personal PDF Edition**.
- Publisher: The Open Group.
- Publication identifier: **N221**.
- Year: **2022**.
- Supplied filename: `n221p.pdf`.
- Length: **14 PDF pages**.
- Content used: PDF pages **2–13**.

| PDF pages | Content |
|---|---|
| 2 | Eleven relationship types and AND/OR junction notation. |
| 3–4 | Ten motivation elements. |
| 5 | Four strategy elements. |
| 6–7 | Thirteen business elements. |
| 8 | Nine application elements. |
| 9–10 | Thirteen technology elements. |
| 11 | Four physical elements, presented within Technology. |
| 12 | Five implementation and migration elements. |
| 13 | Grouping and Location. |

`assets/catalog.json` records the source SHA-256 and exact type names.
`assets/manifest.json` records each vector's page, source selection, bounds, and SHA-256.
The 60 element meanings are concise paraphrases of the supplied cards.
The templates and alternative symbols use the PDF's vector paths. They omit its text labels.
The read-only Access variant is derived by mirroring the source write variant.
The directed Association symbol corrects a source defect: its lower arrow stroke has zero opacity in the PDF.
The extraction restores that existing stroke. The SVG metadata and manifest record the correction.
The renderer constructs scalable relationship lines from the documented notation. It does not stretch the cropped line symbols.

Copyright © 2022 The Open Group. All Rights Reserved.
ArchiMate® is a registered trademark of The Open Group.
These notices also appear in the extracted SVG metadata.
The user's supplied document remains the source for these local assets. This skill does not grant rights in that document.

## Additional primary references

- [STEMG FAQ](https://www.asd-ste100.org/STE_faq.html): STE principles and the distinction between writing rules and dictionary.
- [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf): the writing standard behind the simplified style target.
- [ArchiMate 3.2 online specification](https://pubs.opengroup.org/architecture/archimate32-doc/): the full standard, when accessible.
- [Model Exchange Format resources](https://www.opengroup.org/xsd/archimate/): formal interchange resources, when that output is requested.

The full online specification required sign-in during this build. Its relationship tables were not copied or inferred.
The exchange-format resource page was used only to identify the separate formal interchange standard.
No exchange serializer or full relationship matrix is included in this skill.

## Claims supported by this skill

The skill covers the definitions and notation on the supplied cards.
The helper checks exact type names, IDs, node references, and selected broad relationship constraints.
The helper also checks numeric layout inputs and reports unsupported properties.
It cannot verify every allowed endpoint pair, derivation rule, or junction rule.
It cannot certify ArchiMate or ASD-STE100 conformance.

Use the full version-matched specification or a modeling tool when a task needs those additional checks.
Record the source and result of each additional check. Keep unverified checks visible in the model review.

## Bundled diagram-design resources

The user requested the inclusion of their local `diagram-design` skill.
Its workflow is integrated in [diagram-design.md](diagram-design.md).
Its six supporting references are in `references/diagram-design/`.
Its generic draw.io example is in `assets/diagram-design/file-structure.drawio`.
The bundle preserves layout rules, design values, output guidance, visual checks, and the design glossary.
Internal links point to the bundled files. No separate design skill is needed.
The writing record follows the confirmed style target and does not carry forward an earlier review score.
The design defaults do not override ArchiMate notation or user instructions.
