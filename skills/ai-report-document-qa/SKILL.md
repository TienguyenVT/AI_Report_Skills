---
name: ai-report-document-qa
description: Preserve and verify report artifacts during editing, export, conversion, or cross-application handoff. Use for complex DOCX, cloud-document revisions, Markdown/HTML or LaTeX builds, PDF checks, editability, and source/output mismatches; this provides a QA workflow, not application drivers.
license: MIT
---

# Report artifact preservation and QA

This generalizes document-editing experience into three independent checks: content, structure, and presentation. Passing one does not prove the others.

## Choose relevant checks

Identify the authoritative source, output, target application, intended medium, and editable features that must survive. Use [format checks](references/format-checks.md) for the actual format; do not run every profile for a simple edit.

Before scripted DOCX transformations, read [DOCX preservation](references/docx-preservation.md). Preserve the user's editing and review workflow.

## Protect the source and user work

- Record a stable revision/checkpoint for consequential changes. Keep an independent recovery copy when appropriate.
- Prefer native incremental edits when they preserve live unsaved work. Before replacing a file, recheck its baseline and reconcile concurrent changes.
- Do not close, save, or terminate unrelated user documents/processes to simplify automation. Only close instances created and owned by the task.
- Wait for writers and exports to finish; inspect their result and exit status. Reopen the actual destination, not a stale preview or in-memory object.
- After a failure that may occur after a write, check the state before retrying. Do not repeat a conversion against a newer user revision.

## Validate three layers

1. **Content:** compare text, values, expressions, captions, images, links, and review material that should be preserved. Explain intentional differences. Object counts or whole-file hashes alone do not establish semantic preservation.
2. **Structure:** reopen the artifact, check relevant relationships and navigation targets, and confirm native editability where required. Check the correct body/header/footer/caption roles rather than only the main text.
3. **Presentation:** render or open the final revision and inspect affected pages/screens. Review the whole layout after global changes and check section/page transitions, tables, captions, equations, and whitespace.

Tie QA output to the exact final source revision. An old PDF, generated thumbnails, or a list of image paths is not proof that the final pages were inspected.

## Verify in the right environment

Identify the actual application or renderer before claiming compatibility. A compatibility API name or version string can refer to another application.

For a required cross-application handoff, test the critical features in the destination. When editable delivery is important, modify a small copy, update navigation, save, and reopen it; keep that test copy out of the delivered artifact.

Inspect font substitution, equation behavior, linked/embedded resources, generated fields, and comments/revisions as relevant. Do not claim that a single successful round-trip proves every feature is compatible.

If tooling is missing, use an available supported path and state the limitation. Do not install unrelated software or invent validation. Tool failures, policy restrictions, and unsupported formats are different conditions.

## Deliver verifiable results

Provide the actual artifact, what changed, which checks ran, which application was used, and remaining limits. Keep QA files separate and remove only task-owned temporary files after verifying their paths and purpose.

Do not promise support for every application. The reusable principles apply broadly; integration and rendering depend on the tools available in the user's environment.
