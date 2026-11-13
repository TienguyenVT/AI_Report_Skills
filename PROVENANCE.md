# Source review and adaptation record

This document records how version 0.2.0 generalizes experience guides and incorporates reviewed third-party material. It is an attribution and design record, not a claim that every host, report type, or application has been tested.

## User-owned experience guides

The project owner authorized generalized public editions of these local guides. Originals remain separate; private paths, report contents, measurements, historical file names, and personal preferences are not bundled.

| Reviewed guide | Public edition | Retained decisions | Removed or generalized |
| --- | --- | --- | --- |
| afc-report-lessons | [ai-report-revision](skills/ai-report-revision/SKILL.md), with relevant points in writing/evidence | Scope control, current-version checks, preserving meaning, bounded edits, resuming work, verified lessons | A particular research domain, algorithms, measurement windows, chapter structure, historical results, fixed table preferences |
| word-wps-lessons | [ai-report-document-qa](skills/ai-report-document-qa/SKILL.md), with presentation choices in formatting | Source preservation, concurrency, renderer identity, native editability, fields/navigation, final-artifact verification | Machine paths, application-version anecdotes, specific handover data, assumptions that every report uses Word/WPS |
| afc-paper-config | [ai-report-source-comparison](skills/ai-report-source-comparison/SKILL.md) | Exact locators, extraction pitfalls, semantic parameter differences, configuration/version separation, comparable conditions | Particular parameter values, experiment names, hardware settings, and automatic permission to rerun code |

These are rewritten, generalized editions rather than raw backups. The source names identify the lineage; no external installation is required to use their public counterparts.

## External skills reviewed

Source repository: [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills).

Pinned review commit: [2d2065fb4520fa3f3f2bcf61cff26ec8b7eba4b5](https://github.com/K-Dense-AI/scientific-agent-skills/commit/2d2065fb4520fa3f3f2bcf61cff26ec8b7eba4b5).

The reviewed locally installed text matched this snapshot after newline normalization. License: MIT, copyright 2025 K-Dense Inc. The [original notice](licenses/K-Dense-MIT.txt) is included.

| Upstream material | Included adaptation | Limits of the adaptation |
| --- | --- | --- |
| [scientific-writing/SKILL.md](https://github.com/K-Dense-AI/scientific-agent-skills/blob/2d2065fb4520fa3f3f2bcf61cff26ec8b7eba4b5/skills/scientific-writing/SKILL.md) | Writing by purpose, method/result consistency, uncertainty and source boundaries in writing/evidence | No mandatory journal-submission workflow for routine reports |
| [writing_principles.md](https://github.com/K-Dense-AI/scientific-agent-skills/blob/2d2065fb4520fa3f3f2bcf61cff26ec8b7eba4b5/skills/scientific-writing/references/writing_principles.md) | Preserve observation/estimate/interpretation distinctions; terminology and numeric consistency; avoid arbitrary prose rules | No fixed paragraph length, citation quota, or minimum figure count |
| [evidence_workflow.md](https://github.com/K-Dense-AI/scientific-agent-skills/blob/2d2065fb4520fa3f3f2bcf61cff26ec8b7eba4b5/skills/scientific-writing/references/evidence_workflow.md) | Compact claim/source/locator record and explicit verification states | No required five-registry system, per-sentence hash markers, or invented human approval |
| [figures_tables.md](https://github.com/K-Dense-AI/scientific-agent-skills/blob/2d2065fb4520fa3f3f2bcf61cff26ec8b7eba4b5/skills/scientific-writing/references/figures_tables.md) | Choose appropriate displays, preserve source data, label uncertainty and encodings, inspect final-size legibility | No mandatory visual generation service or minimum number of graphics |
| [scientific-critical-thinking/SKILL.md](https://github.com/K-Dense-AI/scientific-agent-skills/blob/2d2065fb4520fa3f3f2bcf61cff26ec8b7eba4b5/skills/scientific-critical-thinking/SKILL.md) | [ai-report-critical-review](skills/ai-report-critical-review/SKILL.md): question-first, proportionate and traceable appraisal | Formal evidence-grading frameworks are conditional and must be checked at use |
| [statistical_pitfalls.md](https://github.com/K-Dense-AI/scientific-agent-skills/blob/2d2065fb4520fa3f3f2bcf61cff26ec8b7eba4b5/skills/scientific-critical-thinking/references/statistical_pitfalls.md) | Prompts about denominators, independent units, significance, leakage and incompatible synthesis | No automatic statistical tests, scoring, or reconstructed results |
| [experimental_design.md](https://github.com/K-Dense-AI/scientific-agent-skills/blob/2d2065fb4520fa3f3f2bcf61cff26ec8b7eba4b5/skills/scientific-critical-thinking/references/experimental_design.md) | Sampling/measurement, alternative explanations, and applicability questions | No universal clinical checklist, power threshold, or mandatory experimental design |

## Material intentionally not bundled

- The complete upstream skills, executable helpers, registries, and static bibliographies are not copied wholesale.
- Historical guideline/version claims and the upstream request to cite a skill paper are not inserted automatically into users' reports. Relevant policies and sources must be checked for the actual task.
- Optional paid schematic-generation tools and service credentials are not dependencies.
- Private workflow permissions do not become blanket authorization to edit unrelated documents, change configurations, upload data, or publish.
- Source review is not a benchmark of writing quality or application compatibility.

## Attribution and independence

See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Affected standalone skill folders carry the relevant license notices too. Adaptations changed scope, structure, examples, terminology, and workflow requirements for general reports; they are not official K-Dense releases.

The original distribution layout was inspired by [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills). This repository is not affiliated with either source project.
