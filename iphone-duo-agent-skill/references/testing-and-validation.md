# Testing and Validation

Validation must cover continuous transitions, not only representative screenshots. Use Device Hub with the iPhone Duo simulator as described by Apple, and keep build/static evidence separate from observed runtime behavior. [TT-111461]

## Evidence levels

Report each level independently:

1. **Static review:** code paths, container ownership, state lifetime, constraints, API spellings, and unsupported assumptions inspected.
2. **Build/type-check:** target compiled against the selected SDK. This does not prove pose behavior.
3. **Runtime configuration:** a named display/orientation/multitasking state launched and inspected.
4. **Transition:** the app observed while opening, closing, rotating, folding, resizing, moving between displays, or changing accessory/camera availability.
5. **Accessibility:** assistive setting/technology tested in named configurations.
6. **Camera:** capture session, direction, mirroring, aspect ratio, rotation, and accessory behavior exercised on supported simulator/device capability.

Never summarize a build as “tested on iPhone Duo.” State exactly which levels were completed.

## Minimum configuration matrix

Select rows relevant to the feature. “Not applicable” requires a reason.

| Configuration | Primary risks |
|---|---|
| Outer portrait | Wider/shorter compact-width composition; side controls; asymmetric insets |
| Outer landscape | Compact width and height; severe vertical-bar overflow; safe-area side changes |
| Inner landscape, flat | Regular-width information density; side controls; over-stretched compact layout |
| Inner portrait, flat | Regular-width layout with horizontal bars; hierarchy parity |
| Partially folded, book-like | Division region; readability through curve; displacement; contextual continuity |
| Partially folded, tabletop | Upper visibility/lower reachability; stable control targets |
| Split View, app on left | Vertical controls can occupy left outer edge; asymmetric margins/insets |
| Split View, app on right | Mirrored content constraints without assuming hardware bar mirroring |
| Pinned Picture in Picture | Continuous vertical resize; toolbar/tab compression |
| Keyboard visible | Reduced vertical bar capacity; search/input context; accessory-bar ownership |
| Camera/occlusion active | Active occlusion region; viewfinder/control visibility |
| Scene accessory available/unavailable | Toggle truthfulness; supplementary UI lifetime; main-scene continuity |
| Multiple app scenes | Independent navigation/focus; shared document/domain state correctness |

Apple instructs developers to use Device Hub controls to open, close, rotate, and fold the Duo simulator. For Split View, begin on the inner display and drag the app by the home indicator to each side. [TT-111461]

## Transition tests

Test state during the transition, not only before and after:

- Start an active task, then open and close the device.
- Rotate in each display context supported by the app.
- Move between flat and partially folded states while scrolling and while a contextual presentation is open.
- Enter/exit Split View on both sides.
- Present/dismiss keyboard and Picture in Picture while bars are near capacity.
- Activate/deactivate the relevant camera occlusion.
- Enable/disable a scene accessory, then cause system availability to change.
- For camera apps, change display relationship while preview/capture state is configured.

Watch for duplicate state, lost selection/draft, jumpy or separated contextual UI, inaccessible controls, transient overlap, stale overflow, wrong focus, and incorrect camera direction/mirroring.

## Layout assertions

- Foreground controls remain within safe or explicitly reserved-region-aware placement.
- Full-bleed background remains continuous without dragging interactive descendants outside safe placement.
- Opposite insets are measured independently.
- Continuous scrolling content does not jump between regions.
- Related displaced elements preserve proximity and relationship.
- Split arrangements keep both views unobscured; overlay arrangements preserve the intended foreground/background relationship.
- No pose reveals a feature unavailable elsewhere.
- Large regular-width layout adds useful structure instead of blank stretching.

## Navigation and bar assertions

- System containers own the bars.
- Horizontal and vertical forms retain action identity, order, title, and enabled state.
- Custom views fit the vertical fixed-width form or intentionally remain horizontal.
- Primary actions/status remain visible according to assigned priorities.
- Overflow contains the correct actions in stable semantic groups.
- Ellipsis represents overflow only.
- RTL content adaptation does not manually move the hardware-aligned vertical bar.
- Sheets and other presentations avoid the fold without losing dismissal/action controls.

## Accessibility matrix

At minimum, repeat critical compact and regular configurations with:

- Largest supported Dynamic Type/accessibility text sizes
- Reduced Transparency (especially vertical bars/custom items)
- VoiceOver traversal through reflowed content, presentations, and overflow
- Switch Control or Voice Control for displaced/tabletop controls when relevant
- Reduce Motion for hinge-driven effects
- Right-to-left localization for safe-area content and bar/item ordering

General accessibility settings are established platform validation, not new Duo behavior. The Duo-specific risk is the interaction between those settings and reflow, fold avoidance, vertical bars, and multi-display state.

## Camera matrix

For camera features, record the selected strategy and verify:

- Virtual Front Camera switches while preserving common-format operation, if selected
- Individual physical cameras reselect/reconfigure on direction changes
- Direction result is relative to each visible view
- Preview mirroring follows actual direction, including rear camera facing the person
- Preview gravity/aspect ratio avoids distortion and leaves controls usable
- Preview and capture remain upright across rotation and display movement
- Camera occlusion does not hide essential controls/content
- Camera capture accessory appears only under supported system conditions and its toggle disables when unavailable
- Failure/reconfiguration states are visible and recoverable using the app's existing error model

The simulator may not validate every physical camera capability. State any hardware-only gap explicitly.

## API verification gate

Before calling transcript-only iOS 27.1 code production-ready:

- [ ] Compile against the released iOS 27.1 SDK
- [ ] Compare every symbol with current Apple Developer Documentation
- [ ] Confirm module imports and availability annotations
- [ ] Confirm callback/isolation and error semantics
- [ ] Replace transcript ellipses with app-specific code, not guessed framework code
- [ ] Update `api-status.md` with documentation URL and verification date

Until those steps are possible, label the code **Documentation pending** even if it closely follows a Tech Talk snippet.

## Reporting template

```text
Static review: passed/failed — scope
Build: passed/failed/not run — SDK, destination, command
Runtime configurations: observed/not run — exact matrix rows
Transitions: observed/not run — exact transitions
Accessibility: observed/not run — settings and rows
Camera: observed/not run/not applicable — simulator/device limits
API documentation: verified/pending — symbols and sources
Remaining risk: bounded list
```

## Related references

- Adaptive assertions: `adaptive-layouts.md`
- Fold/arrangement assertions: `reserved-regions-and-arrangements.md`
- Bar assertions: `navigation-bars-and-presentations.md`
- Scene/hinge/accessory assertions: `displays-scenes-and-hinge.md`
- Camera assertions: `camera-experiences.md`
