# AGENTS.md — iPhone Duo Agent Skill Author Guide

This file is the contribution contract for `iphone-duo-agent-skill`.

## Purpose

The skill gives coding agents operational knowledge for designing, auditing, implementing, and validating native iPhone Duo apps. It turns Apple's six iPhone Duo Tech Talks into task-oriented guidance while keeping undocumented iOS 27.1 API details quarantined for later verification.

## Source hierarchy

Use evidence in this order:

1. `sources/` — primary repository evidence: official Apple Tech Talk transcripts and extracted code.
2. Published Apple Developer Documentation for iOS 27.1 — add only after it is publicly accessible and record it in `iphone-duo-agent-skill/references/api-status.md`.
3. Established Apple-platform adaptive-layout practice — label it as general guidance, never as Duo-specific API behavior.

Never turn a talk's conceptual description into an API signature. Code tasks may reuse a transcript snippet, but must identify it as transcript-derived and require SDK verification until the corresponding API is documented.

## Content boundaries

### Covered

- Adaptive SwiftUI and UIKit layouts across outer/inner displays, resizing, multitasking, and poses
- Safe areas, asymmetric margins, concentric geometry, reserved regions, displacement, and arrangements
- Navigation containers, presentations, vertical bars, item representations, and overflow
- Display-local state, scene geometry, multiple scenes, hinge observation, and scene accessories
- Camera discovery, camera direction, preview composition, rotation, and dual-display capture experiences
- Continuity of state and capability across pose/display transitions
- Accessibility and pose-aware validation
- Transcript-backed iOS 27.1 Duo API inventory and documentation gaps

### Not covered

- General SwiftUI, UIKit, AVFoundation, or accessibility tutorials unrelated to iPhone Duo
- Unpublished API declarations, inferred availability annotations, concurrency contracts, defaults, edge cases, or compatibility behavior
- Hardware specifications or product behavior absent from the six checked-in Apple sources
- Private APIs, device detection, model-identifier branching, or hinge-driven layout when arrangement/region APIs are appropriate

## Correctness invariants

1. Start from standard adaptive Apple containers and environment/trait inputs; add Duo-specific logic only when content purpose requires it.
2. Preserve content, controls, hierarchy, and task state across displays and poses. A pose may change presentation, not capability.
3. Use size classes, local geometry, safe areas, layout margins, and scene-local screen data. Do not branch on device model, idiom, fixed display metrics, or `UIScreen.main`.
4. Treat opposite safe-area and margin edges independently.
5. Use arrangements and reserved regions for layout; use hinge observation for interactions/effects, not as a replacement layout engine.
6. Keep scrollable continuous content continuous; do not displace it merely because a division region becomes active.
7. Use system navigation, bars, presentations, and overflow before custom equivalents so fold avoidance and axis adaptation remain system-managed.
8. Never invent iOS 27.1 signatures or behavior. Mark all transcript-only APIs `Documentation pending` until verified against published Apple API documentation.
9. Separate static review/build evidence from Device Hub, runtime, accessibility, camera, and transition verification.
10. Every Duo-specific factual claim in a reference must cite at least one talk ID defined in `references/source-map.md`.

## Prohibited patterns

Do not recommend:

```swift
// Device- and dimension-specific branching
if UIDevice.current.model == "iPhone Duo" || width == 1536 { ... }
```

```swift
// Symmetric inset assumption
let width = view.bounds.width - view.safeAreaInsets.left * 2
```

```swift
// Hinge angle used as a hand-built layout breakpoint
.onHingeChange { _, context in
    isTwoColumn = context.hinge?.angle.degrees ?? 0 > 90
}
```

## Repository organization

- `iphone-duo-agent-skill/SKILL.md` — concise routing and core reasoning rules
- `iphone-duo-agent-skill/references/` — task-oriented operational guidance
- `sources/` — immutable primary evidence except when correcting extraction against Apple originals
- `.agents/skills/update-iphone-duo-apis/` — maintenance workflow for future Apple documentation
- `SOURCE_COVERAGE.md` — talk-to-reference coverage audit
- `API_REFERENCE_ROADMAP.md` — future iOS 27.1 documentation integration contract

## Writing and code conventions

- Use canonical terms from `references/glossary.md`.
- Distinguish **Requirement**, **Heuristic**, **Transcript API**, and **Documentation pending** where ambiguity could affect generated code.
- Prefer rules, decision tables, and small source-accurate examples over narrative summaries.
- Keep transcript excerpts faithful. Fix obvious transcript formatting only when meaning is unchanged; note any normalization.
- Avoid unsupported imports, deployment targets, availability checks, protocol conformances, or failure semantics.
- Link related references instead of copying detail.

## Adding or updating a reference

1. Select the developer task, not the originating talk, as the file boundary.
2. Add the file to `references/_index.md` and the router in `SKILL.md`.
3. Add talk IDs beside Duo-specific claims and update `SOURCE_COVERAGE.md`.
4. Add new iOS 27.1 symbols or documentation status changes to `references/api-status.md`.
5. Run the checks documented in `CONTRIBUTING.md`.

## Maintenance

When Apple publishes iOS 27.1 API documentation, use `.agents/skills/update-iphone-duo-apis/SKILL.md`. Documentation must strengthen the existing task-oriented references; it must not replace them with an API catalog or require structural redesign.
