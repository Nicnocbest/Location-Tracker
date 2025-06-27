# Hướng dẫn Deploy Location Tracker lên Railway

## Bước 1: Chuẩn bị Google Maps API

### 1.1 Tạo Google Cloud Project
1. Truy cập [Google Cloud Console](https://console.cloud.google.com/)
2. Tạo project mới hoặc chọn project hiện có
3. Bật billing cho project (cần thẻ tín dụng)

### 1.2 Bật APIs cần thiết
1. Truy cập "APIs & Services" > "Library"
2. Tìm và bật các APIs sau:
   - Maps JavaScript API
   - Geocoding API (tùy chọn)
   - Places API (tùy chọn)

### 1.3 Tạo API Key
1. Truy cập "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "API Key"
3. Copy API key được tạo
4. Click "Restrict Key" để cấu hình bảo mật:
   - Application restrictions: HTTP referrers
   - Website restrictions: Thêm domain của Railway app
   - API restrictions: Chọn Maps JavaScript API

## Bước 2: Deploy lên Railway

### 2.1 Chuẩn bị Repository
1. Tạo GitHub repository mới
2. Push code lên GitHub:
```bash
git init
git add .
git commit -m "Initial commit: Location Tracker app"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

### 2.2 Deploy trên Railway
1. Truy cập [railway.app](https://railway.app)
2. Đăng nhập bằng GitHub
3. Click "New Project" > "Deploy from GitHub repo"
4. Chọn repository `location-tracker`
5. Railway sẽ tự động detect và deploy

### 2.3 Cấu hình Environment Variables
Trong Railway dashboard, thêm các biến môi trường:

```env
GOOGLE_MAPS_API_KEY=your_actual_api_key_here
SECRET_KEY=your-super-secret-key-for-production
DATABASE_URL=postgresql://username:password@host:port/database
PORT=5000
```

**Lưu ý**: Railway sẽ tự động tạo PostgreSQL database và thiết lập DATABASE_URL

### 2.4 Cập nhật API Key Restrictions
1. Quay lại Google Cloud Console
2. Update API Key restrictions:
   - Thêm domain Railway: `*.railway.app`
   - Thêm domain custom nếu có

## Bước 3: Test và Verify

### 3.1 Kiểm tra Deployment
1. Truy cập URL Railway app
2. Test tạo link mới
3. Test chia sẻ link và thu thập vị trí
4. Kiểm tra dashboard và bản đồ

### 3.2 Debug nếu có lỗi
- Xem logs trong Railway dashboard
- Kiểm tra environment variables
- Verify API key và domain restrictions

## Bước 4: Tùy chọn Custom Domain

### 4.1 Setup Custom Domain
1. Trong Railway project settings
2. Thêm custom domain
3. Cấu hình DNS records

### 4.2 Cập nhật API Restrictions
- Thêm custom domain vào Google Maps API restrictions

## Bước 5: Monitoring và Maintenance

### 5.1 Theo dõi Usage
- Google Cloud Console: Monitor API usage
- Railway: Monitor app performance và database

### 5.2 Backup Database
- Railway cung cấp automatic backups
- Có thể export data manually nếu cần

## Lỗi thường gặp và cách fix

### 1. "For development purposes only" trên bản đồ
**Nguyên nhân**: API key chưa được restrict đúng cách hoặc billing chưa được bật
**Giải pháp**: 
- Bật billing cho Google Cloud project
- Cấu hình API key restrictions đúng domain

### 2. Database connection error
**Nguyên nhân**: DATABASE_URL không đúng
**Giải pháp**: 
- Kiểm tra Railway PostgreSQL addon
- Verify DATABASE_URL trong environment variables

### 3. Location permission denied
**Nguyên nhân**: HTTPS required cho geolocation
**Giải pháp**: 
- Railway tự động cung cấp HTTPS
- Đảm bảo user grant permission

### 4. API key quota exceeded
**Nguyên nhân**: Vượt quá limit miễn phí
**Giải pháp**: 
- Upgrade Google Cloud billing plan
- Optimize API calls

## Cost Estimation

### Google Maps API (Monthly)
- Free tier: 28,000 map loads
- Sau đó: $7/1000 map loads
- Ước tính: $0-50/tháng tùy traffic

### Railway Hosting
- Free tier: 500 hours/tháng
- Pro plan: $5/tháng unlimited
- Database: Bao gồm trong plan

## Security Best Practices

1. **API Key Security**:
   - Luôn restrict API key theo domain
   - Không commit API key vào code
   - Regular rotate API keys

2. **Database Security**:
   - Use environment variables cho credentials
   - Regular backup data
   - Monitor unusual access patterns

3. **User Privacy**:
   - Inform users về location tracking
   - Provide opt-out options
   - Comply with GDPR/privacy laws

---

🎉 **Chúc mừng! Ứng dụng Location Tracker đã sẵn sàng để sử dụng!**

Nếu gặp vấn đề, hãy check Railway logs hoặc tạo issue trên GitHub. 