# 🐂 Điện Thờ Chứng Khoán · Cầu Nguyện Cổ Phiếu Về Bờ & Tím Toàn Sàn

> **Phiên bản Web tương tác trực tiếp lấy cảm hứng từ Chánh Điện Online (`kentjuno/chanh-dien-online`), chuyển đổi sáng tạo thành không gian "Tâm linh tài chính" dành riêng cho cộng đồng chứng sĩ Việt Nam!**

---

## 🌟 Tính Năng Nổi Bật

1. **Bảo Tọa Thần Bò Xanh Tím 2.5D**:
   - Tượng Thần Bò Dát Vàng (The Golden Bull) ngự đài sen ngũ sắc tài lộc, hai mắt rực ánh hào quang sắc tím trần.
   - Bảng điện tử LED VN-INDEX (1,288.66 CE) phát sáng hào quang phía sau.
   - Hoành phi **"VẠN LỆNH TÍM TRẦN"** & Đôi câu đối đỏ thếp vàng chuẩn phong thủy:
     - Vế trái: *TÂM THÀNH KHẤN NGUYỆN TÍM TOÀN SÀN*
     - Vế phải: *LÁI KÉO TRẦN TÀU CHỞ VỀ BỜ*
   - Hiệu ứng khói nhang tím/vàng huyền ảo bay lượn trên nền Canvas.

2. **Gõ Mõ Xả Margin (Interactive Digital Wooden Fish)**:
   - Click chuột, chạm màn hình hoặc bấm phím `Space` để gõ mõ.
   - Tích hợp **Web Audio API** tạo tiếng gõ mõ `Cốc... Cốc...` chân thực, không phụ thuộc file âm thanh bên ngoài.
   - Hạt hiệu ứng chữ bay lên ngẫu nhiên: `+1 Cây Trần 🟣`, `Về Bờ +7% 🟢`, `Tây Ngừng Xả 💸`, `Cụ Lái Kéo Tàu 🚀`, `Không Bị Úp Bô 🛡️`, `Xóa Margin Call 🧘‍♂️`...
   - Tự động nhảy số bộ đếm: Công đức cá nhân & Tổng công đức ba sàn.

3. **Dâng Sớ Cầu Trần & Đọc Sớ Bằng Giọng AI**:
   - Nhập pháp danh, chọn mã cổ phiếu (`HPG`, `DIG`, `SSI`, `NVL`, `FPT`, `VIX`...), giá vốn kẹp đỉnh.
   - Chọn lễ phẩm: Nải Chuối Xanh, Nhang Tím Trần, Bò Vàng Dát Vàng, Thỉnh Đại Chung.
   - **Trình soạn sớ tự động**: 1 click để sinh các bài sớ chứng khoán siêu hài hước.
   - Khi dâng sớ:
     - Chuông chùa ngân vang `BOOONNNGGG...` kết hợp tiếng `Ting Ting` khớp lệnh.
     - Trình duyệt tự động đọc lời sớ bằng giọng đọc tiếng Việt trầm bổng (SpeechSynthesis).
     - Cắm thêm 1 nén nhang mới mang tên mã cổ phiếu vào Bát Hương trên bàn thờ.
     - Xuất hiện **Lá Sớ Vàng Thư Pháp** để lưu hoặc copy khoe bạn bè trên Facebook/Zalo/Threads.

4. **Đồng Bộ Thời Gian Thực (Real-time WebSockets)**:
   - Khi bất kỳ ai vào web dâng sớ hay gõ mõ, tất cả người khác đang mở web đều nhìn thấy feed cập nhật, nén nhang mới cắm vào bàn thờ và bảng xếp hạng nhảy số ngay lập tức.

5. **Bảng Xếp Hạng Kêu Cứu & Bảng Vàng Chứng Sĩ**:
   - Top 5 siêu cổ được thắp nhang nhiều nhất hôm nay.
   - Top đại gia chứng sĩ tích đức công đức nhiều nhất.

---

## 🚀 Hướng Dẫn Chạy

### Cách 1: Chạy Full Server Node.js + WebSocket Realtime (Khuyên dùng)

Yêu cầu máy đã cài Node.js (v18 trở lên).

```bash
# 1. Cài đặt thư viện websocket
npm install

# 2. Khởi động server
npm start
```

👉 Mở trình duyệt truy cập: **`http://localhost:3000`**

### Cách 2: Chạy Web Tĩnh độc lập (Không cần server)
- Bạn chỉ cần nhấp đúp trực tiếp vào file **`index.html`** để mở trên bất kỳ trình duyệt nào (Chrome, Edge, Safari, Firefox).
- Mọi âm thanh (tiếng mõ, tiếng chuông, tiếng khớp lệnh, giọng đọc sớ tiếng Việt), hình ảnh đồ họa và hiệu ứng nhang khói đều tự hoạt động 100% độc lập!

---

## 🌐 Triển Khai Lên Mạng (Deploy Online)

- **Cloudflare Pages / GitHub Pages / Vercel**: Bạn chỉ cần upload thư mục chứa file `index.html`.
- **Render / Railway / VPS**: Chạy lệnh `npm start` để có đầy đủ cả WebSocket đồng bộ nhiều người xem cùng lúc.

---

## 🔮 Lộ Trình Mở Rộng Sang TikTok Live / OBS (Sau này)

Cấu trúc mã nguồn đã được module hóa sẵn sàng theo phong cách của Kent Juno:
- Sau này nếu muốn mở phiên **Livestream TikTok**: bạn chỉ cần thêm thư viện `tiktok-live-connector` vào `server.mjs`, khi viewer comment mã cổ phiếu trên live chat, server chỉ cần gọi hàm `broadcast({ type: 'PRAY', ... })` là màn hình livestream sẽ tự thắp nhang và đọc sớ theo thời gian thực!
