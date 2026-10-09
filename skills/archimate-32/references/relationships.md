# Relationships and connectors

Source: N221, PDF page 2. The table below explains logical source and target.
Arrowheads can show a different direction for Access. Diamonds mark the whole, not the part.

| Type | Use | Logical source → target | Line and endpoint symbols |
|---|---|---|---|
| Composition | The whole consists of its parts. | Whole → part | Solid line; filled diamond at the whole. |
| Aggregation | The whole combines other concepts. | Whole → member | Solid line; hollow diamond at the whole. |
| Assignment | Allocate responsibility, behavior performance, storage, or execution. | Responsible or executing element → assigned element | Solid line; filled circle at source; filled arrow at target. |
| Realization | A concrete concept contributes to creating, achieving, sustaining, or operating a more abstract concept. | Concrete → abstract | Dotted line; hollow triangle at target. |
| Serving | Provide functionality to another element. | Provider → consumer | Solid line; open arrow at target. |
| Access | Behavior or active structure uses passive structure. | Accessing element → passive element | Dotted line; arrowheads depend on access mode. |
| Influence | Affect a motivation element. | Influencing concept → affected motivation element | Dashed line; open arrow at target; optional sign or strength label. |
| Association | Relate concepts without a more specific relationship. | Related concept → related concept | Solid line; no arrow, or an open arrow for directed association. |
| Triggering | Show temporal or causal dependence. | Cause or preceding concept → triggered concept | Solid line; filled arrow at target. |
| Flow | Transfer something between concepts. | Sender → receiver | Dashed line; filled arrow at target. |
| Specialization | Show that one concept is a particular kind of another. | Specific → general | Solid line; hollow triangle at target. |

The source uses short dot-like dashes for Realization and Access. Keep these distinct from the longer Flow and Influence dashes.

## Access modes

Keep the logical source as the accessing element in the model. Do not reverse source and target for a read.

| Mode | Meaning | Visible arrowhead |
|---|---|---|
| access | Access with unspecified read or write behavior. | Neither end. |
| read | The accessing element observes passive structure. | At the accessing element. |
| write | The accessing element changes passive structure. | At the passive element. |
| read-write | The accessing element observes and changes passive structure. | At both ends. |

The card shows unspecified access, write, and read-write. The read SVG mirrors the write symbol and records that derivation.

## Junctions

An AND junction uses a filled circle. An OR junction uses a hollow circle.
Use the junction to join relationships of the same type. It is not an architecture element from the 60-element catalog.
AND means all connected branches participate. OR means one or more branches can participate.
Check the standard's junction rules for the selected type and endpoints before making a conformance claim.
Do not use a junction as an unlabeled process or a generic decision box.

## Review an edge

Read each edge as a sentence before drawing it. For example: “The Application Service serves the Business Process.”
Use Triggering for an execution dependency. Use Flow for an identified transfer.
If both facts exist, model two relationships. Label the flow with what moves when that helps the reader.

Check relationship admissibility for the exact endpoint pair.
These definitions are not an allowed-relationship matrix. Broad category checks cannot prove every edge is permitted.
Do not apply a guessed transitive rule to derive an edge.

For Composition and Aggregation, the diamond stays at the logical source when the layout changes.
For Realization and Specialization, the triangle points to the logical target.
For Serving, the arrow points to the consumer.
