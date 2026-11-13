# AI Report Skills

For report tasks, follow the routing rule below and load the relevant skill from skills/. Keep the user's project-specific requirements and existing authorization scope.

@rules/REPORT_SKILL_ROUTING.md

When maintaining this repository, run python scripts/validate.py and python -m unittest discover -s tests. Do not include private reports, data, machine paths, backups, or credentials.

Installing this repository as a plugin exposes its skills; it does not install this root CLAUDE.md into unrelated projects. Merge the routing rule into a consuming project's CLAUDE.md if explicit project-level routing is wanted.
