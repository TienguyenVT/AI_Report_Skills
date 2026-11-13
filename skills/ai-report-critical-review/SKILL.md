---
name: ai-report-critical-review
description: Appraise whether a report's reasoning, study design, comparisons, and uncertainty justify its conclusions. Use for research, business analysis, evaluations, incidents, or technical benchmarks when inference quality matters; do not apply a formal research audit to a routine wording edit.
license: MIT
---

# Critical review of report conclusions

Review the inferential step, not only whether a citation exists. Apply standards suited to the actual question and evidence; do not import clinical frameworks into unrelated work.

## Fix the question

Identify the report's claim, intended decision, relevant population/system, comparator or baseline, outcome, time horizon, and independent unit of observation where applicable.

Distinguish descriptive, predictive, causal, and prescriptive claims. Determine what evidence would be needed for that type of conclusion. A recommendation also depends on constraints and values, not just an estimated effect.

## Inspect before judging

Read the result and supporting method, uncertainty, denominators, exclusions, and relevant source material. Use ai-report-evidence for source checks and ai-report-source-comparison for incompatible definitions or settings.

Keep “not reported” separate from “not performed.” State conditional concerns when the available material cannot resolve them.

Check the relevant issues in [appraisal prompts](references/appraisal-prompts.md): selection, measurement, confounding, dependence, missingness, multiple analyses, leakage, alternatives, and applicability. Do not require every item for every report.

## Match conclusions to support

- Distinguish association from causation, non-significance from equivalence, and statistical evidence from practical importance.
- Examine uncertainty and effect magnitude together when available. Do not invent a test, confidence interval, sample size, or universal significance threshold.
- Separate exploratory/post hoc analyses from prespecified ones. Retain relevant negative, conflicting, and inconclusive evidence.
- Check whether apparently independent evidence shares the same dataset, sources, or assumptions.
- A good model fit, successful build, or functioning prototype is not proof of causal validity, generalization, real-time performance, or operational acceptance.
- Do not assign a quality score by counting checklist items. A missing detail and a demonstrated flaw have different implications.

Use formal reporting, risk-of-bias, or evidence-certainty frameworks only when the question warrants one. Verify the applicable tool/version and unit of assessment from its primary guidance. This skill does not certify regulatory, clinical, or statistical compliance.

## Give constructive, traceable feedback

For each concern provide the report/source location, observation, consequence for the conclusion, uncertainty, and feasible remedy. Distinguish material threats to the main inference from minor reporting issues.

Acknowledge strengths and credible alternative explanations. Apply the same criteria to findings you agree and disagree with.

When edits are authorized, narrow the claim to what the evidence supports; do not merely soften wording while preserving an unsupported inference. When only review is requested, deliver findings without mutating the report.

The review should identify what can be concluded, what remains uncertain, and what additional evidence could resolve it. Do not claim that a methodological review has reproduced the underlying work.
