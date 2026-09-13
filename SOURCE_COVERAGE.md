# Apple Tech Talk Coverage

This matrix verifies that every checked-in Apple iPhone Duo Tech Talk contributes operational knowledge to the skill. Talk IDs are canonicalized in [`source-map.md`](iphone-duo-agent-skill/references/source-map.md).

| Source | Operational knowledge represented | Primary references |
|---|---|---|
| TT-111461 — Prepare your app for iPhone Duo | SDK opt-in boundary; outer/inner size-class behavior; orientation warning; scene-local screen access; concentricity; adaptive navigation/tabs/sheets; safe-area asymmetry; Device Hub and Split View testing; App Resizability skill | `adaptive-layouts.md`, `navigation-bars-and-presentations.md`, `testing-and-validation.md`, `api-status.md` |
| TT-111462 — Raise the Bar with iPhone Duo | Conditions for system-managed vertical bars; container/column rules; ordering and semantic placements; item representation; axis adaptation; accessibility transparency; compression, overflow, and visibility priorities; opt-out cases | `navigation-bars-and-presentations.md`, `continuity-and-accessibility.md`, `api-status.md` |
| TT-111463 — Strike a pose with adaptive layouts on iPhone Duo | Reserved-region model; displacement heuristics; continuous-content exception; active/inactive division and occlusion regions; arrangements; split/overlay selection; containment exclusions | `reserved-regions-and-arrangements.md`, `adaptive-layouts.md`, `api-status.md` |
| TT-111464 — Leverage multiple displays and scenes on iPhone Duo | Discrete/continuous hinge input; hinge for interactions rather than layout; multitasking; multi-instance availability; scene activation error handling; scene accessories; camera capture accessory availability | `displays-scenes-and-hinge.md`, `continuity-and-accessibility.md`, `testing-and-validation.md`, `api-status.md` |
| TT-111465 — Build a great camera experience for iPhone Duo | Virtual and individual front-camera tradeoffs; relative camera direction per view; descriptor handoff; camera reconfiguration/mirroring; preview gravity and aspect ratio; rotation; camera sensor compensation; dual-display camera UI | `camera-experiences.md`, `displays-scenes-and-hinge.md`, `testing-and-validation.md`, `api-status.md` |
| TT-111466 — Design for iPhone Duo | Outer/inner and partially folded design principles; vertical control placement; 50/50 Split View; Picture in Picture resizing; stable capability/hierarchy; tabletop reachability; safe-area alignment; system fold avoidance | `adaptive-layouts.md`, `navigation-bars-and-presentations.md`, `continuity-and-accessibility.md`, `testing-and-validation.md` |

## Cross-cutting requirement coverage

| Requirement | Coverage |
|---|---|
| Adaptive layouts | `adaptive-layouts.md`; `reserved-regions-and-arrangements.md` |
| Displays and configurations | `displays-scenes-and-hinge.md`; `testing-and-validation.md`; `glossary.md` |
| Hinge and pose awareness | `displays-scenes-and-hinge.md`; `reserved-regions-and-arrangements.md` |
| Reserved regions | `reserved-regions-and-arrangements.md`; `api-status.md` |
| Navigation and arrangements | `navigation-bars-and-presentations.md`; `reserved-regions-and-arrangements.md` |
| SwiftUI/UIKit behavior | Paired framework tables and examples in each implementation reference |
| Continuity | `continuity-and-accessibility.md`; `displays-scenes-and-hinge.md` |
| Accessibility | `continuity-and-accessibility.md`; `testing-and-validation.md` |
| Testing | `testing-and-validation.md` |
| Duo-specific APIs | `api-status.md`, with detailed use in owning task references |
| Camera | `camera-experiences.md` |

## Audit status

- Six of six talks represented
- References organized by developer task, not talk sequence
- Every new iOS 27.1 symbol isolated in `api-status.md`
- No future API declaration file pre-populated with inferred content
- API documentation integration supported by additive evidence/status fields and stable task-oriented references
