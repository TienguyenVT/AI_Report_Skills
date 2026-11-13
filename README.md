# AI Report Skills

Three focused skills for writing, checking, and presenting reports with an AI assistant.

**English** | [Tiếng Việt](README.vi.md)

Vietnamese-first instructions for academic, technical, and work reports. Keep each report's own template and source restrictions while improving structure, evidence traceability, and document presentation.

## What this addresses

AI can produce fluent text while changing the meaning, inventing a citation, mixing measurements from different conditions, or damaging a Word document during a small edit. This toolkit separates those responsibilities so the assistant loads guidance relevant to the task.

| Skill | Use it for |
| --- | --- |
| [ai-report-writing](skills/ai-report-writing/SKILL.md) | Outlines, drafting, rewriting, argument structure, terminology, and reducing repetition. |
| [ai-report-evidence](skills/ai-report-evidence/SKILL.md) | Claims, numbers, experimental conditions, comparisons, citations, and source checks. |
| [ai-report-formatting](skills/ai-report-formatting/SKILL.md) | Word/WPS styles, tables, figures, equations, contents, pagination, and rendered verification. |

The [routing rule](rules/REPORT_SKILL_ROUTING.md) selects one skill or combines them when needed. A spelling fix should stay small. Completing a report may require all three.

## Install

Install directly from [TienguyenVT/AI_Report_Skills](https://github.com/TienguyenVT/AI_Report_Skills), or clone it for local use:

```bash
git clone https://github.com/TienguyenVT/AI_Report_Skills.git
cd AI_Report_Skills
```

### Claude Code plugin

From a Claude Code session:

```text
/plugin marketplace add TienguyenVT/AI_Report_Skills
/plugin install ai-report-skills@ai-report-skills
```

The plugin exposes the three skill folders through [.claude-plugin/plugin.json](.claude-plugin/plugin.json). Select an installed skill from the host's menu or request it by name; the host may qualify skill names with the plugin name.

For explicit project routing, merge [rules/REPORT_SKILL_ROUTING.md](rules/REPORT_SKILL_ROUTING.md) into the consuming project's CLAUDE.md. Installing the plugin does not install this repository's root CLAUDE.md into other projects. Claude's validator reports that root file as project-only context; this is expected.

### Codex

For standalone skills, copy the desired complete folders from skills/ into one location:

| Scope | Destination |
| --- | --- |
| One project | .agents/skills/ inside that project |
| Personal | ~/.agents/skills/ |

Include references and agents metadata. Preserve existing skill folders and avoid installing duplicate names in multiple locations. Merge the routing rule into the consuming project's AGENTS.md.

In Codex CLI or the IDE extension:

```text
$ai-report-writing Rewrite this section for clarity without changing the evidence.
```

Alternatively, this repository includes a portable [plugin.json](plugin.json) and [Codex marketplace catalog](.agents/plugins/marketplace.json). On clients supporting local marketplaces, register this GitHub marketplace:

```bash
codex plugin marketplace add TienguyenVT/AI_Report_Skills
```

Then install from that marketplace in the desktop plugin directory. Choose this approach or standalone skills; both are not required.

See the official [skills documentation](https://developers.openai.com/codex/skills/) and [plugin packaging documentation](https://developers.openai.com/plugins/build/plugins). Reload or restart the host if newly installed skills do not appear.

### Cursor or another agent

The [.cursor/rules/report-skills.mdc](.cursor/rules/report-skills.mdc) file supplies a report-specific rule; it is not set to apply to every task.

For another project, copy that rule, rules/REPORT_SKILL_ROUTING.md, and the skills/ folders together, preserving relative paths. Alternatively, adjust the rule to the installed locations.

For another agent, explicitly provide the routing rule and the selected SKILL.md. Automatic selection and invocation syntax depend on the host. The [reference repository's Cursor guide](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/CURSOR.md) illustrates the project-rule distribution pattern.

## Examples

```text
Use ai-report-writing to reorganize this chapter. Preserve every equation,
table, figure, and measured value.

Use ai-report-evidence to check these conclusions against the attached
sources only. List unsupported claims before changing the prose.

Use ai-report-formatting to match this table style in WPS. Preserve the data
and verify the final layout in the target application.
```

See [EXAMPLES.md](EXAMPLES.md) for scoped requests and acceptance criteria. These are review cases, not claims that a host integration or writing-quality benchmark has passed.

## Layout

```text
plugin.json                       Portable plugin identity
.claude-plugin/                   Claude plugin and marketplace manifests
.agents/plugins/marketplace.json  Codex local marketplace
skills/                           Three independently usable skills
rules/REPORT_SKILL_ROUTING.md      Host-neutral routing instructions
AGENTS.md                         Codex/repository maintenance instructions
CLAUDE.md                         Claude project instructions
.cursor/rules/                    Cursor project rule
scripts/validate.py               Offline package checks
tests/                            Validator regression checks
```

The skill bodies are in Vietnamese. The assistant should still follow the requested report language. The toolkit does not impose a chapter count, a research field, or one font and table style.

## Validate

Python 3.10 or newer is needed for development checks, not for reading the skills.

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s tests
```

If Claude Code is installed:

```bash
claude plugin validate .claude-plugin/plugin.json
claude plugin validate .claude-plugin/marketplace.json
```

GitHub Actions runs the offline checks. They cover metadata, manifest consistency, package paths, local Markdown links, and selected private-artifact indicators. They do not verify scientific claims, measure writing quality, guarantee automatic selection, or prove Word/WPS rendering.

## Boundaries

- The skills are instructions, not a document renderer or evidence database.
- Editing DOCX/PDF requires suitable tools in the user's environment.
- Installation does not authorize uploads, publication, submission, or invented content.
- Use permitted sources and keep missing evidence explicit.
- The package contains no hooks, MCP servers, credentials, or report data.

## Contributing and license

See [CONTRIBUTING.md](CONTRIBUTING.md). Released under the [MIT License](LICENSE).

The distribution layout was inspired by [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills): focused skills, project rules, plugin manifests, and setup instructions. The report-specific guidance is independently authored from report-editing practice. This project is not affiliated with that repository or its maintainers.
