# Gelişmiş Aktivite Loglama Sistemi - Kullanım Kılavuzu

## 🎯 Özellikler

Sistem artık tüm kullanıcı aktivitelerini detaylı bir şekilde izliyor ve raporluyor:

### Otomatik Loglanan Aktiviteler:
1. **Sayfa Ziyaretleri** - Hangi kullanıcı hangi sayfayı ziyaret etti
2. **Buton Tıklamaları** - Her buton etkileşimi
3. **Veri Yüklemeleri** - Yüklenen dosyalar ve kayıt sayıları
4. **Export İşlemleri** - Excel/PDF/Word çıktıları
5. **Email Gönderileri** - Kime, ne zaman gönderildi
6. **Analiz İşlemleri** - Hangi analizler yapıldı
7. **Hatalar** - Tüm sistem hataları
8. **Oturum Bilgileri** - Başlangıç/bitiş zamanları

## 📧 Otomatik Email Raporları

### Zamanlanmış Gönderimler:
- **Her gün saat 16:00'da**: Günlük detaylı aktivite raporu
- **Her 4 saatte bir**: Periyodik durum raporu

### Rapor İçeriği:
```
📊 Genel İstatistikler
├─ Toplam aktivite sayısı
├─ Ziyaret edilen sayfa sayısı
├─ Toplam sayfa tıklamaları
├─ Export işlem sayısı
├─ Gönderilen mail sayısı
└─ Hata sayısı

🖱️ Sayfa Ziyaret İstatistikleri
├─ Her sayfa için tıklama sayısı
└─ Yüzdelik dağılım

📂 Veri Yükleme İşlemleri
├─ Yüklenen dosyalar
├─ Kayıt sayıları
└─ Zaman damgaları

💾 Export İşlemleri
├─ Export türleri
├─ Dosya adları
└─ İşlem zamanları

📧 Email Gönderim İşlemleri
├─ Alıcılar
├─ Konular
└─ Gönderim zamanları

⚠️ Hata Kayıtları
├─ Hata mesajları
├─ Hangi sayfada oluştu
└─ Zaman bilgileri
```

## 📁 Log Dosyaları

### Oluşturulan Dosyalar:
1. **`activity_logs_YYYY-MM-DD.json`** - Günlük JSON formatında aktivite logu
2. **`system_log_YYYY-MM-DD.log`** - Sistem log dosyası (teknik detaylar)

### JSON Log Yapısı:
```json
{
  "timestamp": "2026-01-15 14:30:45",
  "user": "ozan.sabudak",
  "machine": "DESKTOP-ABC123",
  "event_type": "PAGE_VISIT",
  "page": "Yönetim Paneli",
  "details": "Sayfa açıldı: Yönetim Paneli"
}
```

### Event Tipleri:
- `SESSION_START` - Oturum başladı
- `SESSION_END` - Oturum bitti
- `APP_START` - Uygulama başlatıldı
- `APP_CLOSE` - Uygulama kapatıldı
- `PAGE_VISIT` - Sayfa ziyareti
- `BUTTON_CLICK` - Buton tıklaması
- `DATA_LOAD` - Veri yükleme
- `EXPORT` - Export işlemi
- `EMAIL_SENT` - Email gönderimi
- `EMAIL_SUCCESS` - Email başarılı
- `ANALYSIS` - Analiz işlemi
- `ERROR` - Hata oluştu

## 🔍 Manuel Loglama (Geliştiriciler için)

Kendi kodunuzda loglama eklemek isterseniz:

```python
# Sayfa ziyareti
activity_logger.log_page_visit("Özel Sayfa")

# Buton tıklama
activity_logger.log_button_click("Özel Buton", "Özel Sayfa")

# Veri yükleme
activity_logger.log_data_load("dosya.xlsx", 1000, "Veri Yükleme")

# Export
activity_logger.log_export("EXCEL", "rapor.xlsx", "Raporlar")

# Email
activity_logger.log_email_sent("user@example.com", "Rapor Konusu", "Mail Merkezi")

# Analiz
activity_logger.log_analysis("PERFORMANS", "Detay bilgi", "Analiz")

# Hata
activity_logger.log_error("Hata mesajı", "Problem Sayfası")

# Genel event
activity_logger.log_event("CUSTOM_EVENT", "Detay açıklama", "Sayfa")
```

## 📊 Rapor Örnekleri

