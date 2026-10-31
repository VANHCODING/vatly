# Vật lý đại cương 1

Bản website mới để đưa trực tiếp lên GitHub Pages: 17 chương, 98 mục công thức/lập luận và 204 bài tập tính toán.

## Các tệp cần đưa lên GitHub

```text
index.html
vendor/
  katex/
README.md
.gitignore
.nojekyll
```

`index.html` chứa toàn bộ bài giảng, dữ liệu bài tập, CSS và JavaScript. `vendor/katex/` chứa bộ hiển thị công thức, font và giấy phép MIT; giữ nguyên cấu trúc thư mục này.

## Đưa lên GitHub Pages

1. Tạo repository trên GitHub.
2. Upload các tệp và toàn bộ thư mục `vendor/` vào thư mục gốc của repository; không đặt bên trong một thư mục dự án khác.
3. Vào **Settings → Pages**.
4. Chọn **Deploy from a branch**, chọn nhánh chứa các tệp (thường là `main`) và thư mục **/ (root)**, rồi **Save**.
5. Chờ GitHub triển khai và mở đường dẫn được hiển thị ở trang Pages.

Hướng dẫn chính thức: [Cấu hình nguồn xuất bản GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

Website tĩnh, không cần cài thư viện, chạy Python hay cấu hình bước build. Các tệp dựng trang, bản trùng, kiểm thử và tệp tạm đã được loại khỏi bộ này. Chỉnh sửa nội dung hoặc giao diện trực tiếp trong `index.html`.

## Sử dụng

Có thể mở `index.html` trực tiếp bằng trình duyệt. Công thức dùng thư viện cục bộ; phông chữ Google Fonts là tùy chọn và có phông hệ thống dự phòng. Tiến độ, ghi chú và bài đã lưu nằm trong trình duyệt; dùng tính năng sao lưu JSON để chuyển thiết bị.

Tài liệu bao gồm cơ học, dao động–sóng, nhiệt học và tương đối hẹp nhập môn. Đây là tài liệu biên soạn độc lập; phạm vi cần đối chiếu đề cương học phần của từng trường. Điểm tự động đánh giá đáp số; phần lập luận có tiêu chí tự đánh giá riêng.
