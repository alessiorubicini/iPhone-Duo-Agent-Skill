---
name: iphone-duo-agent-skill
description: Design, implement, audit, and validate iPhone Duo behavior in native SwiftUI and UIKit apps. Use when work targets Duo adaptive layouts, folds or reserved regions, display or pose transitions, navigation, multiple scenes, hinge input, cameras, continuity, accessibility, or Device Hub testing. Do not use for general iOS development or standalone API-documentation maintenance.
---

# iPhone Duo Agent Skill

## Start

1. Classify the request and read only the matching references from the router below.
2. For Duo-specific code or API claims, also read [`references/api-status.md`](references/api-status.md).
3. Identify the current UI scene, available space, content relationship, and continuity requirement. Do not identify a device model or hard-code display metrics.
4. Establish the standard adaptive baseline: resizable layout, safe areas, size classes, navigation containers, bars, and presentations.
5. Add Duo-specific behavior only for a concrete content or interaction need:
   - reserved regions for custom fold/camera avoidance;
   - arrangements for a persistent two-view split or overlay relationship;
   - hinge observation for interactions or effects, not primary layout;
   - scene accessories for intentional multi-display supplementary UI;
   - camera direction coordination when individual physical-camera capability is required.
6. Preserve content, controls, hierarchy, and task state across poses. Change presentation, not capability.
7. Validate against the relevant Device Hub matrix. Report build/static checks separately from runtime, camera, accessibility, and transition checks.

## Evidence boundary

- Treat `references/` as operational guidance derived from Apple's six iPhone Duo Tech Talks.
- iOS 27.1 API documentation is not yet available. Keep transcript-only syntax marked **Documentation pending**.
- Never infer missing declarations, availability, module ownership, overloads, defaults, error behavior, or fallback semantics.
- When exact code depends on undocumented detail, provide the smallest transcript-backed sketch and name the SDK or documentation check required before shipping.

## Hard rules

- Use size classes and local scene/view geometry, not idiom, orientation, `UIScreen.main`, fixed breakpoints, or device-name checks.
- Handle every safe-area and layout-margin edge independently.
- Keep interactive foreground content safe; allow decorative/full-bleed backgrounds to extend.
- Do not displace continuous scrolling content. When related elements move, move them together and limit travel.
- Do not nest arrangements inside scrolling containers or navigation containers inside arrangements.
- Prefer system containers and presentations for automatic axis adaptation, fold avoidance, and overflow.
- Do not make features or navigation destinations pose-exclusive.
- A hinge value can be absent; reset hinge-driven effects outside their applicable state.
- For multiple simultaneous display views, reason relative to each view/scene rather than one global display.

## Reference router

Read only the references needed for the task:

| Task | Reference |
|---|---|
| Resizability, size classes, safe areas, outer/inner layout | [`adaptive-layouts.md`](references/adaptive-layouts.md) |
| Fold/camera avoidance, displacement, split/overlay choice | [`reserved-regions-and-arrangements.md`](references/reserved-regions-and-arrangements.md) |
| Navigation, tabs, toolbars, presentations, vertical bars, overflow | [`navigation-bars-and-presentations.md`](references/navigation-bars-and-presentations.md) |
| Displays, configurations, multiple scenes, hinge input, accessories | [`displays-scenes-and-hinge.md`](references/displays-scenes-and-hinge.md) |
| Front-camera selection, direction, preview, rotation | [`camera-experiences.md`](references/camera-experiences.md) |
| State continuity, capability parity, reachability, accessibility | [`continuity-and-accessibility.md`](references/continuity-and-accessibility.md) |
| Device Hub matrix and evidence reporting | [`testing-and-validation.md`](references/testing-and-validation.md) |
| Any iOS 27.1 API spelling or behavior | [`api-status.md`](references/api-status.md) |
| Talk URLs and claim IDs | [`source-map.md`](references/source-map.md) |
| Canonical terminology | [`glossary.md`](references/glossary.md) |

## Output contract

For design or implementation work, state the adaptive baseline, any justified Duo specialization, and required validation. For audits, prioritize violations of the hard rules and cite the owning reference. Never claim runtime or API-documentation verification that was not performed.
