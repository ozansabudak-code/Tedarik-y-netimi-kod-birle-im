# Teknik Uygulama Kılavuzu - Yeni Modüller

## Genel Bakış

Bu dokümantasyon, sisteme eklenen yeni modüllerin teknik detaylarını, mimari kararları ve entegrasyon noktalarını açıklar.

## Modül 1: Production Pipeline (Sipariş Aşama Takibi - GANT)

### Mimari Kararlar

#### Veri Yapısı
```python
production_orders_global = {
    'ORDER_NO': {
        'name': 'Sipariş Adı',
        'stages': {
            'İplik → Kumaş': 0-100,  # Yüzde ilerleme
            'Boyama': 0-100,
            'Paketleme': 0-100,
            'Sevkiyat': 0-100
        },
        'start_date': datetime.datetime
    }
}
```

**Neden bu yapı?**
- Dictionary kullanımı O(1) erişim sağlar
- Her sipariş için bağımsız aşama takibi
- Genişletilebilir yapı (yeni aşamalar eklenebilir)
- Datetime ile süre hesaplamaları yapılabilir

#### Görselleştirme

**Matplotlib Seçimi:**
- Tkinter ile mükemmel entegrasyon
- NavigationToolbar2Tk ile zoom/pan desteği
- Profesyonel görünüm
- PNG/PDF export yetenekleri

**GANT Grafiği Implementasyonu:**
```python
# Her aşama 1 birim genişlikte
# İlerleme yüzdesi width olarak kullanılır
ax.barh(y_pos, width=progress/100, left=x_start, ...)
```

**Renk Kodları:**
- İplik → Kumaş: #3498db (Mavi) - Başlangıç
- Boyama: #9b59b6 (Mor) - İşleme
- Paketleme: #e74c3c (Kırmızı) - Tamamlama
- Sevkiyat: #2ecc71 (Yeşil) - Teslimat

### Performans Optimizasyonları

1. **Lazy Loading:** Grafik sadece tab açıldığında çizilir
2. **Selective Redraw:** Sadece değişiklik olduğunda yeniden çizim
3. **Widget Caching:** Mümkün olduğunda widget'lar tekrar kullanılır

### Genişletme Noktaları

```python
# Yeni aşama eklemek için:
# 1. stages dictionary'sine aşama ekle
# 2. stage_combo values'a ekle
# 3. Renk koduna colors listesinde ekle
stages = ['İplik → Kumaş', 'Boyama', 'Paketleme', 'Sevkiyat', 'YENİ_AŞAMA']
colors = ['#3498db', '#9b59b6', '#e74c3c', '#2ecc71', '#YENİ_RENK']
```

### Entegrasyon Noktaları

1. **Global Variables (Satır 146-148)**
```python
production_orders_global = {}
gantt_canvas_global = None
```

2. **Frame Definition (Satır 4809)**
```python
frame_production_pipeline = ttk.Frame(content_area, padding="10")
```

3. **Frames Dictionary (Satır 4832)**
```python
"Üretim Takibi": frame_production_pipeline
```

4. **Menu Items (Satır 4853)**
```python
("📅 Üretim Takibi", "Üretim Takibi")
```

5. **Show Page Function (Satır 5176)**
```python
elif page_name == "Üretim Takibi":
    init_production_pipeline_tab()
```

---

## Modül 2: Commodity Intelligence (Hammadde Fiyat İstihbaratı)

### Mimari Kararlar

#### Veri Yapısı

**Güncel Fiyatlar:**
```python
commodity_prices_global = {
    'Emtia Adı': {
        'current': float,      # Güncel fiyat
        'previous': float,     # Önceki fiyat
        'unit': str,          # Birim (USD/lb, USD/ton)
        'change': float       # Değişim miktarı
    }
}
```

**Geçmiş Fiyatlar:**
```python
commodity_history_global = {
    'Emtia Adı': {
        30: {'dates': [...], 'prices': [...]},
        90: {'dates': [...], 'prices': [...]},
        365: {'dates': [...], 'prices': [...]}
    }
}
```

**Neden çok boyutlu dictionary?**
- Hızlı erişim (O(1))
- Her emtia için bağımsız geçmiş
- Kolay filtreleme ve grafikleme
- Bellek verimliliği

#### Veri Simülasyonu

**Mock Data Stratejisi:**
```python
# Gerçekçi fiyat dalgalanması
prices = [base_price + random.uniform(-base_price*0.15, base_price*0.15) for _ in dates]
# Trend ekleme
trend = np.linspace(base_price * 0.90, base_price, len(prices))
prices = [p * 0.7 + t * 0.3 for p, t in zip(prices, trend)]
```

