"""Offline structural checks for this repository; not a writing-quality evaluator."""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml

SKILLS = {"ai-report-writing", "ai-report-evidence", "ai-report-formatting"}
IGNORED = {".git", "__pycache__", ".venv", "venv"}
PRIVATE_SUFFIXES = {".docx", ".pdf", ".zip", ".bak"}
LOCAL_PATH = re.compile(r"(?i)(?:[a-z]:[\\/](?:Users|Projects)[\\/]|/(?:Users|home)/[^/\s]+/)")


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []

    def check(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    def read_json(relative: str) -> dict:
        return json.loads((root / relative).read_text(encoding="utf-8"))

    def within(relative: str) -> Path:
        path = (root / relative).resolve()
        check(path.is_relative_to(root), f"Path escapes package: {relative}")
        check(path.exists(), f"Missing package path: {relative}")
        return path

    try:
        portable = read_json("plugin.json")
        claude = read_json(".claude-plugin/plugin.json")
        marketplace = read_json(".claude-plugin/marketplace.json")
        codex = read_json(".agents/plugins/marketplace.json")
        for field in ("name", "version", "license"):
            check(portable.get(field) == claude.get(field), f"Manifest mismatch: {field}")
        check(portable.get("name") == "ai-report-skills", "Unexpected plugin name")
        check(portable.get("license") == "MIT", "Expected MIT license")
        check(bool(re.fullmatch(r"\d+\.\d+\.\d+", portable.get("version", ""))),
              "Plugin version must use three numeric components")
        check((root / "LICENSE").read_text(encoding="utf-8").startswith("MIT License"),
              "Missing MIT license text")

        declared = claude.get("skills", [])
        check(set(declared) == {f"./skills/{name}" for name in SKILLS},
              "Claude manifest must declare all three skill folders")
        for path in declared:
            within(path)

        for entry in marketplace["plugins"]:
            check(entry.get("name") == portable["name"], "Claude marketplace identity mismatch")
            check(entry.get("version") == portable["version"], "Claude marketplace version mismatch")
            check(entry.get("license") == "MIT", "Claude marketplace license mismatch")
            check(within(entry["source"]) == root, "Claude marketplace source must resolve to plugin root")
        check(len(marketplace["plugins"]) == 1, "Expected one Claude marketplace entry")
        check(marketplace.get("name") == portable["name"], "Claude marketplace name mismatch")
        for entry in codex["plugins"]:
            check(entry.get("name") == portable["name"], "Codex marketplace identity mismatch")
            check(entry["source"].get("source") == "local", "Expected local Codex source")
            check(within(entry["source"]["path"]) == root, "Codex source must resolve to plugin root")
            check(entry.get("policy", {}).get("installation") == "AVAILABLE",
                  "Codex plugin must be available, not auto-installed")
        check(len(codex["plugins"]) == 1, "Expected one Codex marketplace entry")

        actual = {p.name for p in (root / "skills").iterdir() if p.is_dir()}
        check(actual == SKILLS, "Skill directory inventory differs from the three declared skills")
        for name in SKILLS:
            skill = root / "skills" / name
            text = (skill / "SKILL.md").read_text(encoding="utf-8")
            parts = text.split("---", 2)
            check(len(parts) == 3 and parts[0] == "", f"{name}: missing YAML frontmatter")
            if len(parts) != 3:
                continue
            meta = yaml.safe_load(parts[1])
            check(meta.get("name") == name, f"{name}: frontmatter name mismatch")
            check(isinstance(meta.get("description"), str) and 0 < len(meta["description"]) <= 1024,
                  f"{name}: missing or overlong description")
            check(meta.get("license") == "MIT", f"{name}: missing license")
            check(bool(parts[2].strip()), f"{name}: empty instructions")
            ui = yaml.safe_load((skill / "agents/openai.yaml").read_text(encoding="utf-8"))
            check("$" + name in ui["interface"]["default_prompt"], f"{name}: default prompt mismatch")
            check(25 <= len(ui["interface"]["short_description"]) <= 64,
                  f"{name}: UI description length")
            check(ui.get("policy", {}).get("allow_implicit_invocation", True),
                  f"{name}: unexpected explicit-only policy")

        for file in root.rglob("*"):
            relative = file.relative_to(root)
            if any(part in IGNORED for part in relative.parts):
                continue
            check(not file.is_symlink(), f"Symlink is not portable: {relative}")
            if not file.is_file():
                continue
            check(not any(p == "qa" or p.startswith("_qa") for p in relative.parts),
                  f"QA material in public package: {relative}")
            check(file.suffix.lower() not in PRIVATE_SUFFIXES, f"Private artifact: {relative}")
            check(not file.name.startswith(".env") or file.name == ".env.example",
                  f"Environment file in public package: {relative}")
            if file.suffix not in {".md", ".mdc", ".py", ".json", ".yaml", ".yml", ".txt"}:
                continue
            text = file.read_text(encoding="utf-8")
            check("\ufffd" not in text, f"Invalid replacement character: {relative}")
            check(not LOCAL_PATH.search(text), f"Machine-specific path: {relative}")
            if file.suffix in {".md", ".mdc"}:
                check("[TODO" not in text, f"Unfinished scaffold: {relative}")
                for target in re.findall(r"\]\(([^)\n]+)\)", text):
                    target = target.strip("<>")
                    parsed = urlsplit(target)
                    if parsed.scheme or target.startswith("#"):
                        continue
                    linked = (file.parent / unquote(parsed.path)).resolve()
                    check(linked.is_relative_to(root), f"{relative}: link escapes package: {target}")
                    check(linked.exists(), f"{relative}: broken link: {target}")
    except (OSError, ValueError, TypeError, KeyError, AttributeError, yaml.YAMLError) as error:
        errors.append(f"Invalid or missing package data: {error}")
    return errors


if __name__ == "__main__":
    issues = validate(Path(__file__).resolve().parents[1])
    for issue in issues:
        print("ERROR:", issue)
    if issues:
        sys.exit(1)
    print("PASS: three skills, manifests, local links, and package hygiene.")
