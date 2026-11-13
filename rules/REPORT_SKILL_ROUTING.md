# Report skill routing

Use this rule for report writing, evidence review, and document presentation. Follow the user's current scope, source restrictions, template, and target application. Load only the skills needed for the requested work.

| Requested work | Primary skill | Add another skill when |
| --- | --- | --- |
| Outline, draft, rewrite, improve argument, reduce repetition | ai-report-writing | New or uncertain claims need ai-report-evidence. |
| Check numbers, methods, comparisons, claims, citations | ai-report-evidence | The user also requests a rewritten passage. |
| Styles, headings, tables, figures, equations, contents, pagination | ai-report-formatting | Content changes are separately in scope. |
| Complete report from source material | All three, at the relevant stages | Check evidence, write, format, then verify the affected content and final pages. |

The skill bodies live in skills/<skill-name>/SKILL.md in this repository. In an installed environment, resolve the skill by its name or plugin-qualified name. Use the host's invocation syntax; the names in this table are identifiers, not universal slash commands.

- A spelling or wording fix does not require a full citation audit. A formatting request does not authorize changing scientific content, measured values, or equations.
- Before directly editing a complex DOCX, read the preservation guidance in ai-report-formatting, even if writing is the main task.
- Preserve the distinction between observed results, interpretation, assumptions, and future work. Missing evidence remains missing until checked.
- Use available document/PDF tools for file operations and rendering. These skills supply quality requirements; they do not provide a renderer.
- Ask only for missing information that changes the result. Continue independent work while waiting; do not ask again for decisions already made.
- Project-specific skills can supplement this workflow when actually available and relevant. Do not import another project's measurements, chapter structure, sources, or preferences.
- If a skill or tool is unavailable, state the relevant limitation and complete the supported work. Do not claim a skill was loaded or a document was rendered when it was not.
- Do not interpret this rule as permission to run new experiments, change code, upload documents, publish, or submit work.
