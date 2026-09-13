# Adaptive Layouts

Use this reference to make a view freely resizable before adding fold-aware behavior. The baseline is an adaptive iPhone app, not a set of per-pose mockups.

## Decision sequence

1. **Remove device assumptions.** Search for model names, idiom-based layout selection, fixed screen dimensions, `UIScreen.main`, orientation switches, and symmetric-inset arithmetic.
2. **Describe the experience by available space.** Use horizontal/vertical size classes plus local container or scene geometry.
3. **Adopt system structure.** Prefer adaptive navigation, tab, toolbar, sheet, list, and scroll containers.
4. **Separate foreground from background.** Keep visible/interactive foreground content safe; let decorative or immersive backgrounds extend where intended.
5. **Test continuous resize.** Opening/closing, Split View, and Picture in Picture can resize a scene; the layout must not depend on a finite pose list. [TT-111461, TT-111466]
6. **Only then specialize.** Read `reserved-regions-and-arrangements.md` if a custom element cannot naturally flow or remain usable near the fold/camera.

## Environment model

Apple gives the following Duo size-class examples: [TT-111461]

| Configuration | Horizontal | Vertical | Design implication |
|---|---|---|---|
| Outer display, portrait | Compact | Regular | Single-column baseline; vertical room remains available |
| Outer display, landscape | Compact | Compact | Constrained in both dimensions; expect bar overflow and vertical competition |
| Inner display | Regular | Regular | More structure may be visible, such as sidebars or multiple content regions |

These combinations are examples, not a substitute for reading the live environment. Multitasking and system UI can change available geometry. Do not encode `outer` or `inner` as a derived Boolean from size classes.

Apple's shown access patterns are existing platform mechanisms: [TT-111461]

```swift
// SwiftUI
@Environment(\.horizontalSizeClass)
private var horizontalSizeClass

@Environment(\.verticalSizeClass)
private var verticalSizeClass

// UIKit
traitCollection.horizontalSizeClass
traitCollection.verticalSizeClass
```

### Orientation and idiom

- Do not select layouts by interface orientation or user-interface idiom. Apple explicitly directs Duo layouts to size classes instead. [TT-111461]
- The talk distinguishes inner-display orientation handling from ordinary iPhone behavior. Do not reconstruct those rules; respond to actual size classes and geometry.
- Supporting landscape remains important because hands-free/tent use is plausible, but landscape must not become a device-detection signal. [TT-111461]

### Screen access

Avoid screen objects when local environment, trait, or scene bounds answer the question. When screen access is unavoidable, resolve it from the window scene: [TT-111461]

```swift
let screen = window?.windowScene?.screen
```

Do not use `UIScreen.main`: on a multi-display device, `main` is ambiguous, and Apple says that API will be deprecated in a future release. [TT-111461]

## Layout strategies by content

| Content relationship | Preferred baseline |
|---|---|
| One reading/task flow | Fluid single column; allow margins and line length to adapt |
| Stable hierarchy with more horizontal space | Same hierarchy presented through an adaptive split view |
| Existing vertical stack that benefits from width | Rearrange into multiple columns at an environment-driven threshold |
| Information-dense tab destinations | Consider a system sidebar placement in regular width |
| Immersive non-scrolling visual | Full-display centering may be valid if no interactive element is obscured |
| Full-bleed visual plus controls/content | Full-width background; safe-area-aligned scrollable foreground |

The inner display is not permission to scale every compact-width view proportionally. Use the extra width to expose useful structure without changing capability or hierarchy. [TT-111466]

## Safe areas and margins

### Foreground rule

- SwiftUI content is safe-area constrained by default; retain that behavior for interactive and essential visible elements.
- UIKit manual layout should use `safeAreaInsets` or the safe-area layout guide.
- Layout margins may also be asymmetric; use the actual leading/trailing values rather than mirroring one side. [TT-111461]

Apple's UIKit example contrasts unsafe symmetry with per-edge calculation: [TT-111461]

```swift
// Avoid: assumes equal left and right insets
let width = view.bounds.width - view.safeAreaInsets.left * 2

// Use: accounts for every edge independently
let width = view.bounds.inset(by: view.safeAreaInsets).width
```

### Background rule

Background artwork may use the full bounds and extend behind system chrome when the design calls for it: [TT-111461]

```swift
// SwiftUI
.ignoresSafeArea()

// UIKit
backgroundView.frame = view.bounds
```

Do not apply `ignoresSafeArea()` to a container that also owns interactive content unless descendants are independently kept reachable and visible.

### Centering choices

- **Safe-area centered:** default for scrolling and interactive foreground content; automatically accounts for side controls.
- **Display centered:** acceptable for immersive, highly visual, non-scrolling content only after proving controls cannot obscure interaction.
- **Mixed:** full-width background/header plus inset foreground. Every interactive element belongs to the inset layer. [TT-111466]

## Screen-shape treatment

The talks recommend iOS 26 concentricity APIs for shapes that should follow screen corners: `ConcentricRectangle` in SwiftUI and `UICornerConfiguration` in UIKit. Apple states they are updated for Duo screen shapes. [TT-111461]

Transcript example:

```swift
ConcentricRectangle()
    .fill(Color.green)
    .padding(8.0)
    .ignoresSafeArea()
```

Use this as design guidance, not evidence for undocumented iOS 27.1 declarations. Do not hard-code corner radii from screenshots or presumed hardware metrics.

## SDK opt-in boundary

Apple describes progressively different presentation depending on SDK adoption: existing apps run; iOS 27 work for iPhone resizing improves inner-display use; rebuilding with iOS 27.1 opts into edge-to-edge screen use and new bar behavior. [TT-111461, TT-111462]

Do not convert this statement into guessed availability checks. Confirm the actual deployment/build behavior using the released Xcode 27.1 SDK and current Apple documentation.

`UIRequiresFullScreen` is not an escape from resizability. Apple says Duo continues to honor the key, but the app still resizes when the device opens or closes and may be scaled on the inner display, including in Split View. Remove layout assumptions even when the product retains full-screen requirements. [TT-111461]

The Xcode 27.1 App Resizability skill is Apple's suggested automated audit entry point for SwiftUI and UIKit. Treat its results as static findings to review, not proof of runtime correctness. The talk's migration example replaces global screen scale with the current trait environment: [TT-111461]

```swift
func updateThumbnail(from image: UIImage) {
    // Avoid
    let screenScale = UIScreen.main.scale

    // Prefer the current environment
    let screenScale = traitCollection.displayScale
    // ...
}
```

## Audit checklist

- [ ] No layout branch based on `UIDevice`, model string, assumed outer/inner dimensions, or idiom
- [ ] No `UIScreen.main`; any screen query comes from the owning scene
- [ ] Horizontal and vertical size classes read independently
- [ ] Local geometry drives continuous reflow; no finite pose-size table
- [ ] Safe-area and layout-margin edges handled independently
- [ ] Interactive content remains safe; full-bleed treatment is limited to intentional background/visual layers
- [ ] Regular width exposes useful structure without changing navigation hierarchy
- [ ] Compact height remains functional when bars, keyboard, or Picture in Picture compete for space
- [ ] Landscape is supported where product constraints allow it
- [ ] Custom fold behavior justified only after the adaptive baseline succeeds

## Related references

- Fold/camera-aware custom layout: `reserved-regions-and-arrangements.md`
- System navigation and vertical bars: `navigation-bars-and-presentations.md`
- Scene/configuration model: `displays-scenes-and-hinge.md`
- Test matrix: `testing-and-validation.md`
