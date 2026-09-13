# Reference Index

Select references by developer task. `SKILL.md` carries the shared invariants; these files own the detail.

| File | Read when |
|---|---|
| [`adaptive-layouts.md`](adaptive-layouts.md) | Choosing responsive structure; auditing fixed dimensions, size classes, safe areas, margins, or background/foreground treatment |
| [`reserved-regions-and-arrangements.md`](reserved-regions-and-arrangements.md) | Avoiding the fold/cameras in custom UI; deciding natural flow vs displacement vs split/overlay arrangement |
| [`navigation-bars-and-presentations.md`](navigation-bars-and-presentations.md) | Implementing navigation, tabs, toolbars, sheets, vertical-axis item representations, compression, or overflow |
| [`displays-scenes-and-hinge.md`](displays-scenes-and-hinge.md) | Reasoning about outer/inner displays, Split View, multiple scenes, scene activation, hinge effects, or scene accessories |
| [`camera-experiences.md`](camera-experiences.md) | Selecting front cameras; handling display-relative direction, session changes, preview composition, or rotation |
| [`continuity-and-accessibility.md`](continuity-and-accessibility.md) | Preserving state/capability/hierarchy and validating reachability, semantics, transparency, and assistive use |
| [`testing-and-validation.md`](testing-and-validation.md) | Building a Device Hub test matrix or reporting compile, runtime, transition, camera, and accessibility evidence |
| [`api-status.md`](api-status.md) | Writing or reviewing any Duo-specific iOS 27.1 code; checking what Apple showed versus what remains undocumented |
| [`source-map.md`](source-map.md) | Resolving TT IDs, source paths, official URLs, or claim traceability |
| [`glossary.md`](glossary.md) | Normalizing Duo terms and avoiding ambiguous display/pose language |

## Fast routes

- Existing app readiness audit: `adaptive-layouts.md` → `navigation-bars-and-presentations.md` → `testing-and-validation.md`
- Custom fold-aware layout: `reserved-regions-and-arrangements.md` → `api-status.md`
- Multi-display camera feature: `camera-experiences.md` → `displays-scenes-and-hinge.md` → `testing-and-validation.md` → `api-status.md`
- Accessibility or continuity regression: `continuity-and-accessibility.md` plus the relevant layout/navigation reference
