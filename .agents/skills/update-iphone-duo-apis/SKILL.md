---
name: update-iphone-duo-apis
description: Verify transcript-derived iPhone Duo APIs against newly published Apple iOS 27.1 documentation and update the local operational references. Use only for an official API documentation refresh; network access and repository write access required.
---

# Update iPhone Duo APIs

## Scope

Refresh API evidence without replacing the task-oriented structure of `iphone-duo-agent-skill/references/`. Apple's official documentation outranks transcript extraction for declarations and formal semantics; the six checked-in Tech Talks remain the source for design rationale and demonstrated workflows.

Read `references/scan-manifest.md` before browsing.

## Workflow

1. Read `../../../iphone-duo-agent-skill/references/api-status.md` and collect every `Documentation pending` family.
2. Use only official Apple Developer Documentation, release notes, and SDK interfaces. Record canonical URLs; do not use search snippets or third-party mirrors as evidence.
3. For each family, verify declaration, owning module/framework, platform availability, documented semantics, callback/isolation behavior, errors, defaults, and related types. Leave any unresolved field pending.
4. Compare verified declarations against the exact transcript snippet in `../../../sources/`. Record discrepancies; never silently reconcile them by inference.
5. Update the existing task reference that owns the decision. Keep API catalog detail centralized in `api-status.md` and avoid duplicating prose.
6. Compile representative examples against the released iOS 27.1 SDK. Report compilation separately from Device Hub/runtime behavior.
7. Update `_index.md`, `SKILL.md`, `SOURCE_COVERAGE.md`, or glossary only if routing, coverage, or terminology materially changed.
8. Run repository validation and review the final diff for unsupported claims.

## Required status record

For each verified symbol family, add to `api-status.md`:

- Status: `Verified API documentation`
- Canonical Apple documentation URL
- Verification date
- Released SDK/Xcode version used for compilation, when compiled
- Any Tech Talk discrepancy or remaining unknown

Partial documentation does not justify promoting the entire family. Split a row when individual symbols have different evidence status.

## Stop conditions

- Apple page unavailable or JavaScript shell without authoritative declaration: remain pending.
- Only beta headers available: label the exact beta and do not present as shipping API.
- Declaration compiles but behavior is undocumented: record compile evidence while keeping behavioral claim pending.
- Documentation contradicts the transcript: prefer documentation for API facts and preserve a discrepancy note.

## Validation

- JSON plugin/package metadata parses
- YAML metadata parses
- Skill passes `skill-creator/scripts/quick_validate.py`
- All local Markdown links resolve
- Placeholder/template scan is empty outside primary transcripts
- Every new Duo claim has a TT ID or canonical Apple documentation link
- `api-status.md` contains no unqualified promotion from transcript evidence
- Six-talk coverage remains intact
