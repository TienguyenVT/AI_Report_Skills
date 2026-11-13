---
name: ai-report-revision
description: Revise existing reports while preserving scope, version history, reviewer intent, and concurrent edits. Use for substantial restructuring, multi-round feedback, targeted changes in complex documents, or resuming interrupted report work; a simple wording fix can use ai-report-writing alone.
license: MIT
---

# Report revision

This is a generalized edition of report-collaboration experience. It manages the change, while ai-report-writing improves prose and ai-report-document-qa verifies the artifact.

## Establish a trustworthy baseline

Identify the document ID/path and current saved or live revision. “Final” in a filename or a recent timestamp is not sufficient when versions conflict. Read the affected section, its neighbors, and related previously edited content.

Preserve a recoverable baseline for large edits or overwrites. Use a revision ID, checkpoint, or hash appropriate to the application. An available file lock does not prove a desktop editor has no unsaved buffer.

Honor confirmed decisions until the user changes them. Ask about consequential ambiguity or conflicting versions; do not ask again for already authorized editing.

## Convert feedback into bounded changes

For a substantial revision, use a compact map:

| Request | Current location | Intended change | Content to preserve | Acceptance check |
| --- | --- | --- | --- | --- |

Distinguish editorial, structural, factual, presentational, and unresolved requests. A request to inspect, plan, or collect lessons is not permission to edit the report.

When reorganizing, map old sections to new ones before moving content. Carry associated figures, tables, equations, comments, links, and references. Removing a heading does not imply removing its content or renumbering unrelated displays.

When scientific or business meaning must change, establish the evidence first. Use ai-report-evidence for facts and ai-report-critical-review for disputed interpretations.

## Edit without collateral changes

- Change the smallest unit that fulfills the request, while reading enough context to maintain coherence.
- Do not flatten complex document structures just to replace visible text. Preserve the application's editable objects.
- Keep observed results, assumptions, interpretations, and future commitments distinct across rounds.
- Maintain terminology and notation across affected sections. Do not globally rewrite unrelated content for stylistic consistency.
- Use the host's revisions, comments, or versioning if requested. Do not silently accept/reject pre-existing changes or remove reviewer comments.

Before replacing a saved source, check that its baseline has not changed. If it has, reconcile against the new version and preserve the user's edits; do not restore an old snapshot over them.

## Resume and close the loop

After interruption or a tool error, inspect the actual document and completed operations before retrying. A missing tool response does not prove the write failed.

After editing, compare the intended change map with the result and verify dependent references and surrounding layout. If the user still sees a problem, inspect the exact version and application they are using rather than relying on an earlier completion message.

Deliver the saved revision, changes made, checks performed, and unresolved questions. Record reusable lessons only when requested or authorized, with context, observed cause or uncertainty, remedy, and verification. Do not turn one user's layout preference or a single tool failure into a universal rule.
