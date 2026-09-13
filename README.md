# iPhone Duo Agent Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-5B5BD6)](https://agentskills.io)

Operational guidance for AI coding agents that design, audit, implement, and validate native SwiftUI and UIKit apps for iPhone Duo.

The skill is organized around developer decisions rather than video summaries: adaptive layout, displays and configurations, safe and reserved regions, arrangements, navigation and bars, scenes and hinge input, continuity, camera behavior, accessibility, and testing. Its current Duo-specific evidence comes from all six official Apple iPhone Duo Tech Talks checked into [`sources/`](sources/).

## Evidence boundary

The iOS 27.1 API documentation is not yet available. Consequently:

- New API names and snippets are retained only where Apple showed or stated them in the Tech Talks.
- Transcript-derived APIs are clearly marked `Documentation pending`.
- The skill does not invent declarations, availability, framework ownership, overloads, semantics, or fallbacks.
- Agents are instructed to separate supported design guidance from code that still requires SDK/documentation verification.

The repository already has a dedicated [API status inventory](iphone-duo-agent-skill/references/api-status.md), [source map](iphone-duo-agent-skill/references/source-map.md), and [integration roadmap](API_REFERENCE_ROADMAP.md), so the future iOS 27.1 reference can be incorporated without reorganizing the skill.

## Install

### Agent Skills CLI

```bash
npx skills add https://github.com/alessiorubicini/iPhone-Duo-Agent-Skill --skill iphone-duo-agent-skill
```

### Claude Code plugin

```text
/plugin marketplace add alessiorubicini/iPhone-Duo-Agent-Skill
/plugin install iphone-duo-agent@iphone-duo-agent-skill
```

### Manual installation

Copy or symlink [`iphone-duo-agent-skill/`](iphone-duo-agent-skill/) into the skills directory used by the coding agent. For Codex:

```bash
cp -R iphone-duo-agent-skill "$CODEX_HOME/skills/iphone-duo-agent-skill"
```

Then invoke it explicitly when needed:

```text
Use $iphone-duo-agent-skill to audit this camera app for iPhone Duo.
```

See [USAGE.md](USAGE.md) for realistic task prompts and expected output boundaries.

## What the skill enables

- Audit existing apps for resizability, local geometry, asymmetric safe areas, and multitasking
- Choose between natural flow, displacement, standard navigation, split/overlay arrangements, and reserved-region handling
- Adapt navigation, toolbars, tab bars, presentations, custom items, and overflow to vertical-bar contexts
- Reason about scene-local displays, multiple windows, hinge-driven interactions, and scene accessories
- Plan camera selection and transitions using the Virtual Front Camera or individually selected cameras
- Preserve state, capability, hierarchy, and accessibility across outer/inner display and pose changes
- Produce a Device Hub validation matrix without overstating unperformed runtime checks

## Current Apple sources

| Tech Talk | Primary coverage |
|---|---|
| [Prepare your app for iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111461/) | SDK opt-in, resizability, size classes, safe areas, standard containers, Device Hub |
| [Raise the Bar with iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111462/) | Vertical navigation/tool/tab bars, item axis behavior, compression, overflow |
| [Strike a pose with adaptive layouts on iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111463/) | Displacement, reserved regions, split and overlay arrangements |
| [Leverage multiple displays and scenes on iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111464/) | Hinge observation, multitasking, multiple scenes, scene accessories |
| [Build a great camera experience for iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111465/) | Virtual/physical front cameras, direction, preview, rotation, dual-display capture |
| [Design for iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111466/) | Design principles, pose adaptation, reachability, continuity, fold avoidance |

Detailed coverage is audited in [SOURCE_COVERAGE.md](SOURCE_COVERAGE.md).

This is an independent community project and is not affiliated with or endorsed by Apple. Apple source material and trademarks remain subject to their respective terms; see [NOTICE.md](NOTICE.md).

## Repository structure

```text
iphone-duo-agent-skill/
  SKILL.md                         concise operating rules and topic router
  agents/openai.yaml              OpenAI skill metadata
  assets/logo.svg                 skill icon
  references/
    _index.md                     task-to-reference router
    adaptive-layouts.md
    reserved-regions-and-arrangements.md
    navigation-bars-and-presentations.md
    displays-scenes-and-hinge.md
    camera-experiences.md
    continuity-and-accessibility.md
    testing-and-validation.md
    api-status.md
    source-map.md
    glossary.md
sources/                           primary Tech Talk transcripts and extracted code
.agents/skills/update-iphone-duo-apis/
                                     future API documentation refresh workflow
```

## Contributing

Read [AGENTS.md](AGENTS.md) for the evidence and content contract, then follow [CONTRIBUTING.md](CONTRIBUTING.md). Duo-specific factual changes require traceability to official Apple material.

## License

Original skill content and tooling: [MIT](LICENSE). Third-party source material: [NOTICE.md](NOTICE.md).
