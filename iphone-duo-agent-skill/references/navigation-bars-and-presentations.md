# Navigation, Bars, and Presentations

Use system-owned navigation and presentation containers so controls can move between horizontal and vertical arrangements, avoid the fold, and enter overflow without a second navigation model.

New iOS 27.1 names below are transcript-derived and **Documentation pending**. See `api-status.md`.

## Adoption order

1. Build with the iOS 27.1 SDK to opt into the new bar behavior described by Apple; verify actual availability in the released SDK. [TT-111461, TT-111462]
2. Put SwiftUI toolbar content in `NavigationStack`/`NavigationSplitView`, or use UIKit `UINavigationController`/`UITabBarController`.
3. Preserve semantic placements, groups, image, title, and badge; let the system select representation and axis.
4. Audit custom views for fixed-width vertical-bar compatibility.
5. Set compression and visibility priorities only from product importance.
6. Disable vertical bars only when the content case matches Apple's narrow exceptions.

## Why container ownership matters

Apple's vertical layout considers content owned by system navigation containers. A standalone custom `UIToolbar`, `UINavigationBar`, or `UITabBar` used to construct bespoke chrome does not participate as navigation-controller/tab-controller content. [TT-111462]

```swift
NavigationStack {
    ContentView()
        .toolbar {
            ToolbarItem(placement: .bottomBar) {
                // Existing action
            }
        }
}
```

For UIKit, set toolbar/navigation items on a view controller embedded in `UINavigationController`; do not replace that structure with an independently managed `UIToolbar` merely to control placement.

## Configuration behavior to design for

Apple describes side-positioned controls on the outer display and inner landscape, while inner portrait retains horizontal bars. The side region can contain navigation, toolbar, tab, status, Dynamic Island/Live Activity content, with overflow when vertical room is insufficient. [TT-111462, TT-111466]

Do not manually choose the bar axis from an assumed pose. Supply adaptable item content and respond only when a custom view genuinely needs the environment/trait.

### Container and presentation rules

- In split views, only an edge-positioned detail column participates in the vertical bar; other columns keep horizontal items. [TT-111462]
- An expanded inspector does not receive an additional vertical bar when the detail column already has one. [TT-111462]
- Outer-display sheets with toolbars can use vertical bars; inner-display centered sheets use horizontal bars by default. [TT-111462]
- Apple states that a left-positioned sheet lacks a vertical bar while a right-positioned one receives it when placement is customized. Exact placement API syntax is not shown. [TT-111462]
- The hardware-aligned bar remains on the same physical side in right-to-left languages; content adapts around it. Do not mirror the bar manually. [TT-111462]
- Sheets, alerts, menus, toolbar buttons, and other system components receive fold avoidance. Prefer them over custom equivalents. [TT-111466]

### Tab bar versus sidebar

System tab containers remain available across poses. For an information-dense regular-width experience, Apple shows opting the tab presentation into a sidebar; this changes presentation without changing destinations. [TT-111461, TT-111466]

```swift
// SwiftUI
TabView { /* destinations */ }
    .defaultTabBarPlacement(.sidebar)

// UIKit
tabBarController.sidebar.preferredPlacement = .sidebar
```

Do not infer automatic selection rules or availability from the snippets. Use the sidebar only when the information architecture benefits from it, not merely because regular width is available.

## Order and semantic placement

Model a vertical bar as the existing hierarchy rotated into a top-to-bottom arrangement, not as an independent menu.

1. Primary navigation control: system back, close, or cancellation.
2. Prominent completion/action control.
3. Remaining groups, preserving their semantic top/bottom associations.
4. Tab destinations remain bottom-aligned. [TT-111462]

SwiftUI cancellation placement shown by Apple:

```swift
.toolbar {
    ToolbarItem(placement: .cancellationAction) {
        // Close or cancel
    }
}
```

UIKit custom leading items should not supplement the automatic back button when they replace that role:

```swift
navigationItem.leftItemsSupplementBackButton = false
navigationItem.leadingItemGroups = [UIBarButtonItemGroup(...)]
```

Prominent trailing placements shown in the talk:

```swift
// SwiftUI
ToolbarItem(placement: .topBarPinnedTrailing) {
    // Prominent action
}

// UIKit
navigationItem.pinnedTrailingGroup = UIBarButtonItemGroup(...)
```

Do not infer the full placement or group APIs from these excerpts.

## Item representation and axis

Vertical bars have fixed width and flexible height; symbol-oriented items adapt better than long text or wide custom views. Horizontal bars have the opposite sizing character. [TT-111462]

Provide both a meaningful image/symbol and title where the action supports them:

- Visible bar form can prefer the symbol.
- Overflow or expanded form can use title plus image.
- The title remains accessibility and contextual information even when not visible.

