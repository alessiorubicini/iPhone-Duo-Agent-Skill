# iOS 27.1 API Reference Integration Roadmap

The task-oriented structure is intentionally stable. When Apple publishes iOS 27.1 documentation, integrate authoritative API detail without reorganizing the skill around frameworks or documentation pages.

## Current state

`iphone-duo-agent-skill/references/api-status.md` is the single inventory of new or changed API names mentioned in the Tech Talks. Entries currently record:

- Symbol or family name exactly as stated or shown
- Framework only when the talk identifies it or the containing established type makes it explicit
- Source talk ID
- Current evidence status
- Missing details that block stronger code-generation claims

Task references link to the inventory but retain the implementation decision: why an agent would choose the API and which invariants surround it.

## Publication workflow

1. Confirm that the page is official Apple Developer Documentation for the shipping iOS 27.1 SDK.
2. Capture the exact canonical URL, declaration, framework/module, platform availability, and documented semantics.
3. Compare the published declaration with every transcript snippet; do not silently rewrite discrepancies.
4. Update the matching row in `api-status.md` from `Documentation pending` to `Verified API documentation` and record the verification date.
5. Add only decision-relevant detail to the owning task reference. Avoid copying full Apple documentation.
6. Validate examples against the released SDK. Label compilation evidence separately from Device Hub/runtime behavior.
7. Update the source map and coverage file only if the new evidence adds or changes a supported claim.

## Conflict handling

Published API documentation outranks transcript extraction for declarations and formal semantics. Preserve a short discrepancy note when a transcript spelling differs so existing references remain auditable. If documentation remains ambiguous, keep the specific claim pending instead of resolving it by inference.

## Structural guarantees

The following files already own all future API detail:

- `api-status.md` — symbol inventory, evidence status, canonical documentation links
- Task references — decision rules and implementation context
- `source-map.md` — source identity and traceability
- `testing-and-validation.md` — compile/runtime validation obligations
- `.agents/skills/update-iphone-duo-apis/` — repeatable refresh procedure

No new top-level taxonomy is required when the documentation arrives. Add a focused reference only if a genuinely new developer task cannot fit an existing owner without becoming difficult to retrieve.
