# iOS 27.1 API Status

Consult this ledger before producing Duo-specific code. Every entry below is **Documentation pending**: the name or snippet appears in an Apple Tech Talk, but the iOS 27.1 API reference has not been verified.

This file records evidence, not a reconstructed SDK. Ellipses in snippets intentionally preserve unknown implementation detail.

## Status meanings

- **Shown** — Apple displayed the spelling in a code snippet.
- **Named** — Apple stated the API name or concept without enough syntax to reconstruct a declaration.
- **Documentation pending** — do not infer anything beyond the shown/stated evidence.
- **Verified API documentation** — reserved for future updates with a canonical Apple documentation URL and verification date.

## Layout and reserved regions

| Symbol/family | Talk evidence | Evidence limit |
|---|---|---|
| `ReservedRegion`, `UIViewReservedRegion` | Named as SwiftUI/UIKit APIs for custom UI outside the safe area. [TT-111461] | No declarations shown. |
| `GeometryProxy.reservedRegions(kind:)` | Shown with `.division` and `.occlusion`. [TT-111463] | Return type and full signature not shown. |
| `GeometryProxy.reservedRegions(kind:options:)` | Shown with `.includeInactive`. [TT-111463] | Option-set declaration and combinations not shown. |
| `UIView.reservedRegions(kind:)` | Shown with `.division`. [TT-111463] | Full signature and coordinate semantics not documented here. |
| Reserved-region `frame`, active/inactive state | `frame` mapping shown; behavior described. [TT-111463] | Exact types and observation semantics not shown. |
| `ArrangementView` | SwiftUI primary/secondary builder usage shown. [TT-111463] | Generic declaration and availability not shown. |
| `arrangementViewStyle`, `.split`, `.split.axes(.horizontal)`, `.overlay` | Shown. [TT-111463] | Full style types and axis fallback contract not documented here. |
| `overlayArrangementZIndex` | SwiftUI environment access shown. [TT-111463] | Environment value declaration not shown. |
| `UIArrangementViewController` | Construction, `setViewController(_:for:)`, `updateArrangement(_:)`, and `state(for:)` shown. [TT-111463] | Full UIKit declarations/lifecycle not shown. |
| `UISplitArrangement` / `.split.axes(.horizontal)` | Type named and call spelling shown. [TT-111463] | Type relationships and overloads not shown. |

## Navigation, bars, and presentations

| Symbol/family | Talk evidence | Evidence limit |
|---|---|---|
| `defaultTabBarPlacement(.sidebar)` | SwiftUI use shown. [TT-111461] | Availability and surrounding type details not shown. |
| `tabBarController.sidebar.preferredPlacement = .sidebar` | UIKit use shown. [TT-111461] | Property declarations not shown. |
| `topBarPinnedTrailing`, `pinnedTrailingGroup`, `leadingItemGroups` | SwiftUI/UIKit use shown. [TT-111462] | Full placement/group declarations not shown. |
| `axisBehavior`, `.horizontalOnly`, `.verticalPreferred` | SwiftUI/UIKit toolbar-item use shown. [TT-111462] | Complete behavior enum/defaults not shown. |
| `toolbarVerticalEdge`, `traitCollection.verticalBarEdge` | SwiftUI environment/UIKit trait use shown. [TT-111462] | Value types and cases not shown. |
| `toolbarVerticalCompressionBehavior(.prefersToolbarItems)` | SwiftUI use shown. [TT-111462] | Full behavior set not shown. |
| `navigationItem.verticalBarCompressionBehavior = .prefersBarItems` | UIKit use shown. [TT-111462] | Full behavior set not shown. |
| `ToolbarOverflowMenu` | SwiftUI builder use shown. [TT-111462] | Declaration and containment rules not shown. |
| `navigationItem.additionalOverflowItems` | UIKit assignment with `UIDeferredMenuElement` shown. [TT-111462] | Complete property contract not shown. |
| `visibilityPriority` | SwiftUI/UIKit `.high` use shown. [TT-111462] | Priority type and custom values not shown. |
| `toolbarVerticalBehavior(.disabled)` | SwiftUI use shown. [TT-111462] | Full behavior type not shown. |
| `preferredVerticalBarBehavior` / `UIVerticalBarBehavior` | UIKit override shown returning `.disabled`. [TT-111462] | Availability and other cases not shown. |

