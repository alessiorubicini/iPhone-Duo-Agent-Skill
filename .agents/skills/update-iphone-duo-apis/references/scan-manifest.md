# iOS 27.1 Documentation Scan Manifest

Use this list to prevent broad, untraceable documentation scraping. Search official Apple sources for each family, then record canonical pages in `iphone-duo-agent-skill/references/api-status.md`.

## Layout and regions

- `ReservedRegion`, `UIViewReservedRegion`
- SwiftUI `GeometryProxy` reserved-region queries
- UIKit `UIView` reserved-region queries
- Division/occlusion kinds and inactive-region options
- `ArrangementView` and arrangement styles
- `UIArrangementViewController`, placement state, split/overlay arrangement types

## Navigation and bars

- Tab/sidebar placement APIs
- Pinned toolbar placements/groups
- Toolbar/bar item axis behavior
- Vertical bar environment/traits and opt-out behavior
- Compression, visibility priority, and overflow APIs

## Displays and scenes

- SwiftUI hinge context and `onHingeChange`
- UIKit `UIHingeInteraction`
- Dynamic scene activation and `UIWindowSceneActivationAction`
- Scene-accessory model and `CameraCaptureAccessory`

## Camera

- Virtual Front Camera discovery identifier and capability contract
- Inner/outer ultrawide camera device types
- `AVCaptureDeviceDirectionCoordinator` and `AVCaptureDeviceDescriptor`
- `dynamicAspectRatio`
- Camera rotation coordinator behavior across displays
- Camera sensor orientation compensation

## Required evidence per family

- Canonical Apple documentation URL
- Framework/module
- Exact declaration and related types
- Platform availability
- Documented semantics, defaults, and errors
- Concurrency/isolation contract where published
- Released SDK compilation result
- Tech Talk discrepancy, if any
