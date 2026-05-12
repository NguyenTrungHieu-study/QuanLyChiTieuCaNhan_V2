# Phần Mềm Quản Lý Chi Tiêu Cá Nhân

## Giới thiệu
Ứng dụng Quản lý Chi tiêu Cá nhân là một giải pháp quản lý tài chính trên desktop toàn diện, được thiết kế theo giao diện dashboard SaaS chuyên nghiệp. Ứng dụng giúp bạn theo dõi thu chi, quản lý danh mục, phân tích dữ liệu tài chính qua các biểu đồ trực quan và dự báo xu hướng chi tiêu trong tương lai nhờ các mô hình phân tích như Moving Average.

## Các tính năng chính
- **Giao diện hiện đại (Modern UI):** Xây dựng trên nền tảng `CustomTkinter` với giao diện Dark Mode, phong cách glassmorphism và bố cục 3 vùng (3-zone layout) responsive. Sử dụng các icon và asset hình ảnh chất lượng cao.
- **Quản lý giao dịch chi tiết:** Theo dõi dòng tiền với đầy đủ thông tin: thời gian chính xác (đến từng phút), số tiền (được format chuẩn VND), danh mục động và ghi chú. Hỗ trợ hiển thị trên bảng dữ liệu (data table) với tính năng phân trang (pagination) và thao tác hàng loạt (bulk actions).
- **Quản lý danh mục động (Dynamic Category Management):** Hỗ trợ người dùng thao tác CRUD (Thêm, Sửa, Xóa) cho danh mục với cơ sở dữ liệu mạnh mẽ, cho phép người dùng tùy biến các loại thu chi của riêng mình.
- **Trực quan hóa dữ liệu (Data Visualization):** Tích hợp `Matplotlib` và `Pandas` cung cấp các biểu đồ tài chính như: biểu đồ tròn (Pie chart) cho phân bổ chi tiêu, và biểu đồ đường (Line chart) để thể hiện biến động tài chính theo thời gian.
- **Dự báo chi tiêu (Forecasting):** Ứng dụng mô hình Moving Average để phân tích xu hướng chi tiêu dựa trên chuỗi thời gian (time-series).
- **Cơ sở dữ liệu tích hợp:** Sử dụng hệ quản trị cơ sở dữ liệu SQLite siêu nhẹ, cục bộ và an toàn.

## Kiến trúc Hệ thống
Dự án được xây dựng với cấu trúc **MVC (Model-View-Controller) kết hợp Service Layer** tiên tiến, giúp code gọn gàng, dễ bảo trì:
- `models/`: Định nghĩa dữ liệu và xử lý các câu truy vấn tới SQLite.
- `views/`: Các module giao diện UI/UX sử dụng `CustomTkinter`.
- `controllers/`: Xử lý sự kiện từ UI và điều phối logic giữa Views, Models và Services.
- `services/`: Nơi chứa các logic nghiệp vụ lõi, phân tích dữ liệu bằng Pandas và xử lý tính toán đồ thị biểu đồ.
- `data/`: Thư mục lưu trữ database SQLite sinh ra trong quá trình chạy chương trình.
- `assets/`: Thư mục chứa hình ảnh icon, tài nguyên dùng cho ứng dụng.

## Hướng dẫn Cài đặt & Sử dụng

### Yêu cầu
- Đã cài đặt Python (phiên bản 3.8+).

### Các bước cài đặt

1. **Điều hướng tới thư mục chứa code**
   ```bash
   cd QuanLyChiTieuCaNhan_V2
   ```

2. **Cài đặt thư viện yêu cầu**
   Mở Command Prompt / Terminal và chạy lệnh sau để tải các packages cần thiết:
   ```bash
   pip install -r requirements.txt
   ```
   *(Bao gồm: `customtkinter`, `pandas`, `matplotlib`)*

3. **Khởi chạy ứng dụng**
   Từ thư mục gốc, gõ lệnh:
   ```bash
   python main.py
   ```

## Tài liệu sử dụng
Đọc thêm tài liệu hướng dẫn chi tiết tại tệp: `huong_dan_su_dung.pdf` trong thư mục chính của project.
