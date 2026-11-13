# Repository instructions

For report tasks, read [the routing rule](rules/REPORT_SKILL_ROUTING.md) and only the relevant SKILL.md files. Apply the user's current scope and project requirements before reusable defaults.

When maintaining this repository:
- Keep the seven skills distinct: writing, evidence, presentation, revision, artifact QA, source comparison, and critical review.
- Use English for skill instructions and maintain English/Vietnamese README files.
- Keep each skill useful independently; companion skills are conditional, not mandatory dependencies for every task.
- Preserve the distinction between source checks, inference, structural checks, and visual verification.
- Keep source adaptations and licenses documented in PROVENANCE.md and THIRD_PARTY_NOTICES.md.
- Do not require private skills, machine paths, project data, paid services, or hardcoded clinical frameworks.
- Keep manifests, versions, skill lists, routing, and documentation consistent.
- Run python scripts/validate.py after relevant changes. Keep evaluation artifacts outside the public package.
- Do not restore the removed tests directory unless the user asks.
- Do not include real reports, unpublished data, credentials, QA backups, or local logs in the package.
- Publishing or changing a remote requires user authorization; preserve authorization already given for the active task.

When reusing the workflow elsewhere, merge rules/REPORT_SKILL_ROUTING.md into that project's instructions. Do not replace its existing rules with these repository maintenance instructions.
