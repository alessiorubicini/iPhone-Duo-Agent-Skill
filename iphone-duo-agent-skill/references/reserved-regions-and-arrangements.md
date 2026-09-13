# Reserved Regions, Displacement, and Arrangements

Use this reference after the app is already freely resizable. It selects the smallest intervention that keeps important content visible and reachable around folds, cameras, and system-managed regions.

All iOS 27.1 symbols in this file are transcript-derived and **Documentation pending**. Consult `api-status.md` before generating code.

## Choose the mechanism

| Need | Mechanism | Reason |
|---|---|---|
| Lists, feeds, articles, documents naturally scroll | Natural flow/scrolling | Displacement would interrupt continuity |
| Standard navigation, bars, sheets, alerts, menus, popovers | System component | Apple supplies adaptation and fold avoidance |
| One custom element has a clear destination region | Local displacement | Smallest scope; preserves surrounding layout |
| Related custom elements must retain context | Group displacement | Moves source and dependent UI together |
| Two peers/main-detail views must both remain unobscured | Split arrangement | Side-by-side or stacked division with no foreground overlap |
| Clear foreground/background relationship; background may be partially covered | Overlay arrangement | Maintains layered relationship and can separate around a fold |
| Custom bar or edge-to-edge control needs precise avoidance | Reserved-region query | Uses actual region frames rather than guessed hinge/camera metrics |
| Hinge angle should drive an effect or interaction | Hinge observation | Read `displays-scenes-and-hinge.md`; do not use it to recreate region layout |

## Displacement rules

Displacement changes the frame of existing elements according to available space; it does not create a separate pose-only experience. [TT-111463]

1. Move only what cannot remain usable in place.
2. If elements can adapt independently, displace them independently.
3. If elements express one relationship, move them together. Example: keep a selected photo and its context menu aligned around the fold rather than separating them across a region. [TT-111463]
4. Limit travel; large movement weakens the visual relationship to the source.
5. Pick the destination by purpose:
   - book-like fold: contextual overlays may favor the trailing region, which is closer to continuation on the outer display;
   - tabletop posture: visibility-at-distance content may favor the upper region, while touch controls favor the stable lower region;
   - keyboard/search: keep contextual UI with the view or input it affects. [TT-111463]
6. Preserve all controls and hierarchy. A region changes placement, not feature availability. [TT-111463, TT-111466]

### Do not displace continuous content

Articles, feeds, documents, lists, and other continuous scrolling experiences should keep flowing through the scroll container. Moving the entire stream between regions breaks reading/scroll continuity. [TT-111463]

## Reserved-region model

Apple describes two kinds: [TT-111463]

- **Division:** splits a larger area into smaller usable regions. The Duo fold is represented as a division region. It is active while folded; when flat, its inactive representation has zero width.
- **Occlusion:** covers a smaller frame without dividing the full area. The FaceTime camera is active while the camera is active and inactive otherwise in the talk's Duo example.

By default the shown queries return active regions. The talk shows `.includeInactive` when high-level design decisions need region presence even while inactive—for example, preferring an even grid column count when a division region exists. Do not infer other options or region kinds.

SwiftUI obtains the geometry proxy from `GeometryReader` or `onGeometryChange` according to the talk. Only the `GeometryReader` query shape is shown; do not invent the `onGeometryChange` overload. [TT-111463]

### Transcript-shown queries

```swift
// SwiftUI — shown in TT-111463
GeometryReader { proxy in
    let regions = proxy.reservedRegions(kind: .division)
}
```

```swift
// SwiftUI — include inactive regions
GeometryReader { proxy in
    let regions = proxy.reservedRegions(
        kind: .division,
        options: .includeInactive
    )

    let frames = regions.map(\.frame)
    // ...
}
```

```swift
// UIKit — shown in TT-111463
let regions = view.reservedRegions(kind: .division)
let frames = regions.map(\.frame)
```

The transcripts do not establish complete signatures, coordinate-space rules, type declarations, update delivery, or option combinations. Keep that missing detail explicit.

## Arrangement model

An arrangement maps inputs—such as size classes, aspect ratio, and active division regions—to primary/secondary view placement and visibility. Apple provides split and overlay arrangements in iOS 27.1. [TT-111463]

### Split versus overlay

