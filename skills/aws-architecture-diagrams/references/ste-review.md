# STE rewrite record

The requested target is **80% compliance with ASD-STE100**.
This target guides the rewrite.
It is not a measured compliance result.

The rewrite covers `SKILL.md` and both Markdown diagram guides.
It keeps the AWS rules, design values, assets, and code examples.

## Language rules

The rewrite uses short sentences, active voice, and direct commands.
Each instruction has one main action.
Conditions come before the actions that depend on them.
Technical terms keep one meaning throughout the guides.
Procedural sentences use a maximum of 20 words where practical.

These choices follow the [official ASD-STE100 guidance](https://www.asd-ste100.org/STE_faq.html).
The [Issue 9 procedure rules](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf) give the sentence length limit.

## Technical terms

Official AWS names, asset names, and code identifiers remain unchanged.
The table defines recurring terms for this skill.
It does not give ASD approval to those terms.

| Term | Meaning in this skill |
| --- | --- |
| Asset | A supplied icon, source file, or preset image |
| Canvas | The area that contains the diagram |
| Group | A box that shows component membership |
| Header icon | The icon at the top of a group |
| Node | A component in the diagram model |
| Connector | A visible line between diagram components |
| Edge | A connection in the architecture model |
| Preset | A supplied object with defined dimensions and appearance |
| Artwork variant | An icon version identified by values such as 32 or 64 |
| Design values | The colors and dimensions in `design-tokens.json` |
| Renderer | A tool that makes an image from the diagram file |
| SVG, JSON, PNG, PDF | File format identifiers |
| CIDR, Region, Availability Zone | AWS or network terms from the architecture source |

Technical verbs include `embed`, `export`, `resize`, `crop`, `flip`, `rotate`, and `recolor`.
Their meanings refer to file operations or diagram artwork.
Paths, filenames, command options, XML attributes, and official names keep their required spelling.

## Review limits

Sentence length checks do not establish full STE compliance.
The review does not include a complete dictionary, part-of-speech, and approved-meaning audit.
Treat the result as an STE-informed rewrite toward the 80% target.
Do not report a certified or verified compliance percentage.

The [official download page](https://www.asd-ste100.org/STE_downloads.html) explains the limits of AI compliance claims.
