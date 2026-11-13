---
name: ai-report-evidence
description: Verify report claims, numbers, methods, source support, and citations. Use for factual or numerical checks and reference audits across research, business, technical, and operational reports; do not infer permission to rerun experiments or rewrite the entire document.
license: MIT
---

# Report evidence

Establish what a source supports and what remains uncertain. A fluent sentence, matching topic, valid identifier, or passing script is not proof of the claim.

## Define the check

Identify the current report, requested findings or edits, and permitted source set. Honor restrictions such as attached files only. Continue checks that do not depend on an unanswered question; do not silently expand the source set.

For a long report, use the compact record in [evidence ledger](references/evidence-ledger.md). A single correction can be checked directly. Record who or what actually checked a source; an AI check is not a human sign-off.

## Bind the claim to the source

- Read the supporting passage, table, dataset, log, or implementation at the relevant version. Search results, summaries, memory, and reference lists are discovery aids.
- Check the direction, population or system, time, units, and conditions of the claim. A source may support one clause but not the rest of a sentence.
- Preserve the distinction between direct evidence, reported evidence, interpretation, assumption, and proposal.
- Verify title, author or organization, date, version, and identifiers before filling bibliographic details. Record corrections or version changes when they affect the claim.
- When only a secondary source is accessible, label that limitation. Do not imply the original work was read.
- Use current authoritative material for time-sensitive claims when the source policy permits it. Otherwise report the restriction and the unverified part.

## Check quantitative consistency

Trace values to their source and aggregation method. Check units, scale, sign, precision, numerator/denominator, independent sample size, reporting period, and missing-data handling where relevant.

Compare repeated values across text, tables, plots, summaries, and conclusions. A difference may reflect a legitimate change of population or time window; explain it instead of forcing agreement.

Distinguish simulations, offline analysis, software execution, and physical measurements. Successful execution does not establish real-time performance, operational acceptance, or a causal explanation.

Do not equate similar parameter values with comparable methods. Use ai-report-source-comparison for differing definitions or configurations and ai-report-critical-review for inference, design, or statistical concerns.

Recalculate only within the task's scope. Preserve the input, formula, and interpretation; do not change values just to remove a discrepancy. Do not invent uncertainty intervals, p-values, acceptance limits, or missing results.

## Audit citations and displays

- Check that each citation supports the nearby proposition. Include claims in tables, captions, footnotes, and display lists.
- Verify quotations against the source; paraphrasing borrowed ideas still requires attribution.
- Follow the required citation system. Numbering by order of appearance applies only when that is the chosen system.
- Check citation-to-entry and entry-to-purpose mappings; preserve an intentionally separate reading list.
- Check data provenance, transformations, denominators, labels, and uncertainty in figures. A polished chart cannot repair an unsupported conclusion.
- Treat software/AI attribution separately from evidence for report claims. Do not add a toolkit citation solely because a downloaded skill asks for one.

## Report findings

For each material issue, provide its location, current claim, supporting or conflicting evidence, consequence, and a specific correction or question. Prioritize issues that change the conclusion.

If direct edits are authorized, modify only supported content and revisit dependent locations. Keep unresolved questions visible in working notes; do not present guesses as final facts.

State what was checked and what was unavailable. Reading a paper is not reproducing its experiment; checking a DOI is not validating its findings.
