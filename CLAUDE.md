# AI Report Skills

For report tasks, follow the routing rule below and load only the relevant skill. Preserve the user's language, report requirements, and authorization scope.

@rules/REPORT_SKILL_ROUTING.md

When maintaining this repository, run python scripts/validate.py. Keep source adaptations and licenses documented, use English skill instructions, and maintain both README languages. Keep private artifacts outside the package.

Installing the plugin exposes its skills; this root CLAUDE.md is not automatically installed as project context elsewhere. Merge the routing rule into a consuming project's instructions when explicit routing is wanted.
