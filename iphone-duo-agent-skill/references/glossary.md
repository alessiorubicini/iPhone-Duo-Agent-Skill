# Glossary

Use these terms consistently. Definitions describe the Tech Talk model and must not be expanded with unsupported hardware or API detail.

## Arrangement

A two-view layout container whose system-provided rules map environmental inputs to placement and visibility. The talks describe split and overlay arrangements. It is not navigation infrastructure. [TT-111463]

## Closed, partially open, fully open

The three high-level hinge statuses named in the talks. Do not invent angle ranges for them. [TT-111464]

## Configuration

The combined conditions affecting a scene: display, window size, size classes, rotation, Split View/Picture in Picture participation, pose, active reserved regions, and relevant system UI. Do not use `configuration` as a synonym for hinge status alone.

## Direction

A camera's facing relationship to a particular app view. On Duo, fixed `AVCaptureDevice.position` and display-relative direction answer different questions. [TT-111465]

## Displacement

Adjusting the frame of existing content or controls to keep them visible, reachable, and unobstructed as available regions change. Displacement preserves the experience; it does not introduce pose-only functionality. [TT-111463]

## Division region

A reserved region that divides a larger area into smaller usable regions. The fold is represented this way in the talk; inactive fold regions have zero width. [TT-111463]

## Inner display

The display exposed when iPhone Duo is open. Use the term instead of `main`, `large`, or `tablet` display. [TT-111461, TT-111466]

## Occlusion region

A reserved region represented as a smaller frame within view bounds rather than dividing the whole area. The talk uses the active FaceTime camera as the Duo example. [TT-111463]

## Outer display

The display used when iPhone Duo is closed and also available to specific multi-display experiences while open. Use the term instead of `secondary` unless discussing a view's semantic role. [TT-111461, TT-111464]

## Pose

The physical way the device is open, closed, rotated, partially folded, held, or resting. Use pose for product/design discussion; use size classes, geometry, reserved regions, or hinge context as the actual implementation input selected for a task.

## Reserved region

A region representing hardware or system UI that custom layout may need to account for. The talks describe division and occlusion kinds. Exact iOS 27.1 declarations remain documentation pending. [TT-111461, TT-111463]

## Scene accessory

Supplementary UI paired with a scene and shown on an additional display when the system makes that accessory available. Availability is dynamic. [TT-111464]

## Vertical bar

The system-managed side arrangement of navigation, toolbar, and tab controls in applicable Duo configurations. It is an adaptation of existing bar components, not a separate custom bar. [TT-111462]

## Virtual Front Camera

The `AVCaptureDevice` described by Apple as automatically selecting the relevant inner or outer front camera. It exposes capabilities common to both physical cameras. Exact discovery constants and API documentation remain pending. [TT-111465]