| Question | Split | Overlay |
|---|---|---|
| Relationship | Main-detail or peer content | Foreground-background |
| May one view obscure another? | No; both need usable space | Yes; background can remain usable through scrolling or context |
| Existing analogue | `HStack`/`VStack`-like split | `ZStack`-like layering |
| Duo fold adaptation shown | Views occupy separate regions when appropriate | Views may move from layering to side-by-side regions |

Do not select an arrangement merely because the device folds. Select it because the same two-view relationship exists across supported devices.

If the split style is constrained to an axis it cannot use along the current primary axis, Apple shows the arrangement selecting only one view—the primary view in its example. Preserve a meaningful primary view and do not infer additional fallback controls. [TT-111463]

### SwiftUI transcript patterns

```swift
ArrangementView {
    PlayerView()
} secondary: {
    UpNextView()
}
.arrangementViewStyle(.split)
```

To request the talk's horizontal-only split preference:

```swift
.arrangementViewStyle(
    .split.axes(.horizontal)
)
```

UIKit transcript pattern:

```swift
let arrangementVC = UIArrangementViewController()
let navController = UINavigationController(rootViewController: arrangementVC)

arrangementVC.setViewController(PlayerViewController(), for: .primary)
arrangementVC.setViewController(UpNextViewController(), for: .secondary)
arrangementVC.updateArrangement(.split.axes(.horizontal))
```

The talk's overlay example adapts a view's density from its placement, using the environment's reported z-index rather than hinge-angle thresholds:

```swift
@Environment(\.overlayArrangementZIndex)
private var zIndex: Int

var minimization: UpNextMinimization {
    zIndex > 0 ? .collapsed : .expanded
}
```

UIKit reads corresponding placement state in the shown pattern:

```swift
let primaryState = arrangementVC.state(for: .primary)
myModel.minimization = (primaryState?.zIndex ?? 0) > 0
    ? .collapsed
    : .expanded
```

These examples do not establish the declarations or full state lifecycle.

Apple states that when the split cannot use its configured axis and that axis conflicts with the primary aspect axis, the arrangement can choose a single view; the shown example retains the primary player in a tall layout. Do not generalize this into a complete fallback contract until documentation is published. [TT-111463]

Overlay views can inspect the transcript-shown environment value to adapt their internal representation:

```swift
@Environment(\.overlayArrangementZIndex)
private var zIndex: Int

private var minimization: UpNextMinimization {
    zIndex > 0 ? .collapsed : .expanded
}
```

Use placement state to adapt representation, not to remove capability.

### UIKit transcript patterns

```swift
let arrangementVC = UIArrangementViewController()

arrangementVC.setViewController(playerVC, for: .primary)
arrangementVC.setViewController(upNextVC, for: .secondary)
arrangementVC.updateArrangement(.split.axes(.horizontal))
```

The overlay example reads placement state:

```swift
let primaryState = arrangementVC.state(for: .primary)
myModel.minimization = (primaryState?.zIndex ?? 0) > 0
    ? .collapsed
    : .expanded
```

These snippets are not a substitute for the unpublished UIKit declarations.

## Containment rules

- Arrangements do not provide navigation infrastructure. Do not place `NavigationSplitView` or equivalent navigation containers inside an arrangement. [TT-111463]
- Do not place an arrangement inside `List`, `ScrollView`, or equivalent continuous-content containers. [TT-111463]
- Place navigation outside the arrangement when both are required, as shown by an `ArrangementView` inside a `NavigationStack`.
- Keep scrolling responsibility inside the appropriate primary or secondary child, not around the arrangement.

## Custom-layout review

- [ ] Standard component or natural flow rejected for a specific reason
- [ ] Displacement scope no larger than necessary
- [ ] Related source/context elements remain spatially associated
- [ ] Continuous scrolling content not displaced
- [ ] Destination region chosen by content purpose and reachability
- [ ] Inactive regions queried only for a stable high-level design decision
- [ ] Split chosen only when neither view may be obscured
- [ ] Overlay chosen only for a real foreground/background relationship
- [ ] No arrangement/scroll or arrangement/navigation containment violation
- [ ] No fabricated region dimensions, angle thresholds, or undocumented API declarations

## Related references

- Size-class and safe-area baseline: `adaptive-layouts.md`
- Hinge effects: `displays-scenes-and-hinge.md`
- New symbol evidence: `api-status.md`
- Pose/configuration tests: `testing-and-validation.md`
