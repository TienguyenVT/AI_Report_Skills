# AI Report Skills

Ba skill chuyên biệt giúp AI viết, kiểm chứng và trình bày báo cáo.

[English](README.md) | **Tiếng Việt**

Bộ hướng dẫn dùng cho báo cáo học thuật, kỹ thuật và công việc. Nội dung skill viết bằng tiếng Việt và tôn trọng ngôn ngữ, mẫu trình bày, phạm vi nguồn của từng báo cáo.

## Bộ skill giải quyết việc gì?

AI có thể viết trôi chảy nhưng đổi ý nghĩa, thêm nguồn không có thật, so sánh số liệu khác điều kiện hoặc làm mất cấu trúc DOCX. Bộ này chia trách nhiệm để AI dùng đúng hướng dẫn theo việc được giao.

| Skill | Vai trò |
| --- | --- |
| [ai-report-writing](skills/ai-report-writing/SKILL.md) | Lập dàn ý, viết, biên tập, tổ chức lập luận, thống nhất thuật ngữ và giảm lặp. |
| [ai-report-evidence](skills/ai-report-evidence/SKILL.md) | Đối chiếu số liệu, nhận định, điều kiện thí nghiệm, phép so sánh và nguồn trích dẫn. |
| [ai-report-formatting](skills/ai-report-formatting/SKILL.md) | Chuẩn hóa Word/WPS, bảng, hình, công thức, mục lục, số trang và kiểm tra bản kết xuất. |

[Rule điều phối](rules/REPORT_SKILL_ROUTING.md) chọn skill theo yêu cầu. Sửa chính tả chỉ dùng phần cần thiết; làm báo cáo hoàn chỉnh mới phối hợp cả ba theo từng giai đoạn.

## Cài đặt

Cài trực tiếp từ [TienguyenVT/AI_Report_Skills](https://github.com/TienguyenVT/AI_Report_Skills), hoặc clone để dùng bản local:

```bash
git clone https://github.com/TienguyenVT/AI_Report_Skills.git
cd AI_Report_Skills
```

### Claude Code

Trong phiên Claude Code:

```text
/plugin marketplace add TienguyenVT/AI_Report_Skills
/plugin install ai-report-skills@ai-report-skills
```

Plugin cung cấp ba skill qua manifest trong .claude-plugin/. Chọn skill từ danh sách của ứng dụng hoặc gọi bằng tên; tên hiển thị có thể kèm namespace của plugin.

Muốn điều phối ở cấp dự án, ghép [rule](rules/REPORT_SKILL_ROUTING.md) vào CLAUDE.md của dự án sử dụng. Cài plugin không tự chép CLAUDE.md ở gốc repository này vào các dự án khác. Validator Claude có cảnh báo về giới hạn này; tệp vẫn hữu ích khi làm việc ngay trong repository.

### Codex

Chép đầy đủ các thư mục skill cần dùng trong skills/ vào một nơi:

| Phạm vi | Thư mục |
| --- | --- |
| Riêng dự án | .agents/skills/ trong dự án đó |
| Dùng cá nhân | ~/.agents/skills/ |

Giữ cả references và agents nếu có. Bảo toàn bản đã cài và tránh tạo hai bản trùng tên ở nhiều vị trí. Ghép rule điều phối vào AGENTS.md của dự án cần dùng.

Trong Codex CLI hoặc IDE extension:

```text
$ai-report-writing Viết lại mục này cho mạch lạc, giữ nguyên ý và số liệu.
```

Ngoài ra có [manifest plugin](plugin.json) và [catalog Codex](.agents/plugins/marketplace.json). Với client hỗ trợ marketplace local, có thể dùng cách cài plugin thay cho chép skill:

```bash
codex plugin marketplace add TienguyenVT/AI_Report_Skills
```

Sau đó cài từ marketplace tương ứng trong giao diện plugin desktop. Không cần dùng đồng thời hai cách.

Đối chiếu [hướng dẫn skill chính thức](https://developers.openai.com/codex/skills/) và [hướng dẫn plugin chính thức](https://developers.openai.com/plugins/build/plugins). Nạp lại hoặc khởi động lại ứng dụng nếu skill mới chưa xuất hiện.

### Cursor hoặc agent khác

Repository có [rule Cursor](.cursor/rules/report-skills.mdc) dành cho tác vụ báo cáo, không bật cho mọi yêu cầu.

Khi chuyển sang dự án khác, chép cả rule Cursor, rules/REPORT_SKILL_ROUTING.md và thư mục skills/, giữ nguyên đường dẫn tương đối hoặc sửa cho khớp nơi đã cài.

Với agent khác, yêu cầu đọc rule và SKILL.md cần dùng. Khả năng tự chọn skill phụ thuộc ứng dụng; bộ hướng dẫn không tự cài công cụ.

## Ví dụ giao việc

```text
Dùng ai-report-writing sắp xếp lại chương này theo dàn ý đã duyệt,
giữ đầy đủ công thức, bảng, hình và số liệu.

Dùng ai-report-evidence kiểm tra kết luận theo tài liệu đính kèm.
Chỉ nêu chỗ sai hoặc thiếu bằng chứng, chưa sửa bản báo cáo.

Dùng ai-report-formatting chuẩn hóa bảng theo mẫu trong WPS.
Giữ nguyên dữ liệu và kiểm tra bố cục bản cuối.
```

[Xem thêm tình huống và tiêu chí kiểm tra](EXAMPLES.md). Đây là tiêu chí để thử hành vi, không phải kết quả nghiệm thu mọi tích hợp hoặc chất lượng biên tập.

## Kiểm tra và phát triển

Đọc skill không cần Python. Các kiểm tra dành cho người duy trì cần Python từ 3.10:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s tests
```

Nếu đã cài Claude Code:

```bash
claude plugin validate .claude-plugin/plugin.json
claude plugin validate .claude-plugin/marketplace.json
```

GitHub Actions chạy kiểm tra metadata, manifest, đường dẫn, liên kết Markdown và một số dấu hiệu tệp riêng tư. Kiểm tra này không chứng minh tính đúng khoa học, chất lượng viết, khả năng tự chọn skill hoặc bố cục Word/WPS.

## Giới hạn và giấy phép

Bộ này cung cấp hướng dẫn, không cung cấp trình render hoặc cơ sở dữ liệu bằng chứng. Sửa DOCX/PDF thực tế cần công cụ phù hợp.

Mẫu, số chương, font, kiểu bảng và nguồn được phép do từng báo cáo quyết định. Skill không cấp quyền tự gửi dữ liệu, công bố, nộp bài hoặc tạo số liệu. Gói không chứa hook, MCP server, khóa truy cập hoặc dữ liệu báo cáo.

Xem [hướng dẫn đóng góp](CONTRIBUTING.md) và [giấy phép MIT](LICENSE).

Cách tổ chức tham khảo [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills); nội dung hướng dẫn báo cáo được biên soạn riêng từ kinh nghiệm biên tập. Dự án không có quan hệ bảo trợ hoặc liên kết chính thức với repository đó.
