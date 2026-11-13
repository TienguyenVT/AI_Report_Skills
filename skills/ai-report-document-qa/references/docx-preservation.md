# DOCX preservation for scripted changes

Read this before direct OOXML edits, block moves, or library/automation rewrites of a complex DOCX. Match the audit to the change; a spelling fix does not require every procedure.

## Source and writes

Use a stable source snapshot for substantial changes. Before overwriting an authorized source, compare its current revision/hash with the baseline and reconcile concurrent changes.

Wait for the writer/export to complete, inspect errors, and reopen the actual output. Do not use an old PDF as evidence for a failed new document build. Close only task-owned documents and application instances.

## Complex content

- Do not assign paragraph.text or cell.text when doing so would discard equations, fields, bookmarks, hyperlinks, drawings, or formatting. Edit the relevant text node or property.
- Do not modify math nodes when changing only nearby references. Preserve leading/trailing whitespace through xml:space="preserve" where needed, then inspect for words joined to citations.
- When wrapping XML with python-docx, use a parent object that has part access, such as doc._body; a raw CT_Body is not interchangeable for style-dependent operations.
- Identify anchors by structure, role, location, and text. Confirm uniqueness; a contents entry can duplicate a body heading.
- For a block move, check start < end and keep the insertion point outside the source block. Verify the resulting order and associated figures, tables, equations, and bookmarks.
- Renumber through an original-to-final mapping or scoped regions, not chained replacements that change the same reference twice.

## Styles, fields, and navigation

Inspect inherited/linked styles, direct formatting, and themes. A single font.name property does not establish all character ranges use that font.

For tables, inspect tblPr, tcPr, tblPrEx, and the table style. Row-level formatting can continue to override a table-level change.

Use real numbering structures for editable lists. Check the numbering part and relationships before adding numPr.

Parse by XML namespace. Count m:oMath separately from m:oMathPara; do not confuse prefix matches such as w:instrText with revision elements.

Compare equation content or normalized XML, not only counts. Record intentional expression changes and compare the remaining expressions separately.

Navigation may use HYPERLINK/PAGEREF fields instead of w:hyperlink elements. Check field instructions, displayed results, and bookmark destinations. Keep paired bookmark boundaries and unique IDs.

Match caption SEQ identifiers with the generated figure/table lists. Do not infer identifiers from visible labels or replace broken fields with typed numbers to conceal an error.

## Verify the final artifact

Choose invariants by scope. A footer edit should preserve body content and math; rewriting a chapter allows the authorized changes only. Historic object counts are not universal requirements.

Compare relevant text, expressions, table structure, media, links, comments, and revisions. A changed whole-file hash can reflect package metadata rather than changed content.

For read-only pagination/export, avoid saving the source. If field updates require a save, use a working copy and compare the result.

Identify the actual renderer; a compatibility ProgID or version string may not identify the product claimed. Tie PDF/images to the final DOCX and inspect the images themselves.

Resolve the actual runtime before adding dependencies. After a tool error following a write, inspect completed artifacts before retrying. Keep QA files separate and remove only verified task-owned temporary files.
