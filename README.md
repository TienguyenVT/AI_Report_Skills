# AI Report Skills

Seven focused skills for writing, checking, revising, and presenting reports with an AI assistant.

**English** | [Tiếng Việt](README.vi.md)

The skill instructions are in **English**; reports follow the user's requested language. Use them for academic, technical, business, operational, or educational reports, with the report's own template, audience, source policy, and target application.

## Choose the relevant skill

| Skill | Use it for |
| --- | --- |
| [ai-report-writing](skills/ai-report-writing/SKILL.md) | Outlines, drafting, rewriting, synthesis, terminology, and clear prose. |
| [ai-report-evidence](skills/ai-report-evidence/SKILL.md) | Claims, numbers, methods, source support, and citations. |
| [ai-report-formatting](skills/ai-report-formatting/SKILL.md) | Hierarchy, styles, tables, figures, equations, navigation, and layout. |
| [ai-report-revision](skills/ai-report-revision/SKILL.md) | Existing reports, reviewer feedback, restructuring, version conflicts, and interrupted work. |
| [ai-report-document-qa](skills/ai-report-document-qa/SKILL.md) | Content preservation, native editability, export/conversion, and final artifact verification. |
| [ai-report-source-comparison](skills/ai-report-source-comparison/SKILL.md) | Definitions, metrics, configurations, methods, requirements, and comparable conditions. |
| [ai-report-critical-review](skills/ai-report-critical-review/SKILL.md) | Whether study design, reasoning, comparisons, and uncertainty justify conclusions. |

The [routing rule](rules/REPORT_SKILL_ROUTING.md) selects the smallest useful set. A wording fix can use writing alone. A full report proceeds through evidence, writing, presentation, and verification; specialist skills join only when relevant.

The three experience editions generalize report-editing, Word/WPS, and paper-configuration lessons. Writing, evidence, presentation, and critical review also incorporate selected material from the installed K-Dense scientific skills. See [PROVENANCE.md](PROVENANCE.md) for the exact sources, pinned revision, adaptations, and exclusions.

## Formats and applications

The workflow covers presentation and QA considerations for Word/WPS/LibreOffice documents, cloud documents, Markdown/HTML, LaTeX, PDF, and reports delivered through spreadsheets or slides. See the [format profiles](skills/ai-report-document-qa/references/format-checks.md).

These are reusable instructions. File editing, cloud access, rendering, and automatic skill selection depend on the host's tools. The package does not ship application drivers or claim every application has been tested.

## Install

Clone the repository when using files directly:

```bash
git clone https://github.com/TienguyenVT/AI_Report_Skills.git
cd AI_Report_Skills
```

### Claude Code plugin

In a Claude Code session:

```text
/plugin marketplace add TienguyenVT/AI_Report_Skills
/plugin install ai-report-skills@ai-report-skills
```

The [plugin manifest](.claude-plugin/plugin.json) exposes all seven skills. Select a skill from the host's menu or request it by name; the host may qualify names with the plugin name.

For project-specific routing, merge [rules/REPORT_SKILL_ROUTING.md](rules/REPORT_SKILL_ROUTING.md) into that project's CLAUDE.md. Installing the plugin does not install this repository's root CLAUDE.md as instructions in other projects. Claude's validator may report that file as project-only context.

### Codex standalone skills

Copy the desired **complete skill folders**, including LICENSE.txt, references, and agents metadata, into one location:

| Scope | Destination |
| --- | --- |
| One project | .agents/skills/ inside the project |
| Personal | ~/.agents/skills/ |

Preserve existing folders and avoid duplicate skill names in multiple locations. Merge the routing rule into the consuming project's AGENTS.md. Companion skills are optional; install those relevant to the work.

Example invocation:

```text
$ai-report-writing Rewrite this section in Vietnamese for clarity while preserving its evidence.
```

The repository also includes a portable [plugin.json](plugin.json) and [Codex marketplace catalog](.agents/plugins/marketplace.json). On a client supporting plugin marketplaces:

```bash
codex plugin marketplace add TienguyenVT/AI_Report_Skills
```

Then install the plugin from that marketplace using the host's plugin directory. Use either the plugin or standalone folders; both are not required.

See the official [skills documentation](https://developers.openai.com/codex/skills/) and [plugin packaging documentation](https://developers.openai.com/plugins/build/plugins). Reload the host if newly installed skills do not appear.

### Cursor and other assistants

The [.cursor/rules/report-skills.mdc](.cursor/rules/report-skills.mdc) rule is scoped to report work. Copy it, the routing rule, and the selected skills/ folders together, preserving relative paths; adjust paths when installing elsewhere.

For a host without skill discovery, provide the routing rule and selected SKILL.md explicitly, plus a referenced resource when the task needs it. Automatic selection and invocation syntax depend on the host.

## Example requests

```text
Use ai-report-revision to apply these review comments to the current report.
Preserve unrelated edits and map any sections that move.

Use ai-report-source-comparison to compare these two KPI definitions.
Keep their populations, reporting periods, and denominators explicit.

Use ai-report-critical-review to assess whether the data support this
causal claim. Review only; do not edit the report.

Use ai-report-document-qa to verify the final editable document and PDF.
Identify the renderer used and any checks that remain unavailable.
```

[EXAMPLES.md](EXAMPLES.md) contains scoped requests and acceptance criteria. They are review cases, not completed writing-quality benchmarks or application compatibility tests.

## Repository layout

```text
skills/                           Seven skills, references, UI metadata, licenses
rules/REPORT_SKILL_ROUTING.md      Host-neutral selection and workflow
plugin.json                       Portable plugin identity
.claude-plugin/                   Claude plugin and marketplace manifests
.agents/plugins/marketplace.json  Codex marketplace catalog
.cursor/rules/                    Cursor project rule
AGENTS.md / CLAUDE.md              Repository maintenance/context
PROVENANCE.md                     Source review and adaptation record
THIRD_PARTY_NOTICES.md            Attribution and redistribution notes
licenses/                         Original upstream license text
scripts/validate.py               Offline structural/package checks
```

## Validate and contribute

Python 3.10 or newer is required for development checks, not for reading the skills.

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py
```

If Claude Code is installed:

```bash
claude plugin validate .claude-plugin/plugin.json
claude plugin validate .claude-plugin/marketplace.json
```

GitHub Actions runs the offline validator. It checks metadata, manifests, local links, standalone resources, license notices, and selected private-artifact indicators. It does not prove writing quality, factual accuracy, automatic routing, or rendering compatibility.

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution and evaluation guidance.

## License and boundaries

Released under the [MIT License](LICENSE). Keep each skill's LICENSE.txt when redistributing it. Selected K-Dense adaptations retain their original MIT notice; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

The distribution layout was inspired by [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills). This repository is not affiliated with either upstream project.

The skills do not impose a research field, chapter count, font, citation style, or historical user preference. They contain no report data, credentials, hooks, or MCP servers. Using a skill does not authorize uploads, publication, submission, experiments, or changes outside the user's task.
