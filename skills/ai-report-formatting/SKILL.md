---
name: ai-report-formatting
description: Chuẩn hóa cách trình bày báo cáo Word/WPS và DOCX/PDF theo mẫu, gồm style, phân cấp mục, bảng, hình, công thức, mục lục và phân trang. Dùng khi tạo bản trình bày hoặc sửa bố cục và khả năng chỉnh sửa; giữ nguyên nội dung khoa học nếu không được giao sửa.
license: MIT
---

# Trình bày và bảo toàn báo cáo

Đầu ra cần đọc rõ, thống nhất, tiếp tục chỉnh sửa được và đã kiểm tra trên bản cuối. Áp dụng thiết kế của mẫu hoặc quy định hiện hành, không lấy một báo cáo cũ làm khuôn bắt buộc cho mọi tài liệu.

## 1. Kiểm kê trước khi sửa

- Xác định nguồn, đầu ra, phạm vi và ứng dụng đích: Word, WPS hoặc PDF. Đuôi DOCX không xác định ứng dụng dùng để nghiệm thu bố cục.
- Đọc quy định, mẫu và các trang đại diện. Ghi các thuộc tính cần theo: khổ giấy, lề, thân bài, cấp tiêu đề, khoảng cách, bảng, chú thích, công thức và số trang.
- Giữ định dạng đã thống nhất khi không có yêu cầu đổi. Với tài liệu mới chưa có mẫu, đề xuất ngắn lựa chọn trình bày thông thường và thực hiện; không gọi lựa chọn đó là chuẩn của trường hoặc cơ quan.
- Phân biệt bảng dữ liệu với bảng căn công thức, bìa và chữ ký. Phân biệt Heading thật với chú thích hoặc dòng mục lục trùng chữ.
- Nếu tệp đang được sửa trực tiếp, kiểm tra phiên tài liệu và thay đổi chưa lưu khi công cụ cho phép. Không ghi đè snapshot cũ lên thay đổi mới.
- Trước thay đổi cấu trúc lớn hoặc thao tác ghi đè, giữ bản sao và dấu kiểm nguồn. Đọc [Bảo toàn DOCX](references/docx-preservation.md) trước khi sửa XML, di chuyển khối hoặc dùng script ghi lại DOCX.

## 2. Chọn công cụ theo định dạng

- Khi tạo hoặc sửa DOCX, dùng skill/công cụ tài liệu chuyên dụng nếu có trong môi trường. Với PDF cần trích xuất hoặc kiểm tra trang, dùng khả năng PDF tương ứng. Không giả định công cụ đã được cài.
- Nếu môi trường cung cấp công cụ nạp runtime/thư viện tài liệu, lấy đường dẫn từ đó; không dùng đường dẫn runtime của một phiên cũ.
- Nếu không có công cụ thao tác tệp, thực hiện phần có thể như nội dung hoặc đặc tả định dạng và nêu giới hạn; không gọi đó là một DOCX đã kiểm tra.

## 3. Dùng cấu trúc có thể chỉnh sửa

- Đặt kiểu chữ, cỡ, căn lề, khoảng cách, thụt đầu dòng và quan hệ Heading bằng style/thuộc tính đoạn. Không căn bằng chuỗi khoảng trắng, Tab hoặc nhiều đoạn rỗng.
- Giữ quan hệ cấp mục theo cấu trúc nội dung. Chỉ đổi số mục theo ánh xạ đã chốt; không tự thêm/bỏ chương để đạt một mẫu thẩm mỹ.
- Sửa định dạng trực tiếp gây xung đột có chọn lọc; giữ đậm/nghiêng có nghĩa, chỉ số, liên kết và ký hiệu. Không ép font thân bài vào công thức.
- Kiểm tra vùng ngoài thân bài: bảng, bìa, textbox, header/footer, chú thích và liên kết. Không áp căn đều hoặc thụt đầu dòng thân bài cho mọi vùng.
- Giữ công thức và bảng ở dạng có thể sửa; không biến chúng thành ảnh để che lỗi bố cục. Với hình, giữ tỷ lệ và đọc thử chữ ở kích thước in.

## 4. Bảng, hình và công thức

