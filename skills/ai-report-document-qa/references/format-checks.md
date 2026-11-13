# Select checks for the actual format

These are verification profiles, not bundled application integrations. Use only available, authorized tools and report the actual application/version used.

| Format or workflow | Preserve and inspect | Presentation / handoff check |
| --- | --- | --- |
| Word, WPS, LibreOffice / DOCX | Styles, fields, equations, tables, images, comments, revisions, sections, bookmarks | Reopen in the target editor; update the appropriate fields; inspect the final pages and critical editable objects. |
| Cloud documents | Document/revision identity, selected range, semantic blocks, suggestions, comments, links, collaborator changes | Read back the current revision. Inspect the native view and exported format when both are deliverables. |
| Markdown / HTML | Heading hierarchy, anchors, relative links, code blocks, image resources, math, source content | Use the intended renderer; inspect readable widths and print layout only when print is required. |
| LaTeX | Source, bibliography, labels, equations, figures, included files, build configuration | Use the existing build path; inspect errors and relevant warnings, unresolved citations/references, and the final PDF. |
| Spreadsheet-based reports | Formula/value distinction, source ranges, units, filters, hidden content, chart references, print areas | Recalculate using the appropriate engine, inspect displayed values and exported pages; do not replace formulas with values without authorization. |
| Slide-based reports | Master/layout roles, speaker notes, chart data, reading order, links and embedded objects | Inspect slide view and any required PDF export; page fidelity does not prove animations or embedded media work. |
| PDF delivery | Pages, selectable text where expected, figures, bookmarks, links, fonts and source alignment | Inspect the final PDF; a structurally valid file does not prove readability or accessibility. Preserve an editable source if required. |

For cloud collaboration, an earlier snapshot or selection is not permission to replace a whole document. Verify the live target before a scoped mutation and preserve concurrent work.

For source-based formats, modify the authoritative source instead of patching the exported artifact unless the export itself is the requested editing target.

During conversion, agree which capabilities matter: visual fidelity, editability, navigation, formulas, comments, or accessibility. Some may not survive the chosen format. State losses; do not hide them by flattening content.

Examples of legitimate checks include reading the saved revision, checking referenced assets, updating a generated index, and inspecting actual pages. Avoid treating a screenshot count, ZIP check, or successful build as the complete check.
