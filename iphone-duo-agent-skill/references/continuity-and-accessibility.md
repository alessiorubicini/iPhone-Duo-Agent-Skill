# Continuity and Accessibility

iPhone Duo should feel like one app adapting around the person, not separate outer, inner, and folded products. Presentation may change; content, capability, hierarchy, state, semantics, and recovery must remain coherent. [TT-111463, TT-111466]

## Continuity invariants

### Capability parity

- Every action and destination remains available across supported displays and poses.
- A tabletop layout may reposition media and controls, but it keeps the same controls and general hierarchy. [TT-111466]
- A regular-width layout may expose sidebar/detail simultaneously, but must not introduce a different information architecture.
- Overflow is an alternate representation of existing actions, not a place for pose-only commands.

### Task continuity

Opening, closing, rotating, folding, entering Split View, or receiving a pinned Picture in Picture surface can resize or relocate UI. The active task should survive: selection, scroll intent, draft, playback/capture intent, and recoverable presentation state should not reset solely because geometry changed.

This is an implementation heuristic grounded in Apple's predictable inside/outside experience requirement, not a claimed iOS 27.1 state-restoration API. [TT-111466]

Prefer state ownership that survives view recomposition:

- Domain/task state above pose-specific layout branches
- Scene-specific navigation and focus scoped per scene
- Geometry, safe areas, active regions, and bar axis treated as derived presentation inputs

Avoid duplicating independent models in compact and regular branches unless explicit synchronization is part of the design.

### Context preservation

- Move a contextual overlay with its source when displacing both preserves meaning. [TT-111463]
- When search is focused, keep it associated with the searched view/keyboard across fold adaptation. [TT-111463]
- If an arrangement changes which view overlays another, use the arrangement's reported placement state to adjust density—not to change actions or data.
- If a scene accessory disappears, preserve the user's underlying task and reflect unavailability in the initiating control. [TT-111464]

## Reachability and target placement

Apple's design rationale moves controls to side regions or the stable lower half in certain poses to improve reach and targeting. Interactive elements should remain within safe areas or be explicitly placed using reserved-region information. [TT-111461, TT-111463, TT-111466]

Rules:

1. Keep primary controls away from active fold/camera regions.
2. In a tabletop posture, favor the stable lower region for repeated touch controls and upper region for glanceable/distance content.
3. In book-like folds, avoid leaving a button centered on the curve.
4. Preserve logical reading and focus order when visual position changes.
5. Avoid large displacement that disconnects a control from its content.

System sheets, alerts, menus, toolbar buttons, and other presentations receive Apple's fold-avoidance behavior; custom recreations must justify the accessibility burden. [TT-111466]

## Semantics across bar representations

Even when a toolbar item is displayed as a symbol, provide a meaningful title. Apple uses title plus image for overflow/expanded forms, while the title also supports understandable semantics. [TT-111462]

- Do not encode the action only in a custom icon.
- Keep the same action identity when switching between text, symbol, vertical, horizontal, and overflow representations.
- Use a badge for glanceable count/status where appropriate; do not bury status in a wide custom label solely to keep it visible.
- Prioritize frequent actions and important status so they remain visible longer during compression. [TT-111462]

## Visual accessibility

Apple states that a vertical bar receives a background when Reduced Transparency is enabled. Custom content must remain legible with and without that background. [TT-111462]

Established platform validation also applies:

- Dynamic Type at small and accessibility sizes
- Bold Text, Increase Contrast, Differentiate Without Color, and Reduce Motion where relevant
- VoiceOver names, traits, order, rotor behavior, and escape/dismissal for presentations
- Switch Control/Voice Control targetability
- Sufficient touch targets and no occlusion at extreme safe-area configurations

These are general Apple-platform checks, not new Duo-specific behaviors stated by the talks. Apply them because Duo reflow, vertical bars, displacement, and overflow create additional places for existing accessibility failures to surface.

## Motion and hinge effects

A hinge-driven effect is enhancement, not required feedback.

- Provide an equivalent non-hinge path on devices/scenes without hinge data.
- Reset the effect when hinge data disappears or leaves the applicable state, following Apple's shown pattern. [TT-111464]
- Respect reduced-motion preferences using established platform behavior.
- Do not couple completion of a task to reaching an angle threshold.

## Multi-scene and dual-display accessibility

- Give each scene/accessory a complete, coherent semantic subtree.
- Do not move focus to a second display merely because supplementary UI appears.
- Keep user-enabled and system-available accessory states distinguishable.
- Avoid duplicating an action on both displays with conflicting enabled/state values.
- Announce or otherwise expose meaningful state transitions using established accessibility mechanisms when the product already does so; do not invent Duo-specific announcements.

## Audit questions

- Does compact/regular switching preserve the same destinations and actions?
- Can a user continue the active task after opening, closing, rotating, or entering Split View?
- Does any layout branch instantiate a fresh source of truth?
- Are controls safe and reachable on either side of asymmetric insets?
- Do displaced controls retain context, focus order, and labels?
- Can every toolbar action be understood in symbol, text, and overflow form?
- Is custom bar content legible with Reduced Transparency?
- Are hinge effects optional and motion-sensitive?
- If supplementary UI vanishes, does the main scene remain usable and truthful?

## Related references

- State layers and accessory availability: `displays-scenes-and-hinge.md`
- Bar semantics and overflow: `navigation-bars-and-presentations.md`
- Fold-aware displacement: `reserved-regions-and-arrangements.md`
- Accessibility/configuration matrix: `testing-and-validation.md`
