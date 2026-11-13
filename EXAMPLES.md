# Example requests and review cases

These are synthetic requests and acceptance criteria, not experimental results or benchmark claims. Use only the cases relevant to a change.

| Request | Expected routing | What to inspect |
| --- | --- | --- |
| Fix spelling in one paragraph; preserve all values. | Writing | Only the selected language changes; numbers, units, citations, and scope remain intact. |
| Build an outline from supplied notes. | Writing | Each section has a purpose and available material; gaps do not become invented results. |
| Check whether a citation supports a claim. | Evidence | Inspect the actual passage; a matching topic is not enough. |
| Compare tables measured under different settings. | Evidence | Check conditions and metric conventions before drawing a conclusion. |
| Match table formatting to a sample. | Formatting | Preserve values, merged cells, equations, and captions; inspect affected pages. |
| Rewrite a DOCX section containing equations and fields. | Writing + formatting | Read preservation guidance before editing; keep surrounding structure intact. |
| Create a report from notes and approved sources. | All three, by stage | Check evidence, prose, and layout separately; keep missing material explicit. |
| This project uses a different outline and table style. | Relevant skill + project rules | Actual requirements win over generic examples or historical preferences. |

## Vietnamese prompts

### Rewrite without expanding scope

Dùng ai-report-writing viết lại đoạn được chọn cho dễ hiểu. Giữ nguyên số liệu,
ký hiệu, điều kiện đo và mức độ chắc chắn; không thêm luận điểm mới.

Review: improve the prose without turning a possibility into a confirmed result.
A rewrite of unrelated sections is a failure.

### Review evidence without editing

Dùng ai-report-evidence đối chiếu nhận định với các nguồn tôi cho phép. Ghi vị trí,
bằng chứng và đề xuất sửa; chưa chỉnh tệp báo cáo.

Review: findings need usable locations. Do not invent a DOI, silently expand
the source set, or mutate the document.

### Format an editable document

Dùng ai-report-formatting làm bảng theo mẫu hiện có. Giữ nguyên số liệu và công thức,
kiểm tra trong ứng dụng đích và báo rõ nếu chưa render được.

Review: an output file existing on disk is insufficient. Check preservation and
rendered layout separately. Do not replace editable equations with screenshots.

## Recording a real evaluation

Record input scope, host/version, selected skills, artifacts inspected, output
changes, and unresolved limits. Keep private evaluation material outside the public
package. Describe observed behavior; do not mark a case passed merely because the
instructions contain matching words.