**Avantajları:**
- API bağımlılığı yok
- Offline çalışabilir
- Test ve demo için ideal
- Gerçek API entegrasyonu kolay

### Görselleştirme Stratejisi

**Çok Katmanlı Grafik:**
1. **Ana Fiyat Çizgisi:** Gerçek veriler
2. **Hareketli Ortalama:** 7 günlük (trend göstergesi)
3. **Referans Çizgisi:** Güncel fiyat (yatay)

**Neden 7 günlük MA?**
- Kısa vadeli gürültüyü filtreler
- Haftalık trend açıkça görünür
- Hesaplama maliyeti düşük
- Sektörde yaygın kullanım

### Uyarı Sistemi

**Eşik Değer Mantığı:**
```python
if abs(pct_change) >= 5:  # %5 kritik eşik
    icon = "🔴" if pct_change > 0 else "🟢"
    direction = "yüksek" if pct_change > 0 else "düşük"
```

**Neden %5?**
- Tekstil sektöründe anlamlı değişim
- Çok hassas değil (false alarm önleme)
- Çok geç değil (fırsat kaybını önler)
- Sektör standartları ile uyumlu

### Ticker Enhancement

**Original Ticker:**
```python
ticker_text = f"USD/TL | EUR/TL | BRENT | PAMUK (statik)"
```

**Enhanced Ticker:**
```python
# Dinamik hammadde fiyatları
if commodity_prices_global:
    cotton_data = commodity_prices_global['Pamuk']
    cotton_price = f"{cotton_data['current']:.2f}"
    cotton_icon = "🔼" if cotton_data['change'] >= 0 else "🔽"

ticker_text = f"USD/TL | EUR/TL | BRENT | PAMUK: ${cotton_price} {icon} | ..."
```

**Avantajlar:**
- Real-time güncelleme
- Görsel feedback (ikonlar)
- Tek bakışta piyasa durumu
- Modüler entegrasyon

### Threading ve Asenkron Operasyonlar

**Neden Threading?**
```python
def refresh_data():
    fetch_mock_commodity_data()  # Senkron
    update_price_cards()         # UI Update
    update_chart()               # Heavy computation
    update_alerts()              # UI Update
```

**GUI donmasını önlemek için:**
- Ağır hesaplamalar thread'de
- UI update'leri main thread'de (root.after)
- Daemon thread kullanımı (otomatik cleanup)

### Performans Optimizasyonları

1. **Grafik Cache:**
   - Aynı emtia/period için tekrar hesaplama yok
   - Widget destroy/create minimize edildi

2. **Veri Yönetimi:**
   - Sadece görünen period için veri çekilir
   - History verisi lazy load

3. **Update Strategy:**
   - 60 saniyede bir otomatik güncelleme
   - Manuel yenileme de mevcut
   - Selective update (sadece değişenler)

### Genişletme Rehberi

#### Yeni Emtia Eklemek

```python
# 1. commodity_prices_global'e ekle
commodity_prices_global['Yeni Emtia'] = {
    'current': 1000,
    'previous': 950,
    'unit': 'USD/ton',
    'change': 50
}

# 2. commodity_combo'ya ekle
commodity_combo['values'] = [..., "Yeni Emtia"]

# 3. Geçmiş veri oluştur (otomatik)
# fetch_mock_commodity_data() içinde yeni emtia için history oluşturulur
```

#### Gerçek API Entegrasyonu

```python
def fetch_real_commodity_data():
    """Gerçek API'den veri çeker"""
    # Örnek: Alpha Vantage API
    api_key = "YOUR_API_KEY"
    url = f"https://www.alphavantage.co/query?function=COMMODITY&symbol=COTTON&apikey={api_key}"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        # Parse ve commodity_prices_global'e aktar
        commodity_prices_global['Pamuk'] = {
            'current': data['price'],
            'previous': data['previous_close'],
            'unit': 'USD/lb',
            'change': data['price'] - data['previous_close']
        }
    except Exception as e:
        # Fallback to mock data
        fetch_mock_commodity_data()
```

### Güvenlik Hususları

1. **API Key Yönetimi:**
```python
# .env dosyası kullan
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('COMMODITY_API_KEY')
```

2. **Rate Limiting:**
```python
import time
last_request_time = 0
MIN_REQUEST_INTERVAL = 60  # saniye

def rate_limited_request():
    global last_request_time
    now = time.time()
    if now - last_request_time < MIN_REQUEST_INTERVAL:
        time.sleep(MIN_REQUEST_INTERVAL - (now - last_request_time))
    last_request_time = time.time()
    # API request
```

