# Using the iPhone Duo Agent Skill

Invoke the skill for design, implementation, review, debugging, or validation work whose result must behave correctly across iPhone Duo displays, poses, and multitasking configurations.

## Example prompts

### Audit an existing app

```text
Use $iphone-duo-agent-skill to audit this SwiftUI app for iPhone Duo. Identify fixed-size assumptions, unsafe centering, custom bars, pose-exclusive controls, and missing Device Hub cases. Do not implement changes.
```

Expected result: prioritized findings tied to code locations, the relevant reference rules, and an explicit distinction between static evidence and runtime checks still required.

### Design an adaptive feature

```text
Use $iphone-duo-agent-skill to design a media player that preserves one hierarchy on the outer and inner displays, supports a tabletop pose, and never hides transport controls in the fold. Choose standard containers before custom Duo logic.
```

Expected result: a layout decision based on size classes and content relationships, plus a pose/configuration validation matrix. Any iOS 27.1 API spelling remains marked as transcript-derived until documented.

### Implement a custom layout

```text
Use $iphone-duo-agent-skill to replace this hand-built split/overlay layout with the most appropriate arrangement. Keep scrolling content out of the arrangement container and preserve every action in all configurations.
```

Expected result: a split-versus-overlay rationale, the smallest code change, and a documentation caveat for transcript-only APIs.

### Review navigation and bars

```text
Use $iphone-duo-agent-skill to make these toolbar items work in horizontal and vertical bars. Preserve semantic placement, titles, accessibility, and the most important actions during overflow.
```

Expected result: system-container adoption, axis-compatible representations, grouping/priority decisions, and no fabricated APIs.

### Plan a camera experience

```text
Use $iphone-duo-agent-skill to decide between the Virtual Front Camera and individual front cameras for this capture workflow, including open/close transitions and an outer-display accessory.
```

Expected result: a capability tradeoff, per-view direction coordination where required, actor-boundary considerations stated only as supported by the talk, and camera/preview transition tests.

## Evidence labels in skill output

- **Established platform guidance** — ordinary adaptive Apple-platform practice; not represented as new Duo API behavior.
- **Tech Talk evidence** — behavior or API name stated or shown in one of the six source transcripts.
- **Documentation pending** — iOS 27.1 declaration or behavior still requiring verification against Apple Developer Documentation.
- **Verified API documentation** — reserved for future entries that include the exact Apple documentation URL and verification metadata.

## Expected limits

The current skill can select architectures, preserve Apple-shown patterns, identify unsupported assumptions, and define tests. It must not fill gaps in the unpublished iOS 27.1 API reference. When exact compilation-ready syntax depends on those gaps, the correct output is a bounded implementation sketch plus the named verification requirement.
