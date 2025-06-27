# Location Tracker - Link Rút Gọn với Thu Thập Vị Trí

Ứng dụng web cho phép tạo link rút gọn và thu thập vị trí GPS của người dùng khi họ click vào link.

## 🌟 Tính năng

- ✅ Tạo link rút gọn dễ nhớ
- 📍 Thu thập vị trí GPS chính xác
- 🗺️ Hiển thị vị trí trên Google Maps  
- 📊 Dashboard quản lý link và thống kê
- 📱 Responsive design, tương thích mobile
- 🔒 Bảo mật dữ liệu người dùng

## 🚀 Cài đặt và Chạy Local

### Yêu cầu
- Python 3.8+
- Google Maps API Key

### Cài đặt

1. Clone repository:
```bash
git clone <your-repo-url>
cd location-tracker
```

2. Tạo virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
```

3. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

4. Tạo file .env từ env_example.txt:
```bash
copy env_example.txt .env  # Windows
# cp env_example.txt .env  # Linux/Mac
```

5. Chỉnh sửa file .env:
```env
GOOGLE_MAPS_API_KEY=your_actual_api_key_here
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///location_tracker.db
PORT=5000
```

6. Chạy ứng dụng:
```bash
python app.py
```

Truy cập: http://localhost:5000

## 🌐 Deploy lên Railway

### Bước 1: Chuẩn bị
1. Tạo tài khoản tại [railway.app](https://railway.app)
2. Cài đặt Railway CLI hoặc dùng GitHub integration

### Bước 2: Deploy
1. Push code lên GitHub repository
2. Kết nối Railway với GitHub repo
3. Tạo project mới trên Railway
4. Thêm environment variables:
   - `GOOGLE_MAPS_API_KEY`: API key của Google Maps
   - `SECRET_KEY`: Chuỗi bí mật cho Flask
   - `DATABASE_URL`: Railway sẽ tự động tạo PostgreSQL

### Bước 3: Lấy Google Maps API Key
1. Truy cập [Google Cloud Console](https://console.cloud.google.com/)
2. Tạo project mới hoặc chọn project hiện có
3. Bật Google Maps JavaScript API
4. Tạo API Key và thêm domain restrictions
5. Copy API Key vào Railway environment variables

## 📖 Cách sử dụng

### 1. Tạo link rút gọn
- Truy cập trang chủ
- Nhập tiêu đề, URL gốc và mô tả
- Click "Tạo Link Rút Gọn"
- Copy link được tạo

### 2. Chia sẻ link
- Gửi link rút gọn cho người khác qua:
  - Tin nhắn SMS
  - Email
  - Social media
  - QR code

### 3. Theo dõi vị trí
- Khi người dùng click vào link:
  - Trình duyệt sẽ yêu cầu quyền truy cập vị trí
  - Ứng dụng thu thập tọa độ GPS
  - Người dùng được chuyển hướng đến URL gốc
- Xem thống kê tại Dashboard

### 4. Xem báo cáo
- Truy cập Dashboard để xem:
  - Danh sách tất cả link đã tạo
  - Số lượt click cho mỗi link
  - Chi tiết vị trí trên bản đồ
  - Thời gian và độ chính xác GPS

## 🔧 API Endpoints

- `GET /` - Trang chủ
- `GET /dashboard` - Dashboard quản lý
- `POST /create` - Tạo link mới
- `GET /l/<short_code>` - Chuyển hướng và thu thập vị trí
- `POST /api/location` - Lưu dữ liệu vị trí
- `GET /link/<id>` - Chi tiết link và bản đồ

## ⚠️ Lưu ý quan trọng

### Pháp lý
- Chỉ sử dụng cho mục đích hợp pháp
- Cần thông báo rõ ràng cho người dùng về việc thu thập vị trí
- Tuân thủ GDPR và các quy định bảo vệ dữ liệu cá nhân

### Bảo mật
- Không lưu trữ thông tin nhạy cảm trong database
- Sử dụng HTTPS trong production
- Hạn chế quyền truy cập database

### Sử dụng đạo đức
- Chỉ thu thập vị trí khi người dùng đồng ý
- Có chính sách bảo mật rõ ràng
- Cung cấp tùy chọn opt-out

## 🛠️ Công nghệ sử dụng

- **Backend**: Flask, SQLAlchemy
- **Frontend**: Bootstrap 5, jQuery, HTML5 Geolocation
- **Database**: SQLite (local), PostgreSQL (production)
- **Maps**: Google Maps JavaScript API
- **Deployment**: Railway

## 📄 License

MIT License - Xem file LICENSE để biết thêm chi tiết.

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón! Hãy:
1. Fork project
2. Tạo feature branch
3. Commit changes
4. Push to branch  
5. Tạo Pull Request

## 📞 Hỗ trợ

Nếu gặp vấn đề, hãy tạo issue trên GitHub hoặc liên hệ qua email.

---

⭐ **Nếu project hữu ích, hãy cho một star nhé!** ⭐ 