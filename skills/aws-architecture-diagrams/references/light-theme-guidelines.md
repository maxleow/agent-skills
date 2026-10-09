# AWS rules for light backgrounds

The source is the supplied AWS Architecture Icons file, release **24-2026.07.31**.
It contains 156 slides.
The slide references below identify that source.
This document restates its design rules.
It does not confirm later AWS releases.

Use `design-tokens.json` for exact colors and dimensions from the source shapes.
Use the preview images to examine preset appearance.
For the source checksum and asset notices, read [the source record](source-provenance.json).

## Canvas and assembly

The source has versions for light and dark backgrounds.
Light backgrounds are usual for web diagrams.
Select the version for the required medium.
Start with the boundary groups.
Add the service and resource icons.
Connect the components.
Add process numbers if necessary.
Use the examples to help with layout.
Do not copy their architecture into an unrelated request.
**[Slides 11, 20–21]**

For a portrait document, the recommended PowerPoint canvas is **6.5 inches wide by 8.75 inches high**.
Use a white background.
Apply the same diagram rules.
The source recommends a grouped diagram that you can copy into Word as a picture.
Keep an editable source when you deliver a picture.
**[Slide 12]**

This skill uses white as the default for ordinary light diagrams.
The source requires white for portrait diagrams and Training and Certification.
It does not require one page size for all light diagrams.

## Groups

Use the preset boundary style.
Most groups contain an outline, label, and header icon.
Availability Zone, security group, and generic group presets have **no icon**.
Do not add an invented icon to those presets.
Resize the boundary box.
Keep the header icon size unchanged.

Leave at least **0.05 inch** between nested boxes on all sides.
Leave additional space for headers and readable content.
An Auto Scaling group can cross multiple groups.
VPCs and subnets can contain nested groups.
If no preset suits the diagram, use a generic group.
**[Slides 14, 25]**

The table gives the outline values from slide 25.
The standard outline width is **1.25pt** (15875 EMU).
The source boxes have no interior fill.
Keep their interiors transparent when you nest groups.

| Preset | Color | PowerPoint dash preset | Header icon |
| --- | --- | --- | --- |
| AWS Cloud | `#000000` | solid | AWS logo, or cloud alternative |
| Region | `#00A4A6` | sysDash | Region |
| Availability Zone | `#00A4A6` | dash | none |
| Security group | `#DD344C` | solid | none |
| Auto Scaling group | `#ED7100` | dash | Auto Scaling, centered above label |
| Virtual private cloud (VPC) | `#8C4FFF` | solid | VPC |
| Private subnet | `#00A4A6` | solid | Private subnet |
| Public subnet | `#7AA116` | solid | Public subnet |
| Server contents | `#7D8998` | solid | Server |
| Corporate data center | `#7D8998` | solid | Corporate data center |
| EC2 instance contents | `#ED7100` | solid | EC2 |
| Spot Fleet | `#ED7100` | solid | Spot Fleet |
| AWS account | `#E7157B` | solid | AWS account |
| AWS IoT Greengrass Deployment | `#7AA116` | solid | Greengrass Deployment |
| AWS IoT Greengrass | `#7AA116` | solid | Greengrass |
| Elastic Beanstalk container | `#ED7100` | solid | Elastic Beanstalk |
| AWS Step Functions workflow | `#E7157B` | solid | Step Functions |
| Generic group | `#7D8998` | dash or solid | none |

Use the Cloud group with the AWS logo by default.
If the target Region does not permit that logo, use the Cloud group with the cloud icon.
Slide 25 gives China as an example.
This statement records the source design note.
It does not give legal advice.

### Make a custom service group

Select the template with the correct category color.
Change the group label.
Replace the square with the official **32-variant service SVG**.
The source recommends SVG instead of PNG for image quality.
The asset package uses directories such as `Arch_Compute/32/`.
Do not depend on the older source directory name `Arch_32`.
**[Slide 26]**

| Custom-group category set | Outline color |
| --- | --- |
| Analytics; Games; Networking & Content Delivery; Serverless | `#8C4FFF` |
| Application Integration; Management Tools; Multicloud & Hybrid | `#E7157B` |
| Cloud Financial Management; Internet of Things; Storage | `#7AA116` |
| Artificial Intelligence; End User Computing; Migration & Modernization | `#01A88D` |
| Blockchain; Compute; Containers; Media Services; Quantum Technologies | `#ED7100` |
| Business Applications; Customer Experience; Front-End Web & Mobile; Security & Identity | `#DD344C` |
| Customer Enablement; Databases; Developer Tools; Satellite | `#C925D1` |

