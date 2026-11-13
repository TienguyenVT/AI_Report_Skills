# AI Report Skills

Bảy skill chuyên trách giúp AI viết, kiểm chứng, chỉnh sửa và trình bày báo cáo.

[English](README.md) | **Tiếng Việt**

Các tệp **SKILL.md viết bằng tiếng Anh**; báo cáo vẫn dùng ngôn ngữ người dùng yêu cầu. Bộ skill dành cho báo cáo học thuật, kỹ thuật, kinh doanh, vận hành và giáo dục, theo đúng mẫu, đối tượng đọc, phạm vi nguồn và ứng dụng đích của từng công việc.

## Chọn skill theo công việc

| Skill | Công việc phù hợp |
| --- | --- |
| [ai-report-writing](skills/ai-report-writing/SKILL.md) | Lập dàn ý, viết mới, viết lại, tổng hợp tài liệu, thống nhất thuật ngữ và diễn đạt. |
| [ai-report-evidence](skills/ai-report-evidence/SKILL.md) | Kiểm tra nhận định, số liệu, phương pháp, nguồn và trích dẫn. |
| [ai-report-formatting](skills/ai-report-formatting/SKILL.md) | Cấp mục, style, bảng, hình, công thức, điều hướng và bố cục. |
| [ai-report-revision](skills/ai-report-revision/SKILL.md) | Sửa báo cáo có sẵn, xử lý góp ý, tái cấu trúc, xung đột phiên bản và tiếp tục việc bị gián đoạn. |
| [ai-report-document-qa](skills/ai-report-document-qa/SKILL.md) | Bảo toàn nội dung, khả năng chỉnh sửa, xuất/chuyển đổi và kiểm tra tệp cuối. |
| [ai-report-source-comparison](skills/ai-report-source-comparison/SKILL.md) | Đối chiếu định nghĩa, chỉ số, cấu hình, phương pháp, yêu cầu và điều kiện so sánh. |
| [ai-report-critical-review](skills/ai-report-critical-review/SKILL.md) | Đánh giá liệu thiết kế, lập luận, phép so sánh và độ bất định có hỗ trợ kết luận hay không. |

[Rule phân luồng](rules/REPORT_SKILL_ROUTING.md) chọn số skill cần thiết cho từng việc. Sửa câu chữ có thể chỉ cần skill viết. Làm báo cáo đầy đủ đi từ bằng chứng đến nội dung, trình bày và kiểm tra; bổ sung skill chuyên trách khi có nhu cầu.

Ba skill kinh nghiệm được khái quát hóa từ quá trình biên tập báo cáo, xử lý Word/WPS và truy cấu hình bài báo. Các phần viết, bằng chứng, trình bày và phản biện còn tiếp nhận có chọn lọc nội dung từ bộ scientific skills của K-Dense đã cài trước đó. [PROVENANCE.md](PROVENANCE.md) ghi nguồn, phiên bản đối chiếu, phần tiếp nhận và phần loại bỏ.

## Định dạng và ứng dụng

Bộ skill có hướng dẫn trình bày và kiểm tra cho Word/WPS/LibreOffice, tài liệu đám mây, Markdown/HTML, LaTeX, PDF, cùng báo cáo trình bày qua bảng tính hoặc slide. Xem [hướng dẫn theo định dạng](skills/ai-report-document-qa/references/format-checks.md).

Đây là hướng dẫn quy trình. Khả năng sửa tệp, truy cập tài liệu đám mây, kết xuất và tự chọn skill phụ thuộc công cụ của ứng dụng AI. Repo không kèm bộ điều khiển ứng dụng và không khẳng định đã thử trên mọi ứng dụng.

## Cài đặt

Nếu sử dụng trực tiếp các tệp:

```bash
git clone https://github.com/TienguyenVT/AI_Report_Skills.git
cd AI_Report_Skills
```

### Plugin cho Claude Code

Chạy trong phiên Claude Code:

```text
/plugin marketplace add TienguyenVT/AI_Report_Skills
/plugin install ai-report-skills@ai-report-skills
```

[Manifest plugin](.claude-plugin/plugin.json) khai báo đủ bảy skill. Chọn từ menu của ứng dụng hoặc gọi theo tên; ứng dụng có thể thêm tên plugin vào tên skill.

Để phân luồng theo dự án, ghép [rules/REPORT_SKILL_ROUTING.md](rules/REPORT_SKILL_ROUTING.md) vào CLAUDE.md của dự án đó. Việc cài plugin không tự đưa CLAUDE.md ở gốc repo này vào dự án khác. Trình kiểm tra Claude có thể cảnh báo tệp đó chỉ là ngữ cảnh của dự án hiện tại.

### Cài skill độc lập cho Codex

Sao chép **nguyên thư mục skill** cần dùng, gồm LICENSE.txt, references và agents, vào một trong các vị trí:

| Phạm vi | Nơi cài |
| --- | --- |
| Một dự án | .agents/skills/ trong dự án |
| Cá nhân | ~/.agents/skills/ |

