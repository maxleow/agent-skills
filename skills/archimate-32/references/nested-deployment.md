# Nested deployment views

Prefer a nested arrangement when the reader needs deployment scope and the source confirms a containment hierarchy.
Use it for cloud runtime views and combined deployment views. Follow a user-selected arrangement.
Keep other view styles available when nesting does not answer the question.

## Establish the scope

Record each container ID, member IDs, scope meaning, and evidence before placing objects.
Separate physical deployment from logical membership and access.
Choose an ArchiMate element or Grouping by its meaning. A cloud border alone does not determine its type.

A useful cloud pattern is account → Region → VPC → private worker subnet.
Add a cluster or namespace boundary only when its meaning is supported.
These are examples, not required levels. Global services may have no Region boundary.
Keep an unknown placement outside the specific scope that is unverified. Label that limit.

For managed Kubernetes, distinguish worker placement from the managed control API.
Do not put the control plane in a worker subnet merely because both belong to the same cluster.
Do not place shared namespace workloads on a dedicated application's nodes without evidence.
Use an explicit label for a cluster boundary that shows logical workload membership.

Service and Interface boxes describe behavior and access points. They are not additional deployment resources.
Place them beside their provider. State when their location is a logical presentation choice.
Keep confirmed ownership and service-consumer relationships in the model.

## Arrange one connected canvas

- Put user channels and identity outside the runtime on the left.
- Put the main application providers and their interfaces inside the confirmed workload scope.
- Put shared and external dependencies on the right, with hosting limits stated.
- Put build, deployment, and secret-delivery paths below the runtime.
- Keep supported alternatives in a separate area marked unselected. Add no active-runtime path without evidence.

Use a consistent reading direction. ArchiMate arrows must retain their semantic direction.
Reserve space for provider → interface → exposed service → consumer relationships.
Keep long protocol, authentication, retention, and operating details in nearby numbered annotations.
Leave space below each container title and between nested borders.
Route across a border away from its title. Put a connection label wholly on one side of the border.
Keep connector paths clear of border strokes. A shared stroke can hide which scope a path crosses.

## Reduce duplicate lines

Represent confirmed Grouping membership through containment when it is clearer.
Retain the explicit Aggregation relationships in the model and record which ones the view shows through containment.
Do not also draw every membership line over the same nested objects.
Check each member against the source and the model; nesting must not invent an owner or host.

A combined view can expand a documented component dependency through interfaces and services.
It can omit an existing summary line when that line repeats the same documented dependency.
Keep the original relationship in the model and list the omission in the view record.
Do not remove distinct behavior, access modes, authentication, or data paths to reduce clutter.
Do not claim formal relationship derivation without the full standard or a compatible modeling tool.

## Verify the result

Use [connector validation](connector-validation.md) after each layout change.
Resolve nested child positions through all parents before measuring ports or paths.
Confirm that each member lies inside its intended boundary and below the title space.
Check logical overlays and provider-related display elements separately from physical placement.
Inspect every group title, border crossing, marker, label, and dense area in the final render.
Check that line gaps or bridges distinguish crossings from junctions.

For a revision, compare the old and new views using the same model and renderer.
Record preserved IDs and relationships, containment representations, omitted summary lines, readable scale,
canvas area, visible connectors, crossings, and unresolved defects.
Use these measurements with visual inspection. A smaller canvas alone does not prove a clearer diagram.