Template colors and icon colors can differ slightly.
Keep each supplied asset unchanged.
Do not change icon colors to make them match a template.
Some directories use older category names, such as Management-Governance or Machine-Learning.
Search for the actual service name.

## Icons

Keep diagram icons at their preset size, color, and format.
Do not crop, flip, rotate, recolor, stretch, or change their shapes.
The source permits proportional size changes for presentation use.
Keep the aspect ratio when you use that exception.
Do not use it to make ordinary diagram icons smaller.
**[Slide 15]**

The usual service icon is **60pt square** in the source.
Its 64-variant asset has an **80px square canvas** at 96 CSS pixels per inch.
Resource icons are usually **36pt / 48px**.
Group header icons are usually **30pt / 40px**.
These measurements come from the source and assets.
They are not additional AWS rules.
If a preset has different dimensions, use its actual values.
A filename variant does not always specify the complete canvas size.

Use the service icon from the correct functional category for each serverless component.
A Serverless category icon can show a serverless architecture as a whole.
**[Slide 147]**

## Connectors

Use the source presets or equivalent default connectors.
Use **Open Arrow, Size 4**.
The Open XML values are `type="arrow"`, `w="med"`, and `len="sm"`.
These arrowheads have no fill.
The standard connectors on slide 27 are **black, 1.25pt**.
Use straight segments and right angles where possible.
If necessary, use a diagonal connector from the source.
Do not replace these arrows with decorative, curved, or filled-triangle arrows.
The source also has plain lines and arrows with heads at both ends.
**[Slides 16, 27]**

Use arrowheads at both ends only for a connection with flow in both directions.
A plain line shows a connection without a flow direction.
If a connection is unclear, use a legend or a short edge label.
These last recommendations are layout advice, not additional AWS rules.

## Labels

Use **12pt Arial** for ordinary icon labels.
Keep labels separate from icons.
You can change general resource labels for the required use.
Keep AWS service names on no more than **two lines**.
Keep `AWS` or `Amazon` on the same line as the first word of the service name.
Do not divide a word between lines.
Do not add a hyphen within a word to divide it.
If necessary, make the label wider or use an established abbreviation.
**[Slide 17]**

Give the full service name before you use its short form.
For a separate diagram, you can give full names in a small legend.
Do not use the same abbreviation for different services.
A role label such as `Output bucket` can supplement the service or resource name.
Keep the AWS service identity clear.

## Numbered callouts

Callouts identify process steps.
The presets are black circles with bold white Arial numerals.
Use one preset size throughout the diagram.
Do not stretch the circles.
Do not change the colors or font size.
Do not create other callout shapes.
Do not replace numbers with letters.
The source presets contain numbers **1–10**.
Use large callouts for simple diagrams.
Use small callouts for dense diagrams.
Arrange numbers in a clear reading order.
Keep callout placement consistent.
**[Slide 18]**

The table gives the measured preset dimensions:

| Set | Diameter | Numeral size |
| --- | --- | --- |
| Large | 0.36 inch / 25.92pt / 34.56 CSS px | 14pt, bold |
| Small | 0.30 inch / 21.60pt / 28.80 CSS px | 11pt, bold |

Slide 18 refers to team conventions.
Follow conventions that the user already supplies.
Do not make a routine diagram depend on contact with other people.
If the process has more than ten steps, use separate views or an external sequence list.
Do not invent a new preset.

## Training and Certification

Use this profile only for Training and Certification diagrams.
**[Slide 13]**

- Use a white background.
- Use **16pt black** type throughout the diagram.
- Keep icon sizes fixed.
- Keep icon colors unchanged.
- Use **2pt** lines throughout the diagram.
- Keep the supplied line colors.

This profile replaces the ordinary 12pt labels and 1.25pt line widths.
The callout presets have white numerals.
That format conflicts with the requirement for black type throughout the diagram.
Unless the user gives an explicit exception, omit optional numbered callouts for this profile.

## Layout recommendations

These recommendations supplement the source rules:

- Use a left-to-right layout for a simple request or data path.
- Use a top-to-bottom layout for a portrait diagram.
- Align repeated components.
- Keep spacing consistent.
- Leave space for two-line labels and group headers.
- Keep text at least 16px from group borders, inside and outside each group.
- Prefer a 24px gap where space permits.
- Measure from the painted border edge to the text at the intended display size.
- Reject smaller gaps, even without overlap.
- Put connectors in empty spaces.
- Keep connectors away from labels and unrelated icons.
- Reduce crossings without a change to the actual connections.
- If the diagram is too dense, use multiple views.
- Keep icons and type at their prescribed sizes.
- Use a legend when color alone does not explain a flow or boundary.
- Examine the architecture separately from the visual style.

A box with the correct color can still put a managed service within the wrong network boundary.
