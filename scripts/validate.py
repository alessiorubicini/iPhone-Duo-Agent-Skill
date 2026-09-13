#!/usr/bin/env python3
"""Validate repository structure, metadata, links, sources, and skill routing."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "iphone-duo-agent-skill"
EXPECTED_SOURCES = {
    "prepare-your-app-for-iphone-duo.md": "111461",
    "raise-the-bar-with-iphone-duo.md": "111462",
    "strike-a-pose-with-adaptive-layouts.md": "111463",
    "leverage-multiple-displays-and-scenes.md": "111464",
    "build-a-great-camera-experience.md": "111465",
    "design-for-iphone-duo.md": "111466",
}
EXPECTED_REFERENCES = {
    "_index.md",
    "adaptive-layouts.md",
    "api-status.md",
    "camera-experiences.md",
    "continuity-and-accessibility.md",
    "displays-scenes-and-hinge.md",
    "glossary.md",
    "navigation-bars-and-presentations.md",
    "reserved-regions-and-arrangements.md",
    "source-map.md",
    "testing-and-validation.md",
}


class ValidationError(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts
    )


def validate_json() -> None:
    for relative in (
        "package.json",
        ".claude-plugin/plugin.json",
        ".cursor-plugin/plugin.json",
    ):
        with (ROOT / relative).open(encoding="utf-8") as handle:
            value = json.load(handle)
        require(isinstance(value, dict), f"{relative}: top level must be an object")

    package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
    require(package.get("skill") == SKILL.name, "package.json: skill mismatch")
    require(package.get("skillFolder") == SKILL.name, "package.json: skillFolder mismatch")

    for relative in (".claude-plugin/plugin.json", ".cursor-plugin/plugin.json"):
        plugin = json.loads((ROOT / relative).read_text(encoding="utf-8"))
        require(
            f"./{SKILL.name}" in plugin.get("skills", []),
            f"{relative}: missing skill path",
        )


def parse_frontmatter(path: Path) -> dict[str, str]:
    content = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---(?:\n|$)", content, re.DOTALL)
    require(match is not None, f"{path.relative_to(ROOT)}: invalid frontmatter")

    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        key, separator, value = line.partition(":")
        require(bool(separator), f"{path.relative_to(ROOT)}: unsupported frontmatter line")
        values[key.strip()] = value.strip()
    return values


def validate_skills() -> None:
    for path, expected_name in (
        (SKILL / "SKILL.md", "iphone-duo-agent-skill"),
        (
            ROOT / ".agents/skills/update-iphone-duo-apis/SKILL.md",
            "update-iphone-duo-apis",
        ),
    ):
        values = parse_frontmatter(path)
        require(values.get("name") == expected_name, f"{path}: unexpected skill name")
        require(bool(values.get("description")), f"{path}: missing description")
        require(
            len(values["description"]) <= 1024,
            f"{path}: description exceeds 1024 characters",
        )
        require(
            re.fullmatch(r"[a-z0-9-]{1,64}", values["name"]) is not None,
            f"{path}: invalid skill name",
        )

    metadata = (SKILL / "agents/openai.yaml").read_text(encoding="utf-8")
    for required in (
        "interface:",
        'display_name: "iPhone Duo Agent Skill"',
        "$iphone-duo-agent-skill",
        "allow_implicit_invocation: true",
    ):
        require(required in metadata, f"agents/openai.yaml: missing {required}")


def validate_inventory() -> None:
    references = {
        path.name for path in (SKILL / "references").glob("*.md")
    }
    require(references == EXPECTED_REFERENCES, "reference inventory does not match router")

    source_files = {path.name for path in (ROOT / "sources").glob("*.md")}
    require(source_files == EXPECTED_SOURCES.keys(), "source inventory is not exactly six talks")

    for filename, talk_number in EXPECTED_SOURCES.items():
        content = (ROOT / "sources" / filename).read_text(encoding="utf-8")
        require(
            f"tech-talks/{talk_number}" in content,
            f"sources/{filename}: missing expected Apple talk URL",
        )


def validate_local_links() -> None:
    link_pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
    failures: list[str] = []

    for path in markdown_files():
        for target in link_pattern.findall(path.read_text(encoding="utf-8")):
            clean = target.strip().split("#", 1)[0]
            if not clean or re.match(r"^[a-z][a-z0-9+.-]*:", clean, re.IGNORECASE):
                continue
            resolved = (path.parent / clean).resolve()
            if not resolved.exists():
                failures.append(f"{path.relative_to(ROOT)} -> {target}")

    require(not failures, "broken local links:\n  " + "\n  ".join(failures))


def validate_scaffold_removal() -> None:
    pieces = (
        "[" + "skill-id" + "]",
        "[" + "Skill Name" + "]",
        "[" + "DOMAIN" + "]",
        "[" + "TOPIC" + "]",
        "example" + "-skill",
        "update" + "-skill-template",
        "Foundation" + "Models",
        "starter" + " template",
        "universal agent" + " skill template",
    )
    failures: list[str] = []

    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts or "sources" in path.parts:
            continue
        if path == Path(__file__).resolve() or path.name == ".DS_Store":
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for piece in pieces:
            if piece.casefold() in content.casefold():
                failures.append(f"{path.relative_to(ROOT)} contains {piece!r}")

    require(not failures, "scaffold remnants:\n  " + "\n  ".join(failures))


def validate_talk_traceability() -> None:
    source_map = (SKILL / "references/source-map.md").read_text(encoding="utf-8")
    coverage = (ROOT / "SOURCE_COVERAGE.md").read_text(encoding="utf-8")
    valid_ids = {f"TT-{number}" for number in EXPECTED_SOURCES.values()}

    for talk_id in valid_ids:
        require(talk_id in source_map, f"source-map.md: missing {talk_id}")
        require(talk_id in coverage, f"SOURCE_COVERAGE.md: missing {talk_id}")

    used_ids: set[str] = set()
    for path in markdown_files():
        if "sources" in path.parts:
            continue
        used_ids.update(re.findall(r"TT-\d{6}", path.read_text(encoding="utf-8")))
    require(used_ids <= valid_ids, f"unknown talk IDs: {sorted(used_ids - valid_ids)}")


def main() -> int:
    checks = (
        validate_json,
        validate_skills,
        validate_inventory,
        validate_local_links,
        validate_scaffold_removal,
        validate_talk_traceability,
    )
    try:
        for check in checks:
            check()
    except (OSError, json.JSONDecodeError, ValidationError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print(f"PASS: {len(checks)} repository checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
