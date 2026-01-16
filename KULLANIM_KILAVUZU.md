# Kullanım Kılavuzu - Birleşik Tedarik ve Reklamasyon Yönetim Sistemi

## 🎯 Genel Bakış

Bu sistem, tedarikçi performans yönetimi ve reklamasyon takibi için kapsamlı bir çözüm sunar.

## 📱 Ana Menü Yapısı

### Tedarikçi Performans Modülü
```
📊 Yönetim Paneli       → Ana dashboard, KPI'lar, performans grafikleri
🔍 Analiz & Veri        → Veri yükleme, filtreleme, analiz parametreleri
🛒 Akıllı Sipariş       → Otomatik sipariş önerileri ve optimizasyon
💰 Pazarlık Robotu      → AI destekli fiyat müzakeresi
📰 Sektör Haberleri     → Canlı tekstil sektörü haberleri
📝 Tedarikçi Karnesi    → Detaylı tedarikçi değerlendirme
📈 Aylık Trend          → Zaman serisi analizi
🔮 Gelecek Tahmini      → Tahmine dayalı analitik
🗺️ Harita              → Coğrafi tedarikçi haritası
📋 Detaylar             → Sipariş ve işlem detayları
⚖️ Karşılaştırma        → Tedarikçi karşılaştırma
📷 OCR (Fatura)         → Fatura okuma ve işleme
💬 Verilerinle Konuş    → AI chatbot
🤖 YZ Raporu            → Yapay zeka analiz raporu
```

### Reklamasyon Yönetimi Modülü ⭐ YENİ
```
🏭 Reklamasyon Yönetimi
   ├─ Ana Sayfa           → Hızlı erişim ve sistem durumu
   ├─ 📊 Yönetici Özeti   → Risk analizi, toplam hacimler
   ├─ 📑 Detaylı Raporlar → Operasyonel liste, filtreler
   ├─ 📧 Mail Merkezi     → Otomatik rapor gönderimi
   ├─ 📸 Fotoğraf Galerisi → Hata kanıtı yönetimi
   └─ 📂 Veri Yükleme     → Excel veri aktarımı
```

## 🚀 Hızlı Başlangıç

### 1. Tedarikçi Performans İçin
```python
# Adım 1: Analiz & Veri sekmesine gidin
# Adım 2: "Dosya Seç" ile Excel dosyanızı yükleyin
# Adım 3: "ANALİZİ BAŞLAT" butonuna tıklayın
# Adım 4: Yönetim Paneli'nde sonuçları görün
```

### 2. Reklamasyon Yönetimi İçin
```python
# Adım 1: Yan menüden "🏭 Reklamasyon Yönetimi" sekmesine tıklayın
# Adım 2: Ana sayfadan "📂 Veri Yükleme" butonuna tıklayın
# Adım 3: Reklamasyon Excel dosyanızı yükleyin
# Adım 4: "📊 Yönetici Özeti" ile sonuçları görüntüleyin
```

## 📊 Veri Formatları

### Tedarikçi Performans Verisi
Gerekli kolonlar:
- Tedarikçi Adı
- Stok Kodu
- Fiyat
- Teslimat Süresi
- İade Adedi

### Reklamasyon Verisi
Gerekli kolonlar:
- Fiş Tipi (62: Alım, 63: İade, 52: Reklamasyon)
- Fiş Tarihi
- Cari Adı (Tedarikçi)
- Order No
- Tahsis Tutarı
- Tahsis Net Miktar
- Order Grup Adı

## 🎨 Özellikler

### Reklamasyon Yöneticisi Özeti
- **KPI Kartları**: Toplam alım, risk, iade, reklamasyon
- **Grafikler**: En riskli tedarikçiler, risk dağılımı
- **Filtreler**: Tedarikçi bazlı filtreleme
- **Export**: Excel ve PDF çıktı

### Detaylı Raporlar
- **Hızlı Filtreler**: 
  - Geciken Siparişler
  - Zamanında Teslim
  - İade Olanlar
  - Reklamasyon Olanlar
  
- **Detaylı Arama**: Tedarikçi, Order No, Takım, Stok, Parti bazlı

- **İki Tablo Sistemi**:
  1. Detaylı operasyonel liste
  2. Takım bazlı yönetici özeti

### Mail Merkezi
- **HTML Formatlı**: Profesyonel görünüm
- **Otomatik Grafikler**: Risk analizi grafikleri gömülü
- **Ek Dosyalar**: Excel raporları otomatik ekleme
- **Özelleştirilebilir**: Konu ve içerik düzenleme

### Fotoğraf Galerisi
- **Fotoğraf Yükleme**: JPG, PNG desteği
- **Galeri Görünümü**: Thumbnail önizleme
- **Dokümantasyon**: Hata kanıtı saklama

## 🔧 Gelişmiş Özellikler

### Otomatik Hesaplamalar (Reklamasyon)
```
Gecikme Cezası:
  < 7 gün    → %5
  7-15 gün   → %10
  > 15 gün   → %25

Risk Oranı = (İade + Reklamasyon) / Toplam Alım * 100
```

### Veri Doğrulama
- Otomatik tarih formatı dönüşümü
- Para birimi temizleme
- Boş değer yönetimi
- Hata mesajları ve loglar

## 💡 İpuçları

1. **Veri Kalitesi**: Temiz ve düzenli veri daha iyi sonuçlar verir
2. **Düzenli Yedekleme**: Export özelliklerini kullanarak düzenli yedek alın
3. **Filtreleme**: Detaylı raporlarda filtreleri etkin kullanın
4. **Mail Ayarları**: Gmail için "Uygulama Şifresi" kullanın
5. **Fotoğraf Boyutu**: Büyük dosyalar otomatik küçültülür

## 🆘 Destek

Sorun yaşarsanız:
1. Konsol çıktısını kontrol edin
2. Veri formatını doğrulayın
3. Gerekli kütüphanelerin yüklü olduğundan emin olun

## 📝 Versiyon Bilgisi

**Versiyon**: 2.7 (Entegre)
**Son Güncelleme**: Ocak 2026
**Geliştirici**: DeFacto Tedarik Zinciri Ekibi
