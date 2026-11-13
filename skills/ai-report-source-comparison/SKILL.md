---
name: ai-report-source-comparison
description: Extract and compare definitions, parameters, metrics, requirements, or methods across reports, papers, specifications, datasets, and implementation snapshots. Use when similarly named values may have different conditions or meanings; do not infer permission to change configurations or rerun work.
license: MIT
---

# Source and configuration comparison

A generalized edition of configuration-extraction experience. Answer the actual comparison question without silently merging incompatible sources.

## Separate the task and evidence types

Distinguish extracting published information, inspecting the current implementation, comparing results, and changing/rerunning a system. A request for a parameter table authorizes extraction, not an experiment.

Keep source-reported settings, settings observed in a particular implementation/version, and recommendations in separate columns. Reading a paper does not establish that a program uses its configuration.

## Extract with context

Identify the exact source and version. Search meaningful terms, notation variants, units, and nearby methodology sections. Read surrounding material when a sentence, definition, or table crosses a page or column.

Inspect a rendered page when extraction may lose signs, exponents, subscripts, merged headers, or column order. Distinguish the PDF page index from printed page numbering. Use exact file names rather than truncated labels.

Capture enough context to interpret a value: base versus effective/normalized quantities, fixed versus variable settings, defaults versus overrides, and the applicable scenario. Preserve “not reported” rather than filling from another source.

## Build an auditable comparison

| Item and meaning | Source/version and locator | Reported value/unit | Conditions or transformation | Comparability / open issue |
| --- | --- | --- | --- | --- |

Select only the fields needed for the question. For reproducibility or quantitative comparison, relevant conditions may include inputs, population/system, initialization, version, measurement boundary, time window, aggregation, and uncertainty.

Do not assume identical symbols or numerical settings mean identical methods. Conversely, different units may express the same quantity only after an explicit, valid conversion.

A mean over a transient interval is not automatically a stable-state value. A transformed-scale difference is not automatically a relative change in the underlying quantity. State the reference denominator and handle zero or undefined comparisons explicitly.

## Interpret and deliver

Separate differences observed in the sources from causes demonstrated by controlled evidence. Matching trends do not establish numerical equivalence or statistical replication.

Retain each author's stated rationale with its own settings. A claim of fair or optimal tuning remains that source's claim unless independently tested.

Return the comparison, exact source locations, conditions that matter, and unresolved gaps. Use ai-report-critical-review if the user asks whether the design or inference is justified. Use ai-report-evidence to audit claims that cite the comparison.