3. **Error Handling:**
```python
try:
    # API request
except requests.Timeout:
    # Fallback to cached data
except requests.ConnectionError:
    # Show offline mode
except Exception as e:
    # Log error, show user-friendly message
    activity_logger.log_error(f"API Error: {str(e)}")
```

---

## Entegrasyon Checklist

### Production Pipeline
- [x] Global variables tanımlandı
- [x] Frame oluşturuldu
- [x] Frames dictionary'e eklendi
- [x] Menu item eklendi
- [x] show_page fonksiyonuna eklendi
- [x] init fonksiyonu yazıldı
- [x] Activity logging entegrasyonu

### Commodity Intelligence
- [x] Global variables tanımlandı
- [x] Frame oluşturuldu
- [x] Frames dictionary'e eklendi
- [x] Menu item eklendi
- [x] show_page fonksiyonuna eklendi
- [x] init fonksiyonu yazıldı
- [x] Ticker enhancement yapıldı
- [x] Activity logging entegrasyonu

---

## Test Senaryoları

### Production Pipeline Tests

```python
# Test 1: Sipariş Ekleme
def test_add_order():
    order_no = "TEST-001"
    order_name = "Test Sipariş"
    # Ekleme fonksiyonu çağrılır
    assert order_no in production_orders_global
    assert production_orders_global[order_no]['name'] == order_name

# Test 2: Aşama Güncelleme
def test_update_stage():
    order_no = "TEST-001"
    stage = "Boyama"
    progress = 50
    # Güncelleme fonksiyonu çağrılır
    assert production_orders_global[order_no]['stages'][stage] == 50

# Test 3: GANT Çizimi
def test_gantt_draw():
    # Grafik çizim fonksiyonu çağrılır
    # Assert: Exception fırlatılmamalı
    # Assert: Canvas widget oluşturulmalı
```

### Commodity Intelligence Tests

```python
# Test 1: Veri Çekme
def test_fetch_data():
    fetch_mock_commodity_data()
    assert len(commodity_prices_global) == 3
    assert 'Pamuk (Cotlook A Index)' in commodity_prices_global

# Test 2: Grafik Çizimi
def test_chart_render():
    commodity = "Pamuk (Cotlook A Index)"
    period = 30
    # Grafik çizim fonksiyonu çağrılır
    assert commodity in commodity_history_global
    assert period in commodity_history_global[commodity]

# Test 3: Uyarı Sistemi
def test_alert_system():
    # %5+ değişim ile mock veri
    commodity_prices_global['Test'] = {
        'current': 100,
        'previous': 90,
        'change': 10
    }
    # Uyarı fonksiyonu çağrılır
    # Assert: Uyarı metni "yüksek" içermeli
```

---

## Troubleshooting

### Yaygın Sorunlar

**Problem 1: Grafik görünmüyor**
```python
# Çözüm: plt.tight_layout() ve canvas.draw() çağrıldığından emin ol
plt.tight_layout()
canvas = FigureCanvasTkAgg(fig, master=chart_frame)
canvas.draw()
canvas.get_tk_widget().pack(fill="both", expand=True)
```

**Problem 2: Ticker güncellenmiyor**
```python
# Çözüm: root.after ile yeniden çağrıldığından emin ol
def update_market_ticker():
    # ... update logic ...
    root.after(60000, update_market_ticker)  # 60 saniye sonra tekrar
```

**Problem 3: Thread hatası**
```python
# Çözüm: UI update'leri root.after ile sarmalayın
def background_task():
    data = fetch_data()
    root.after(0, lambda: update_ui(data))  # Ana thread'de çalıştır

threading.Thread(target=background_task, daemon=True).start()
```

---

## Sonraki Adımlar

1. **Gerçek API Entegrasyonu**
   - Cotlook API key alınması
   - API wrapper sınıfı oluşturulması
   - Error handling güçlendirilmesi

2. **Veritabanı Desteği**
   - SQLite ile lokal cache
   - Geçmiş veri saklanması
   - Offline mod desteği

3. **İleri Seviye Analizler**
   - Prophet ile tahminleme
   - Korelasyon analizi
   - Sezonsal pattern tespiti

4. **Bildirim Sistemi**
   - Email/SMS entegrasyonu
   - Slack/Teams webhook
   - Push notification

5. **Export Özellikleri**
   - GANT grafiği PDF export
   - Fiyat raporları Excel export
   - Otomatik raporlama

---

## Katkıda Bulunanlar

- DeFacto Tedarik Zinciri Ekibi
- GitHub Copilot AI Assistant

**Versiyon:** 2.8  
**Son Güncelleme:** Ocak 2026
