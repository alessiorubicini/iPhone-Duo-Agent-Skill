# Contributing

Contributions should improve the accuracy or operational value of the iPhone Duo Agent Skill without speculating beyond Apple's published material.

## Before editing

Read [AGENTS.md](AGENTS.md), then use [the reference index](iphone-duo-agent-skill/references/_index.md) to locate the owning topic. The checked-in files under `sources/` are the primary evidence for current Duo-specific claims.

## Content workflow

1. Identify whether the change is general Apple-platform guidance, transcript-backed Duo behavior, or published iOS 27.1 API documentation.
2. Update the smallest task-oriented reference that owns the guidance.
3. Cite Duo claims with talk IDs from `references/source-map.md`.
4. Update `references/api-status.md` for any API evidence/status change.
5. Update `_index.md`, `SKILL.md`, and `SOURCE_COVERAGE.md` only when routing or coverage changes.

## API contributions

Until Apple publishes the iOS 27.1 API reference, preserve transcript API spellings exactly and label them `Documentation pending`. Do not infer:

- Full declarations or overloads
- Framework ownership unless the talk states it
- Availability annotations or fallback behavior
- Parameter labels, option-set combinations, actor isolation, or error semantics not shown in source
- Whether transcript snippets compile unchanged in the shipping SDK

After publication, follow [API_REFERENCE_ROADMAP.md](API_REFERENCE_ROADMAP.md) and the `update-iphone-duo-apis` maintenance skill. Cite the exact Apple documentation URL for each verified symbol family.

## Pull request checklist

- [ ] Every changed Duo claim traceable to one or more checked-in Apple sources or published Apple API documentation
- [ ] No device-model checks, fixed Duo metrics, or symmetric-inset assumptions
- [ ] No pose-exclusive capability or navigation hierarchy
- [ ] SwiftUI and UIKit guidance aligned where both are covered by Apple
- [ ] Transcript-only API examples still marked `Documentation pending`
- [ ] All six Tech Talks remain represented in `SOURCE_COVERAGE.md`
- [ ] Reference index and `SKILL.md` router match files on disk
- [ ] Markdown links resolve; JSON and YAML parse
- [ ] Scaffold-remnant scan and skill validation pass
- [ ] Runtime claims limited to tests actually performed

## Validation

From the repository root:

```bash
python3 scripts/validate.py
```

The repository validator checks metadata, skill frontmatter, file inventories, local Markdown links, scaffold remnants, six-talk coverage, and known talk IDs. Maintainers should additionally run the upstream Agent Skills validator used by their distribution platform.

## License

Contributions are licensed under the repository's [MIT License](LICENSE).
