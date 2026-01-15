# Yeni Özellikler - Tedarik Yönetimi Sistemi v2.8

## 📅 Sipariş Aşama Takibi - GANT Planı (Production Pipeline)

### Genel Bakış
Tekstil üretim hattındaki tüm aşamaları sipariş bazında görselleştiren GANT çizelgesi modülü. Gerçek zamanlı üretim takibi ve aşama güncellemesi sağlar.

### Özellikler
- **Üretim Aşamaları:**
  - İplik → Kumaş Üretimi
  - Boyama
  - Paketleme
  - Sevkiyat

- **İnteraktif Kontroller:**
  - Yeni sipariş ekleme
  - Aşama durumu güncelleme (%0-100 arası)
  - Görsel GANT grafiği ile ilerleme takibi

- **Grafik Özellikleri:**
  - Matplotlib tabanlı profesyonel görselleştirme
  - Her aşama için farklı renk kodları
  - İlerleme yüzdelerinin grafik üzerinde gösterimi
  - Zoom ve pan özellikleri (NavigationToolbar2Tk)
  - Lejant ile aşama tanımları

### Kullanım
1. Sol menüden **"📅 Üretim Takibi"** seçeneğine tıklayın
2. **Yeni Sipariş Ekle** bölümünden:
   - Sipariş numarası girin (örn: ORD-001)
   - Sipariş adı girin (örn: Pamuklu Gömlek)
   - "➕ Sipariş Ekle" butonuna tıklayın
3. **Aşama Durumu Güncelle** bölümünden:
   - Güncellenecek siparişi seçin
   - Aşamayı seçin (İplik→Kumaş, Boyama, vb.)
   - Slider ile ilerleme yüzdesini ayarlayın (%0-100)
   - "🔄 Durumu Güncelle" butonuna tıklayın
4. Sağ paneldeki GANT grafiğinde tüm siparişlerin durumunu görüntüleyin

### Örnek Veri
Sistem ilk açılışta 3 adet örnek sipariş ile gelir:
- ORD-001: Pamuklu Gömlek (İplik %100, Boyama %75, Paketleme %30)
- ORD-002: Denim Pantolon (İplik %100, Boyama %100, Paketleme %80, Sevkiyat %20)
- ORD-003: Polyester Ceket (İplik %60)

---

## 💹 Hammadde Fiyat İstihbaratı (Commodity Intelligence)

### Genel Bakış
Tekstil sektörü için kritik hammadde fiyatlarının gerçek zamanlı takibi, geçmiş analizi ve fiyat uyarı sistemi.

### Takip Edilen Emtialar
1. **Pamuk (Cotlook A Index)** - USD/lb
2. **Polyester** - USD/ton
3. **Viskon** - USD/ton

### Özellikler

#### 1. Fiyat Kartları
- Güncel fiyat bilgileri
- Önceki fiyatla karşılaştırma
- Yükseliş/düşüş ikonları (▲/▼)
- Yüzdesel değişim hesaplaması

#### 2. Geçmiş Fiyat Grafikleri
- **Zaman Aralıkları:**
  - 30 gün
  - 90 gün
  - 365 gün (1 yıl)

- **Grafik Özellikleri:**
  - Matplotlib tabanlı profesyonel görselleştirme
  - Fiyat çizgisi
  - 7 günlük hareketli ortalama
  - Güncel fiyat referans çizgisi
  - Interaktif zoom ve pan

#### 3. Fiyat Uyarı Sistemi
- %5 ve üzeri değişimlerde otomatik uyarı
- Fiyat karşılaştırma analizi
- Referans fiyat bilgilendirmesi
- Örnek: "🔴 Pamuk: Bu fiyat %6.5 yüksek! (Referans: 92.50)"

#### 4. Canlı Ticker Şeridi
- Ana ekranın üst kısmında sürekli kayan bant
- Tüm emtia fiyatlarının özet gösterimi
- Döviz kurları (USD/TL, EUR/TL)
- Enerji fiyatları (Brent Petrol)
- Baltic Dry Index (navlun fiyatları)
- 60 saniyede bir otomatik güncelleme

### Kullanım

#### Hammadde Fiyatları Sekmesi
1. Sol menüden **"💹 Hammadde Fiyatları"** seçeneğine tıklayın
2. Üst panelde güncel fiyat kartlarını görüntüleyin
3. **Kontrol Paneli:**
   - Emtia seçin (Pamuk, Polyester, Viskon)
   - Zaman aralığı seçin (30, 90, 365 gün)
   - "📊 Grafiği Güncelle" butonuna tıklayın
4. "🔄 Verileri Yenile" ile güncel fiyatları çekin
5. Alt kısımda fiyat uyarılarını kontrol edin

#### Ticker Şeridi
- Uygulama açıldığında otomatik olarak başlar
- Ekranın en üstünde sürekli kaydırılarak gösterilir
- Hiçbir işlem gerektirmez, sürekli güncel kalır

### Veri Kaynakları
Sistem şu anda mock (test) verisi kullanmaktadır. Gerçek API entegrasyonu için aşağıdaki kaynaklar önerilebilir:
- Cotlook Index API (Pamuk)
- Commodity Market APIs (Genel emtia fiyatları)
- Yahoo Finance API (Döviz ve enerji)

### Genişletme İmkanları
1. **Yeni Emtialar:**
   - İplik fiyatları
   - Boya maddeleri
   - Aksesuar fiyatları

2. **Gelişmiş Analizler:**
   - Trend tahminleri
   - Sezonsal analiz
   - Korelasyon analizleri

3. **Alarm Sistemi:**
   - Email/SMS bildirimleri
   - Özelleştirilebilir eşik değerleri
   - Otomatik sipariş önerileri

---

## Teknik Detaylar

### Kullanılan Teknolojiler
- **Tkinter**: GUI framework
- **Matplotlib**: Grafik ve görselleştirme
- **Pandas**: Veri işleme
- **NumPy**: Sayısal hesaplamalar
- **Threading**: Asenkron veri çekme

### Dosya Konumu
Tüm yeni özellikler `birinci kodum` dosyasına entegre edilmiştir:
- Satır 1025-1475: Production Pipeline (GANT) modülü
- Satır 1477-1800: Commodity Intelligence modülü
- Satır 595-632: Enhanced ticker band

### Modüler Yapı
Her iki modül de mevcut sistem yapısına uygun olarak geliştirilmiştir:
- Ayrı init fonksiyonları
- Global değişken yönetimi
- Activity logging entegrasyonu
- Show_page dinamik yükleme

---

## Güvenlik ve Performans

### Güvenlik
- API anahtarları güvenli saklanmalı
- Hassas fiyat bilgileri şifrelenmeli
- Kullanıcı yetkilendirmesi eklenebilir

### Performans
- Thread kullanımı ile UI donması önlendi
- Veri cache mekanizması
- Grafik lazy loading
- Optimize edilmiş matplotlib rendering

---

## Destek ve Geliştirme

### Bilinen Sınırlamalar
1. Şu an mock veri kullanılmaktadır
2. Offline modda çalışmaz
3. Geçmiş veriler simüle edilmiştir

### Gelecek Geliştirmeler
1. Gerçek API entegrasyonu
2. Veritabanı desteği
3. Excel export özellikleri
4. Email/SMS bildirim sistemi
5. Tedarikçi fiyat karşılaştırma entegrasyonu

---

## İletişim
Bu özellikler hakkında sorularınız için lütfen geliştirme ekibi ile iletişime geçin.

**Versiyon:** 2.8  
**Tarih:** Ocak 2026  
**Geliştiren:** DeFacto Tedarik Zinciri Ekibi
