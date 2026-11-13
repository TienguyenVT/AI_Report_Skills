---
name: ai-report-formatting
description: Design or standardize report presentation in document editors, cloud documents, Markdown/HTML, LaTeX, or PDF workflows. Use for hierarchy, styles, tables, figures, equations, navigation, and readable layouts; preserve substantive content unless editing it is requested.
license: MIT
---

# Report presentation

Make the report readable, consistent, and appropriate for its audience and medium. Use the requested template and target application; do not impose one font, chapter count, or historical table style.

## Inspect and select the medium

Identify the source, editable output, delivery medium, target application, and affected scope. Read the current template and representative pages or screens. Reuse established design decisions; for a new untemplated report, state reasonable presentation choices without calling them an institutional standard.

Classify content by role: body, heading, caption, note, equation, table, cover, and navigation. A named style or a table object may be used for a different purpose.

Use available native tools or format-specific capabilities. This skill is not a renderer, editor integration, or universal application driver. For conversion, complex file edits, or cross-application compatibility, use ai-report-document-qa.

## Establish hierarchy

- Use semantic headings, paragraph styles, list structures, and spacing properties rather than spaces or blank lines used as layout.
- Match heading levels to the actual outline. Do not add or delete chapters merely for appearance.
- Keep labels, terminology, units, emphasis, and notation consistent. Preserve meaningful bold/italic, subscripts, symbols, and hyperlinks.
- Do not apply body justification, indentation, or font settings indiscriminately to covers, captions, code, tables, or equations.
- Use native editable structures where practical. Do not flatten a table or equation into an image to hide an editing or rendering problem.
- For digital output, check heading navigation, link labels, meaningful reading order, and useful alternative text. Do not claim formal accessibility compliance without the required evaluation.

## Design tables and figures

Choose tables for lookup or exact comparison, charts for relationships or trends, and prose when neither helps. Explain the message without duplicating all displayed values.

Keep data, merged cells, notes, units, and precision unchanged during a formatting-only task. Identify table-style values from the actual sample before applying them.

Fit content to its medium: repeat table headers where supported, allow content to grow, avoid clipped rows, and keep captions with their objects. A row taller than a page may need a deliberate break.

Keep graphics proportional and labels legible at final size. Use redundant labels or patterns when color alone would carry meaning. Show scales, units, denominators, and uncertainty where needed; avoid transformations that mislead.

## Maintain navigation and references

Identify whether numbers and links are manual, generated, or cached. Check real heading targets and caption types before regenerating contents or lists of figures/tables.

For paginated output, derive page numbers from actual layout after updates. For flowing HTML or cloud documents, verify anchors and navigation rather than inventing fixed page numbers.

Keep section/page-number conventions and citation mechanisms intact unless change is requested. Updating a field does not prove the displayed destination or page is correct.

## Verify the result

Review affected pages/screens and their boundaries; inspect the whole layout after global style changes or restructuring. Look for orphan headings, broken tables, detached captions, clipped equations, unreadable labels, unexpected whitespace, and missing navigation.

Use the target application when claiming compatibility. A successful export, valid package, or correct page count alone is not a visual check. If rendering is unavailable, state which structural checks succeeded and which visual checks remain.

Deliver the actual requested format with concise changes and verification limits. For a plain-text edit, do not add unnecessary conversion or page-rendering steps.
