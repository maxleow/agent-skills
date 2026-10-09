# Modeling decisions

## Choose by meaning

| Question | Select |
|---|---|
| Who can perform business behavior? | Business Actor |
| What responsibility does that actor have? | Business Role |
| What sequence achieves a business result? | Business Process |
| What behavior is grouped by resources or competence? | Business Function |
| What behavior is exposed to consumers? | A service in the appropriate layer |
| Where can a consumer access that service? | An interface in the appropriate layer |
| What modular application unit provides functionality? | Application Component |
| What environment hosts or uses computational resources? | Node |
| What physical IT resource executes software? | Device |
| What software provides the execution environment? | System Software |
| What non-IT physical machine transforms material? | Equipment |
| What data is structured for automated processing? | Data Object |
| What file or deployment item implements software or data? | Artifact |
| What ability exists? | Capability |
| What approach uses abilities and resources to achieve a goal? | Course of Action |
| What desired end state is intended? | Goal |
| What result or effect occurs? | Outcome |
| What temporary stable architecture state exists? | Plateau |
| What difference exists between two states? | Gap |

A cloud product can require several elements. Choose the type for the architectural role shown in the view.
For example, separate application functionality, the execution environment, and an exposed technology service when the question requires them.
Keep a business actor distinct from a stakeholder's interests. Keep a strategy resource distinct from a specific implementation resource.

## Control scope and state

Use the user's facts and level of detail. Do not invent services, components, goals, dates, or migration steps.
Label an assumption when a useful draft needs one. Preserve unknowns when the assumption would change the architecture.

Separate current and target states with distinct views or explicit state properties.
Use Plateau, Gap, Work Package, Deliverable, and Implementation Event when a migration view needs those concepts.
Do not rename the same model element each time it appears in another view.

Use names that identify actual concepts. Behavior labels can use a verb and object, such as “Approve Order.”
Do not turn a naming preference into a language rule.
Select a standard viewpoint only when it fits the question. Label a custom view as custom.

## Trace the reasoning

For a complex model, keep a compact ledger:

| Item | Record |
|---|---|
| Element | Stable ID, exact type, name, evidence, and state. |
| Relationship | ID, source, target, exact type, label, and relevant properties. |
| Assumption | Assumed fact, reason, and the decision it affects. |
| Validation | Checks completed, checks unavailable, and remaining issues. |

Do not add this ledger to a simple diagram unless it helps the user.
Preserve source locations when the user asks for an evidence-based model.

## Review in two passes

First check meaning. Confirm each type, endpoint, direction, and state against the facts and relevant source rules.
Check collaboration membership, passive structure use, service exposure, and motivation distinctions where they appear.

Then check presentation. Confirm symbols, readable labels, visible arrowheads, and an unambiguous legend.
Use color consistently. The reference-card palette is a useful default, but color does not establish a type.
Nesting needs a documented model relationship. It does not create one by itself.

Report only findings that change the result. State the affected concept, problem, correction, and evidence.
Do not describe an unverified edge as valid merely because its SVG renders.
