# Example requests and acceptance cases

These are synthetic requests, not measured outcomes. Select only cases relevant to a change. English instructions should preserve the user's requested report language.

| Request | Primary routing | Acceptance criterion |
| --- | --- | --- |
| Fix spelling in one paragraph, preserve values | Writing | Only the requested language changes; no full audit or unrelated rewrite. |
| Write an operational update from notes | Writing | Distinguish completed work, blockers, and proposed actions; do not invent owners or dates. |
| Produce a business decision memo | Writing + evidence as needed | Separate facts, assumptions, tradeoffs, and recommendation; no fabricated costs. |
| Verify a citation using attached sources only | Evidence | Read actual support; do not expand the source set or infer support from a title. |
| Reorganize an existing report with reviewer comments | Revision + writing | Preserve the change map, objects, comments, and other authors' edits. |
| Resume after a failed save response | Revision + document QA | Inspect current state before retrying; do not overwrite a newer revision. |
| Match a table's presentation to a sample | Formatting | Preserve values and formulas; inspect the affected layout. |
| Convert a cloud document to DOCX | Document QA | Check current revision, retained features, actual exported file, and target app limits. |
| Prepare Markdown/HTML for screen reading | Formatting + QA as needed | Verify semantic hierarchy, links, figures and readable view; do not invent fixed page numbers. |
| Build a LaTeX report for PDF delivery | Document QA | Use the existing build, check references and warnings, inspect the final PDF. |
| Compare parameters or metrics across sources | Source comparison | Preserve definitions, conditions and versions; mark unreported values. |
| Review a before/after causal claim | Critical review + evidence | Consider other explanations; distinguish missing detail from a demonstrated flaw. |
| Present a benchmark as proof of deployment readiness | Critical review | Keep benchmark observations separate from unmeasured operational acceptance. |
| Complete a report from approved materials | Core workflow; specialists as needed | Check support, prose, presentation, and final artifact separately. |

## Concrete examples

### Same label, different metric

Synthetic sources: one document reports a daily mean of per-team percentages; another reports a percentage calculated from pooled monthly counts.

Request: “Explain why these two rates differ.”

Expected behavior: source comparison identifies denominator, weighting, and period differences before a numeric comparison. It does not label one source wrong or claim a causal explanation without evidence.

### Scoped wording in Vietnamese

Request: “Viết lại đoạn được chọn cho dễ hiểu, giữ số liệu và mức độ chắc chắn.”

Expected behavior: improve the Vietnamese prose, preserve values and qualifiers, and leave unselected sections alone. The English SKILL.md is not a reason to translate the report.

### Conversion with an unavailable renderer

Request: “Convert this report and confirm the layout is identical.”

Expected behavior: perform only the supported conversion and structural checks, identify the unavailable target-application check, and avoid claiming visual equivalence. A ZIP check cannot close this gap.

## Recording an actual evaluation

Record the request, available source, selected skill, output, actual checks, and limits. Use synthetic or authorized materials. Keep private artifacts outside the repository.

Do not mark a case passed because the instructions contain its expected wording. A package validator checks structure, not reasoning quality or host behavior.