### 1. HTML Email Raporu
Profesyonel tasarımlı, renkli, grafikli email raporu:
- Modern gradient tasarım
- Responsive layout
- İstatistik kartları
- Detaylı tablolar
- Otomatik JSON dosya eki

### 2. JSON Log Dosyası
Programatik erişim için machine-readable format:
- Her aktivite ayrı JSON objesi
- Zaman damgalı
- Kullanıcı ve makine bilgili
- Kolay parse edilebilir

### 3. System Log Dosyası
Teknik detaylar ve debug için:
- Timestamp'li entries
- Log level (INFO, ERROR)
- Detaylı hata mesajları

## ⚙️ Konfigürasyon

### Email Ayarları (birlesik_kod.py):
```python
GMAIL_USER = "your-email@defacto.com"
GMAIL_APP_PASSWORD = "your-app-password"
GMAIL_RECEIVER_LOGS = "admin@defacto.com"  # Log alacak email
```

### Zamanlanmış Görevler:
```python
# Günlük rapor (16:00)
schedule.every().day.at("16:00").do(activity_logger.send_daily_report_email)

# Periyodik rapor (her 4 saatte)
schedule.every(4).hours.do(activity_logger.send_daily_report_email)
```

Zamanlama değiştirmek için:
```python
# Her gün 09:00
schedule.every().day.at("09:00").do(...)

# Her 2 saatte
schedule.every(2).hours.do(...)

# Her Pazartesi 10:00
schedule.every().monday.at("10:00").do(...)

# Her 30 dakikada
schedule.every(30).minutes.do(...)
```

## 🛡️ Gizlilik ve Güvenlik

### Loglanan Bilgiler:
✅ Kullanıcı adı (sistem kullanıcısı)
✅ Makine adı  
✅ Aktivite tipleri
✅ Zaman damgaları
✅ Dosya adları
✅ Sayfa isimleri

### Loglanmayan Bilgiler:
❌ Şifreler
❌ Hassas veri içerikleri
❌ Kişisel bilgiler
❌ Finansal detaylar

### Dosya Güvenliği:
- Log dosyaları lokal saklanır
- Sadece email ile paylaşılır
- Günlük bazda dosya oluşturulur
- Eski dosyalar otomatik temizlenmez (manuel temizleme gerekir)

## 📈 Kullanım Senaryoları

### 1. Performans İzleme
```
"Hangi sayfalar en çok kullanılıyor?"
"Kullanıcılar en çok hangi özellikleri kullanıyor?"
"Sistem ne kadar aktif kullanılıyor?"
```

### 2. Hata Analizi
```
"En çok hangi sayfalarda hata oluşuyor?"
"Hatalar hangi saatlerde yoğunlaşıyor?"
"Tekrar eden hatalar var mı?"
```

### 3. Aktivite Denetimi
```
"Kim ne zaman sisteme girdi?"
"Hangi kullanıcı hangi raporları export etti?"
"Kime mail gönderildi?"
```

### 4. Optimizasyon
```
"Az kullanılan özellikler hangileri?"
"Sistem yükü hangi saatlerde yüksek?"
"Kullanıcı davranış pattern'leri neler?"
```

## 🚀 Başlangıç

Sistem otomatik çalışır. Herhangi bir manuel kurulum gerekmez:

1. **Uygulama Başlatma**: Loglama otomatik başlar
2. **İlk Rapor**: Aynı gün saat 16:00'da
3. **Periyodik Raporlar**: Her 4 saatte bir
4. **Uygulama Kapanış**: Oturum özeti otomatik kaydedilir

## 💡 İpuçları

1. **Log Arşivleme**: Eski log dosyalarını periyodik olarak arşivleyin
2. **Email Kontrolü**: Spam klasörünü kontrol edin
3. **Disk Alanı**: Log dosyaları zamanla büyür, düzenli temizlik yapın
4. **Raporları Saklayın**: Trend analizi için email raporlarını saklayın
5. **JSON Parse**: Log analizi için Python/JavaScript kullanabilirsiniz

## 📞 Destek

Log sistemi ile ilgili sorunlar için:
- Log dosyalarını kontrol edin
- Email ayarlarını doğrulayın
- SMTP bağlantı sorunlarını test edin
- schedule modülünün kurulu olduğundan emin olun

---

**Not**: Bu özellik v2.8'den itibaren aktif kullanımdadır.
