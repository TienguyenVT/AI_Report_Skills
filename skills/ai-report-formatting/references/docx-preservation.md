# Bảo toàn DOCX khi chỉnh bằng script

Chỉ cần đọc phần này khi thao tác OOXML, thay đổi cấu trúc hoặc ghi lại DOCX bằng thư viện/automation. Không bắt một sửa chính tả đơn giản thực hiện toàn bộ kiểm kê.

## Nguồn và ghi tệp

- Ghi đường dẫn, thời điểm và SHA-256 nguồn trước thay đổi lớn; làm trên bản sao ổn định.
- Trước khi thay thế nguồn đã được phép ghi đè, đối chiếu lại dấu kiểm. Nếu nguồn thay đổi, giữ cả bản mới và bản làm việc, đối chiếu trước khi tích hợp.
- Kiểm tra writer kết thúc và mã thoát; mở lại đúng đầu ra đã ghi. Một PDF cũ còn tồn tại không chứng minh lần tạo DOCX mới thành công.
- Chỉ đóng document/instance đã tạo. Không kết thúc toàn bộ WINWORD hoặc WPS để giải quyết khóa tệp.

## Nội dung phức tạp

- Không gán lại paragraph.text hoặc cell.text khi có công thức, field, bookmark, hyperlink, drawing hay định dạng cần giữ. Thay đúng nút văn bản hoặc thuộc tính cần sửa.
- Không đi vào nút toán học khi chỉ sửa văn bản dẫn chiếu. Giữ xml:space="preserve" ở nút có khoảng trắng đầu/cuối; kiểm tra chữ dính sau khi tách run.
- Khi bọc XML bằng python-docx, dùng đối tượng cha có part như doc._body, không dùng trực tiếp CT_Body cho thao tác cần style.
- Tìm điểm neo bằng loại phần tử, Heading, nội dung và vị trí; xác nhận duy nhất. Không chọn nhầm dòng mục lục có cùng tên với tiêu đề.
- Khi di chuyển khối, xác minh điểm bắt đầu < điểm kết thúc và điểm chèn nằm ngoài khối. Sau di chuyển, kiểm tra thứ tự cùng mọi hình, bảng, công thức và dấu trang đi kèm.
- Đổi số chương theo ánh xạ gốc hoặc theo vùng; tránh thay nối tiếp khiến cùng số bị tăng hai lần.

## Style, bảng và trường

- Kiểm tra style kế thừa, linked style, định dạng trực tiếp và theme. Giá trị font.name không chứng minh mọi vùng ký tự dùng cùng font.
- Với bảng, kiểm tra tblPr, tcPr, tblPrEx và table style. Màu/viền ở cấp hàng có thể còn ghi đè dù đã đổi thuộc tính bảng.
- Với danh sách cần chỉnh sửa tiếp, dùng numbering thực; kiểm tra numbering part/relationship trước khi gán numPr.
- Dùng parser theo namespace để kiểm tra OMML và revisions. Đếm m:oMath riêng với m:oMathPara; không tìm tiền tố chuỗi có thể đếm nhầm w:instrText thành w:ins.
- So sánh công thức bằng nội dung hoặc XML chuẩn hóa, không chỉ số lượng. Khi có thay đổi chủ đích, ghi ngoại lệ theo vị trí và so phần còn lại.
- Dẫn chiếu có thể được lưu bằng field HYPERLINK/PAGEREF thay vì phần tử w:hyperlink. Kiểm tra cả field code, kết quả và bookmark đích.
- Giữ bookmark start/end theo cặp và ID duy nhất. Không thay trường lỗi bằng số gõ tay chỉ để mất thông báo.
- Với danh mục hình/bảng, khớp identifier SEQ thật với TOC; không suy identifier từ nhãn hiển thị.

## So sánh và render

- Chọn bất biến theo phạm vi: sửa footer thì thân bài và biểu thức toán phải giữ; viết lại chương thì chỉ phần được phép đổi. Tổng đếm của phiên cũ không phải chuẩn bất biến cho mọi bản sau.
- So sánh văn bản, biểu thức toán, cấu trúc bảng, media, liên kết và comments/revisions theo mức rủi ro. Khác hash cả DOCX chưa chứng minh nội dung khác vì metadata ZIP có thể đổi.
- Nếu chỉ lấy số trang hoặc xuất PDF qua Word/WPS, ưu tiên mở chỉ đọc và đóng không lưu. Nếu phải lưu để cập nhật trường, làm trên bản làm việc rồi đối chiếu trước/sau.
- Nhận diện ứng dụng thực tế bằng phiên/executable và thông tin xuất khi cần. ProgID hoặc chuỗi version tương thích không đủ chứng minh đúng renderer.
- PDF/ảnh QA phải gắn với bản DOCX cuối. Đợi tiến trình kết thúc và xác minh ảnh giải mã được; xem ảnh thực tế, không chỉ tạo đường dẫn.
- Nếu công cụ thiếu dependency, kiểm tra runtime đang dùng trước khi cài thêm hoặc đổi đường xử lý. Khi gặp lỗi sau thao tác ghi, xác minh tệp đã tạo trước khi chạy lại.
- Giữ tệp QA riêng; chỉ dọn tệp do tác vụ tạo, sau khi xác nhận đường dẫn nằm trong phạm vi dự kiến.
