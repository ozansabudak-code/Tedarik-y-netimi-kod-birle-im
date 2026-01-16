# Tedarik Yönetimi Kod Birleşimi

## Proje Açıklaması

Bu proje, iki ayrı tedarikçi yönetim sistemini birleştirerek kapsamlı bir çözüm sunmaktadır.

## ⭐ YENİ: Gelişmiş Aktivite Loglama Sistemi (v2.8)

**Detaylı kullanıcı aktivite takibi ve otomatik raporlama!**

- 📊 **Otomatik Günlük Raporlar**: Her gün saat 16:00'da email ile
- ⏱️ **Periyodik Raporlar**: Her 4 saatte bir durum raporu
- 🖱️ **Detaylı Aktivite İzleme**: Sayfa ziyaretleri, tıklamalar, export'lar
- 📧 **Email Takibi**: Kime ne zaman mail gönderildi
- 💾 **JSON & Log Dosyaları**: Machine-readable formatda kayıtlar
- ⚠️ **Hata İzleme**: Tüm sistem hataları loglanır
- 📈 **İstatistiksel Raporlar**: HTML formatında profesyonel raporlar

👉 Detaylar için [LOGLAMA_KILAVUZU.md](LOGLAMA_KILAVUZU.md) dosyasına bakın

## Dosya Yapısı

- **birinci kodum**: Orijinal tedarikçi performans analiz sistemi
- **ikinci kodum**: Reklamasyon ve kalite yönetim sistemi  
- **birlesik_kod.py**: ✨ **Birleştirilmiş ve entegre edilmiş kod** ✨

## Birleşik Kod Özellikleri

`birlesik_kod.py` dosyası, her iki sistemin tüm özelliklerini içerir:

### Tedarikçi Performans Modülü (Birinci Kod)
- 📊 Yönetim Paneli
- 🔍 Analiz & Veri Yükleme
- 🛒 Akıllı Sipariş Sistemi
- 💰 Pazarlık Robotu
- 📰 Sektör Haberleri
- 📝 Tedarikçi Karnesi
- 📈 Aylık Trend Analizi
- 🔮 Gelecek Tahmini
- 🗺️ Harita Entegrasyonu
- 📷 OCR (Fatura Okuma)
- 💬 AI Destekli Sohbet
- 🤖 YZ Raporu

### Reklamasyon Yönetimi Modülü (İkinci Kod) - YENİ!
**Ana Menüde "🏭 Reklamasyon Yönetimi" sekmesi altında:**

1. **📊 Yönetici Özeti**: 
   - Toplam alım hacmi, risk analizi
   - İade ve reklamasyon tutarları
   - Tedarikçi bazlı risk grafikleri
   - Excel/PDF export

2. **📑 Detaylı Raporlar**:
   - Operasyonel detaylı liste
   - Gelişmiş filtreleme (durum, arama)
   - Takım bazlı özet raporlar
   - Gecikme ve ceza hesaplamaları

3. **📧 Mail Merkezi**:
   - HTML formatlı profesyonel raporlar
   - Otomatik grafik ekleme
   - Excel ek dosyaları
   - Toplu mail gönderimi

4. **📸 Fotoğraf Galerisi**:
   - Hata kanıtı fotoğraf yükleme
   - Galeri görünümü
   - Parti/sipariş bazlı dokümantasyon

5. **📂 Veri Yükleme**:
   - Excel dosyası yükleme
   - Otomatik veri işleme
   - Örnek veri desteği

## Kullanım

```bash
python3 birlesik_kod.py
```

## Gereksinimler

```
tkinter
ttkthemes
pandas
matplotlib
requests
Pillow
fpdf
python-docx
smtplib
watchdog
rapidfuzz
tkintermapview (opsiyonel)
```

## Kurulum

```bash
pip install -r requirements.txt
```

## Özellikler

- ✅ Tüm orijinal özellikler korundu
- ✅ Reklamasyon yönetimi tam entegre edildi
- ✅ Modern ve tutarlı arayüz
- ✅ Yan yana çalışan modüller
- ✅ Bağımsız veri setleri
- ✅ Export/import özellikleri

## Not

Her iki modül bağımsız çalışır ve kendi veri setlerini kullanır. Reklamasyon modülü, ana menüden kolayca erişilebilir bir sekme olarak entegre edilmiştir.