Giữ các thư mục đã có và tránh cài trùng tên skill ở nhiều nơi. Ghép rule phân luồng vào AGENTS.md của dự án sử dụng. Các skill phối hợp là tùy nhu cầu, không bắt buộc cài tất cả.

Ví dụ:

```text
$ai-report-writing Viết lại mục này bằng tiếng Việt cho rõ ràng, giữ nguyên bằng chứng.
```

Repo cũng có [plugin.json](plugin.json) và [danh mục marketplace Codex](.agents/plugins/marketplace.json). Với ứng dụng có hỗ trợ marketplace plugin:

```bash
codex plugin marketplace add TienguyenVT/AI_Report_Skills
```

Sau đó cài plugin từ marketplace qua danh mục plugin của ứng dụng. Chọn plugin hoặc các thư mục skill độc lập; không cần cài cả hai.

Tham khảo [tài liệu skill chính thức](https://developers.openai.com/codex/skills/) và [tài liệu đóng gói plugin](https://developers.openai.com/plugins/build/plugins). Tải lại ứng dụng nếu chưa thấy skill mới.

### Cursor và các trợ lý khác

[Rule Cursor](.cursor/rules/report-skills.mdc) chỉ dành cho công việc báo cáo. Sao chép rule này, rule phân luồng và các thư mục skills/ cần dùng cùng nhau; giữ cấu trúc đường dẫn hoặc điều chỉnh khi cài ở vị trí khác.

Nếu ứng dụng không tự phát hiện skill, cung cấp trực tiếp rule phân luồng và SKILL.md được chọn, kèm tài liệu tham chiếu khi công việc cần. Cách gọi và khả năng tự chọn skill phụ thuộc ứng dụng.

## Ví dụ yêu cầu

```text
Dùng ai-report-revision để áp dụng góp ý vào bản báo cáo hiện tại.
Giữ các chỉnh sửa không liên quan và lập đối chiếu cho những mục bị di chuyển.

Dùng ai-report-source-comparison để so sánh hai cách định nghĩa KPI này.
Làm rõ tập đối tượng, kỳ báo cáo và mẫu số của mỗi bên.

Dùng ai-report-critical-review để đánh giá kết luận nhân quả này.
Chỉ nhận xét, chưa chỉnh sửa báo cáo.

Dùng ai-report-document-qa để kiểm tra bản tài liệu còn chỉnh sửa được và PDF.
Nêu ứng dụng kết xuất và những bước chưa thể kiểm tra.
```

[EXAMPLES.md](EXAMPLES.md) có các tình huống và tiêu chí nghiệm thu. Đây là ca tham khảo để đánh giá, không phải tuyên bố đã vượt qua thử nghiệm chất lượng viết hoặc tương thích ứng dụng.

## Cấu trúc repo

```text
skills/                           Bảy skill, tham chiếu, metadata, giấy phép
rules/REPORT_SKILL_ROUTING.md      Chọn skill và phối hợp theo nhiệm vụ
plugin.json                       Định danh plugin
.claude-plugin/                   Manifest plugin và marketplace Claude
.agents/plugins/marketplace.json  Danh mục marketplace Codex
.cursor/rules/                    Rule dự án cho Cursor
AGENTS.md / CLAUDE.md              Hướng dẫn duy trì repo/ngữ cảnh
PROVENANCE.md                     Nguồn và cách chuyển thể
THIRD_PARTY_NOTICES.md            Ghi công và lưu ý phân phối lại
licenses/                         Nguyên văn giấy phép nguồn bên ngoài
scripts/validate.py               Kiểm tra cấu trúc và gói phân phối
```

## Kiểm tra và đóng góp

Cần Python 3.10 trở lên khi chạy kiểm tra phát triển; không cần Python để đọc skill.

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py
```

Nếu đã có Claude Code:

```bash
claude plugin validate .claude-plugin/plugin.json
claude plugin validate .claude-plugin/marketplace.json
```

GitHub Actions chạy kiểm tra ngoại tuyến về metadata, manifest, liên kết nội bộ, tài nguyên độc lập, thông báo giấy phép và một số dấu hiệu tệp riêng tư. Các bước này không chứng minh chất lượng viết, tính đúng của nhận định, khả năng tự phân luồng hay tương thích kết xuất.

Xem [CONTRIBUTING.md](CONTRIBUTING.md) để biết cách đóng góp và đánh giá thay đổi.

## Giấy phép và phạm vi

Phát hành theo [MIT](LICENSE). Khi phân phối riêng một skill, giữ LICENSE.txt của skill đó. Phần chuyển thể từ K-Dense giữ nguyên thông báo MIT của nguồn; xem [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

Cách tổ chức gói lấy cảm hứng từ [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills). Repo này không có quan hệ đại diện hoặc bảo trợ từ hai dự án nguồn.

Bộ skill không áp đặt lĩnh vực, số chương, font, kiểu trích dẫn hay sở thích cũ của một người dùng. Gói không chứa báo cáo thật, thông tin đăng nhập, hook hay MCP server. Việc dùng skill không tự cấp quyền tải dữ liệu lên, công bố, nộp bài, chạy thí nghiệm hoặc sửa nội dung ngoài nhiệm vụ.