Text-only items and complex custom views remain horizontal by default in Apple's described behavior. Do not force a control vertical solely to increase bar density.

### Axis behavior decision

| Item | Choice from talk |
|---|---|
| Transitions between symbol and text (for example custom Select/Done) | Keep related representations together with horizontal-only behavior |
| Custom view with a deliberate fixed-width vertical representation | Allow vertical-preferred behavior |
| Text conveys standalone information (for example a price) | Keep horizontal |
| Text only repeats a recognizable symbol | Prefer symbol; keep title metadata |
| Count/status | Consider a system badge rather than inline text |

Transcript-shown API use:

```swift
ToolbarItem {
    SelectOrDoneButton()
}
.axisBehavior(.horizontalOnly)
```

```swift
let item = UIBarButtonItem(customView: ProfileView())
item.axisBehavior = .verticalPreferred
```

For custom representations, read vertical context only to adjust layout, not to fork functionality:

```swift
@Environment(\.toolbarVerticalEdge) private var edge

// UIKit
switch traitCollection.verticalBarEdge {
    // ...
}
```

The value is populated when items can participate on the vertical axis and nil/unspecified otherwise according to the talk. Exact value types remain undocumented here. [TT-111462]

### Spacing and visual treatment

- Do not introduce extra axis-specific spacer logic without a content need. Apple states flexible spacers have zero size vertically while fixed spacers retain minimum size. [TT-111462]
- Vertical bars have no scroll-edge effect by default in the talk's described design.
- Reduced Transparency causes the vertical bar to receive a background; validate custom item contrast and legibility in both states. [TT-111462]
- Keyboard accessory bars stay attached to the keyboard; do not move them into the side bar. [TT-111462]

## Compression and overflow

Outer landscape, keyboard presentation, and Picture in Picture can reduce vertical capacity. Design overflow as a dynamic condition, not one fixed device state. [TT-111462]

### Choose what compresses first

- Navigation-focused experience: keep tab destinations accessible; toolbar compresses first. Apple identifies this as the default.
- Task-focused experience: keep frequent actions visible; tab bar compresses first.

Transcript-shown preferences:

```swift
ContentView()
    .toolbarVerticalCompressionBehavior(.prefersToolbarItems)
```

```swift
navigationItem.verticalBarCompressionBehavior = .prefersBarItems
```

### Consolidate overflow

Use one system-managed overflow rather than nesting a bespoke overflow menu inside system overflow. The ellipsis is reserved for overflow; use distinct symbols for other menus. [TT-111462]

```swift
.toolbar {
    ToolbarOverflowMenu {
        Button("Scan") { /* ... */ }
        Button("Connect") { /* ... */ }
    }
}
```

```swift
navigationItem.additionalOverflowItems = UIDeferredMenuElement { provider in
    provider(self.persistentOverflowItems())
}
```

### Visibility priority

Apple states that default overflow proceeds bottom-to-top, while item priority can retain more important controls. Prioritize groups first, then individual items only if needed. Frequent actions and glanceable status/badges should remain visible longer. [TT-111462]

```swift
ToolbarItem {
    Button(/* ... */) { /* ... */ }
}
.visibilityPriority(.high)
```

Do not invent custom numeric priority syntax; the talk names high, low, and custom priorities but does not show the custom API.

## Opting out

Apple gives two narrow examples where disabling vertical behavior may be appropriate: a single-page bottom-heavy interface whose content needs the width, and a control-heavy sheet with only one bar item. [TT-111462, TT-111466]

```swift
NavigationStack {
    ContentView()
        .toolbarVerticalBehavior(.disabled)
}
```

```swift
final class MyViewController: UIViewController {
    override var preferredVerticalBarBehavior: UIVerticalBarBehavior {
        .disabled
    }
}
```

Do not disable vertical bars globally to avoid adapting custom items.

## Review checklist

- [ ] System navigation/tab controller owns bar content
- [ ] Same actions and destinations in horizontal and vertical configurations
- [ ] Semantic item ordering and grouping preserved
- [ ] Every symbol item also has a meaningful title
- [ ] Wide custom item has an intentional horizontal or vertical representation
- [ ] No manual RTL mirroring of the hardware-aligned vertical bar
- [ ] Compression choice reflects navigation versus task priority
- [ ] One system overflow; ellipsis reserved for overflow
- [ ] Frequent actions and glanceable status assigned higher retention priority where needed
- [ ] Reduced Transparency and constrained-height legibility tested
- [ ] Vertical behavior disabled only for a documented content rationale

## Related references

- Layout and safe-area baseline: `adaptive-layouts.md`
- Capability parity and accessibility: `continuity-and-accessibility.md`
- Pose/configuration tests: `testing-and-validation.md`
- API evidence status: `api-status.md`