- Dùng bảng khi người đọc cần tra giá trị hoặc so sánh; dùng đồ thị khi cần thấy xu hướng. Không tạo minh họa trang trí thay bằng chứng hoặc ảnh nguồn được yêu cầu.
- Lấy thông số cụ thể của bảng mẫu trước khi chuẩn hóa; giữ dữ liệu, đơn vị, ô gộp, công thức và chú thích. Không tự làm tròn số trong tác vụ định dạng.
- Cột vừa vùng in, hàng tự giãn để không cắt chữ; lặp hàng tiêu đề khi bảng qua trang. Giữ các hàng ngắn nguyên vẹn khi phù hợp; không cấm ngắt một hàng cao hơn cả trang.
- Giữ chú thích cùng đối tượng. Với bảng dài, tránh để chỉ còn chú thích và hàng tiêu đề ở cuối trang; giữ thêm ít nhất phần dữ liệu đầu khi bố cục cho phép.
- Giữ ảnh rõ, không méo hoặc crop mất nhãn. Biểu đồ cần trục, đơn vị và chú giải đủ hiểu; kiểm tra phân biệt được khi in theo chế độ người dùng cần.
- Giữ biểu thức toán, dấu, chỉ số và ký hiệu. Thay số phương trình chỉ khi cấu trúc yêu cầu, rồi kiểm tra mọi dẫn chiếu liên quan.

## 5. Mục lục, dẫn chiếu và số trang

- Xác định cơ chế đang có: mục lục tự động, số gõ tay, trường đánh số, dẫn chiếu, dấu trang hoặc công cụ quản lý trích dẫn.
- Mục lục nội dung lấy đúng Heading; danh mục hình/bảng lấy đúng loại chú thích. Không gọi chuỗi số gõ tay hoặc kết quả cache là tự động.
- Với SEQ/REF, kiểm tra định danh và đích dấu trang; cập nhật trường tạo số trước rồi trường dẫn chiếu. Chỉ hướng dẫn Ctrl+A, F9 hai lượt khi phù hợp với cơ chế và ứng dụng đã kiểm tra; xác minh cả trường trong vùng ngoài thân bài nếu có.
- Chốt thứ tự và bố cục trước khi cập nhật. Phân trang thực tế rồi kiểm tra lại tên mục, số dẫn, trang và liên kết. Không dùng số trang ước lượng để hoàn thiện mục lục.
- Kiểm tra section, trang đầu/chẵn/lẻ, liên kết header/footer và quy tắc bắt đầu lại số. Không tự đổi quy ước số La Mã hoặc đánh số bìa.

## 6. Kiểm tra bản bàn giao

Kiểm tra ba lớp theo mức thay đổi:

1. Nội dung: phần ngoài phạm vi còn nguyên; số liệu, công thức, ảnh và dẫn chiếu không mất hoặc đổi ý ngoài dự kiến.
2. Cấu trúc: tệp mở lại được, gói hợp lệ, tài nguyên đủ, Heading đúng, trường và dấu trang có đích, không còn scaffold chưa hoàn thành.
3. Trực quan: render từ chính bản cuối và xem trang ở độ phân giải đọc được. Với thay đổi nhỏ, xem trang ảnh hưởng và ranh giới; với tái cấu trúc hoặc đổi style toàn cục, kiểm tra toàn bộ bố cục.

- Xem kỹ đầu chương, tiêu đề đứng lẻ, bảng bị cắt, chú thích xa đối tượng, khoảng trắng bất thường, công thức, footer và trang chuyển section.
- Dùng đúng ứng dụng đích khi cần khẳng định tương thích. Nếu dùng renderer khác, nói rõ đó là kiểm tra thay thế; không suy từ tên API rằng đã kiểm tra đúng Word/WPS.
- Nếu khả năng tiếp tục chỉnh sửa là yêu cầu bàn giao, thử trên bản sao: sửa nội dung, cập nhật mục lục, lưu và mở lại. Không để dữ liệu thử vào bản cuối.
- Sau thay đổi ảnh hưởng bố cục, render lại phần cần thiết; không dùng PDF cũ làm bằng chứng. ZIP hợp lệ hoặc đủ số trang không thay kiểm tra trực quan.
- Nếu chưa render được, nêu chính xác phần đã và chưa kiểm tra; không chứng nhận tài liệu đã hoàn thiện toàn bộ.

Bàn giao đường dẫn tuyệt đối tới tệp có thật, thay đổi chính, công cụ kiểm tra và giới hạn còn lại. Chỉ đóng instance ứng dụng do tác vụ tạo; không đóng hoặc lưu tài liệu của người dùng để thuận tiện cho automation.
