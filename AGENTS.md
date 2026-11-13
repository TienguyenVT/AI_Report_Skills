# Repository instructions

For report tasks, read [the routing rule](rules/REPORT_SKILL_ROUTING.md) and only the relevant SKILL.md files under skills/. Apply the user's project-specific instructions before reusable defaults.

When maintaining this repository:
- Keep the three skills focused on writing, evidence, and formatting respectively.
- Preserve the user's requested scope and the distinction between a check and proof.
- Keep skills self-contained; do not require private skills, local machine paths, or project data.
- Keep plugin names, versions, skill directories, and installation instructions consistent.
- Run python scripts/validate.py and python -m unittest discover -s tests after changing packaging or validation code.
- Never include real reports, unpublished data, credentials, QA backups, or local logs in the public package.
- Publishing or changing a remote requires a separate user request.

When reusing this workflow in another project, merge rules/REPORT_SKILL_ROUTING.md into that project's instructions. Do not replace its existing AGENTS.md with these repository maintenance instructions.
