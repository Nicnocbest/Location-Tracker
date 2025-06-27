# 🚀 DEPLOY LÊN PYTHONANYWHERE - MIỄN PHÍ HOÀN TOÀN

## Bước 1: Tạo tài khoản PythonAnywhere (1 phút)
1. Truy cập: **https://www.pythonanywhere.com**
2. Click **"Pricing & signup"** → **"Create a Beginner account"**
3. Điền thông tin và verify email

## Bước 2: Upload code (2 phút)
1. **Mở Dashboard** → **"Files"**
2. **Upload** tất cả files trong thư mục `location-tracker/`
3. Hoặc clone từ GitHub:
```bash
git clone https://github.com/HieuNguyen267/Location.git
```

## Bước 3: Cài đặt dependencies (1 phút)
1. **Mở Console** → **"Bash"**
2. **Chạy lệnh:**
```bash
cd Location
pip3.10 install --user -r requirements.txt
```

## Bước 4: Tạo Web App (2 phút)
1. **Dashboard** → **"Web"** → **"Add a new web app"**
2. **Chọn domain:** `yourusername.pythonanywhere.com`
3. **Python version:** 3.10
4. **Framework:** Manual configuration

## Bước 5: Cấu hình WSGI (2 phút)
1. **Edit WSGI file** (`/var/www/yourusername_pythonanywhere_com_wsgi.py`):
```python
import sys
import os

# Add your project directory to sys.path
path = '/home/yourusername/Location'
if path not in sys.path:
    sys.path.append(path)

from app import app as application

# Set environment variables
os.environ['GOOGLE_MAPS_API_KEY'] = 'AIzaSyDNI_ZWPqvdS6r6gPVO50I4TlYkfkZdXh8'
os.environ['SECRET_KEY'] = 'location-tracker-production-secret-2024'
os.environ['DATABASE_URL'] = 'sqlite:////home/yourusername/Location/location_tracker.db'

if __name__ == "__main__":
    application.run()
```

## Bước 6: Reload và Test (1 phút)
1. **Click "Reload"** trong Web tab
2. **Truy cập:** `https://yourusername.pythonanywhere.com`
3. **Test tạo link** và thu thập GPS

---

## 🎯 **HOẶC DEPLOY NHANH VỚI VERCEL**

### Vercel (Miễn phí, nhanh nhất)
```bash
npm install -g vercel
vercel login
vercel --prod
```

### Environment Variables cho Vercel:
```bash
vercel env add GOOGLE_MAPS_API_KEY
vercel env add SECRET_KEY
vercel env add DATABASE_URL
```

---

## 🔥 **HOẶC SỬ DỤNG NGROK ĐỂ SHARE LOCAL**

### Ngrok (Nhanh nhất để test):
```bash
# Cài đặt ngrok
npm install -g ngrok

# Chạy app local
python app.py

# Mở terminal mới
ngrok http 5000
```

**Sẽ có URL như:** `https://abc123.ngrok.io`

---

**Bạn muốn thử platform nào?**
- ✅ **PythonAnywhere** (Miễn phí, dễ nhất)
- ✅ **Vercel** (Nhanh nhất)  
- ✅ **Ngrok** (Test ngay local)
- ✅ **Heroku** (Cần thẻ tín dụng)
- ✅ **Render** (Miễn phí có giới hạn) 