## Displays, scenes, and hinge

| Symbol/family | Talk evidence | Evidence limit |
|---|---|---|
| `onHingeChange` | SwiftUI modifier shown with previous/current context. [TT-111464] | Context and hinge types are unnamed in the talk. |
| Hinge `status`, `.partiallyOpen`, and `angle` | Access shown; closed/partially open/fully open statuses stated. [TT-111464] | Angle range, units beyond shown `Angle`, cadence, and delivery contract not shown. |
| `UIHingeInteraction` | Named as UIKit counterpart. [TT-111464] | No declaration or usage shown. |
| `UIWindowSceneActivationAction` | Named as an action that automatically hides when new windows are unavailable. [TT-111464] | Construction and error-handling declarations not shown. |
| `sceneAccessory` | SwiftUI modifier shown. [TT-111464] | General accessory protocol/type system not shown. |
| `CameraCaptureAccessory` | Shown with content, `isEnabled:` binding, and `onAvailabilityChange`. [TT-111464] | Full declaration, callback type, and availability contract not shown. |

## Camera

| Symbol/family | Talk evidence | Evidence limit |
|---|---|---|
| Virtual Front Camera discovery | Behavior and discovery through `AVCaptureDeviceDiscoverySession` using front position plus wide/ultrawide types described. [TT-111465] | Exact virtual-camera device type constant is not shown. |
| `.builtInOuterUltraWideCamera`, `.builtInInnerUltraWideCamera` | Names shown in direction-coordinator setup and described for physical-camera access. [TT-111465] | Discovery combinations and availability declarations not shown. |
| `AVCaptureDeviceDirectionCoordinator` | Initializer use shown with `view`, device types, and change handler; Apple states it is in AVKit. [TT-111465] | Full declaration, map types, lifecycle, and error contract not shown. |
| `AVCaptureDeviceDescriptor` | Named as main-actor-safe and sendable, suitable for transfer to a camera actor. [TT-111465] | Declaration and device-construction API not shown. |
| `AVCaptureDevice.dynamicAspectRatio` | Property shape shown as `AVCaptureDevice.AspectRatio?`. [TT-111465] | Selection/mutation API and supported values not shown. |
| `AVCapturePhotoOutput.isCameraSensorOrientationCompensationEnabled` | Boolean property shape shown. [TT-111465] | Availability and interaction with specific rotation APIs not shown. |

## Existing APIs with stated Duo behavior

These names are not necessarily new in iOS 27.1, but their Duo behavior is part of the talks. Verify current Apple documentation before changing code around them.

| API | Duo-specific talk evidence |
|---|---|
| SwiftUI size-class environment / UIKit trait collection | Outer/inner size-class combinations and use as layout inputs. [TT-111461] |
| `window?.windowScene?.screen` | Recommended over `UIScreen.main` when screen access is unavoidable. [TT-111461] |
| `ConcentricRectangle`, `UICornerConfiguration` | iOS 26 concentricity APIs stated to support Duo screen shapes. [TT-111461] |
| `NavigationSplitView`, `UISplitViewController`, `TabView`, `UITabBarController` | Stated to adapt across Duo poses/configurations. [TT-111461] |
| Toolbar cancellation placement and UIKit back-item grouping | Ordering guidance shown. [TT-111462] |
| Badge APIs | iOS 26 APIs recommended for symbol-compatible count representation. [TT-111462] |
| `AVCaptureVideoPreviewLayer.videoGravity` | Recommended for preview composition. [TT-111465] |
| Camera rotation coordinator | Recommended for cross-display upright preview/capture; exact type not named in transcript. [TT-111465] |

## Safe code-use rule

When code must include an entry from this ledger, annotate the result in prose as transcript-derived and unverified against the iOS 27.1 API reference. Do not fabricate a compile-ready wrapper to hide missing declarations. After Apple documentation is available, follow the repository's `API_REFERENCE_ROADMAP.md` and update the status before removing that caveat.
