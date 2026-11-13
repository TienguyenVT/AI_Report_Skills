# Contributing

Tie each change to a concrete report-writing, review, or packaging problem. Write skill instructions in English and maintain both English and Vietnamese README files. The report output must still follow the user's requested language.

1. Describe the task, failure, and expected behavior without sharing private report content.
2. Update the smallest relevant skill or routing rule. Keep domain-specific preferences in the consuming project's instructions.
3. For third-party adaptations, inspect the actual source and license. Record the pinned source, changed scope, and retained notices in PROVENANCE.md and THIRD_PARTY_NOTICES.md. Preserve notices inside affected standalone skill folders.
4. Update relevant links, examples, UI metadata, manifests, and bilingual documentation.
5. Install requirements-dev.txt and run python scripts/validate.py.
6. Try relevant cases in EXAMPLES.md for behavioral changes, and report what was actually observed. Static checks do not measure writing quality or routing behavior.
7. For a claimed formatting or compatibility fix, verify a representative artifact in the stated target application. Keep private reports and QA outputs outside the public package.

Keep the seven responsibilities distinct. Add supporting references only when they help an actual task; do not require every skill for small edits.

The portable and Claude manifests share a name, version, and license. Marketplace entries expose that same plugin. Skill names match their directories, and local resources stay inside each skill so it can be copied independently.

New contributions are provided under the repository's MIT license. Third-party material retains its original notices; do not imply that project authors wrote all adapted content or that source attribution constitutes endorsement.
