## Görev

Analog mikrofon sensöründen gelen ses sinyalini ADC üzerinden oku.

Okunan ADC değerlerini debug UART üzerinden terminale yazdır.

Amaç:

- ADC çalışma mantığını anlamak
- Analog sinyali dijital veriye çevirmek
- ADC raw değerlerini okumak
- UART ile ölçüm sonuçlarını gözlemlemek

---

## Görev Senaryosu

Sistemde analog çıkış veren bir mikrofon sensörü bulunmaktadır.

Mikrofon çıkışı:

```
Ses sinyali
     |
     v
Analog Mikrofon
     |
     v
ADC Kanalı
     |
     v
Mikrodenetleyici
     |
     v
UART Terminal
```

ADC üzerinden okunan değerler terminalde gösterilecektir.

Örnek çıktı:

```
MIC RAW = 2048

MIC RAW = 2135

MIC RAW = 1987
```

---

# Yapılacaklar

| # | Madde | Yapıldı |
|---|-------|---------|
| 1 | Mikrofon datasheet'inden çalışma gerilimini ve çıkış tipini incele | ☐ |
| 2 | Kart şemasından mikrofon ADC pinini ve ADC kanalını bul | ☐ |
| 3 | ADC kanalını doğru şekilde yapılandır | ☐ |
| 4 | ADC ile mikrofon analog değerini oku | ☐ |
| 5 | ADC raw değerini UART üzerinden yazdır | ☐ |
| 6 | Sessiz ortam ve sesli ortam ADC değerlerini karşılaştır | ☐ |
| 7 | ADC değerini gerilim değerine çevir | ☐ |
| 8 | Ölçüm sonuçlarını rapora ekle | ☐ |
| 9 | Teorik soruları cevapla | ☐ |

---

# Teknik Gereksinimler

## ADC Okuma

ADC'den alınan değer:

```c
uint16_t mic_value;
```

şeklinde tutulmalıdır.

Örnek:

```c
mic_value = ADC_Read();
```

---

# UART Çıktısı

Her 100 ms veya 500 ms'de bir değer gönderilebilir.

Örnek:

```
MIC = 2034
MIC = 2050
MIC = 2201
```

---

# ADC Değerini Gerilime Çevirme

ADC çözünürlüğü:

```
12 bit ADC
```

ise maksimum değer:

```
4095
```

Formül:

```
Vadc = (ADC_RAW / ADC_MAX) * Vref
```

Örnek:

```
ADC_RAW = 2048

Vref = 3.3V
```

Yaklaşık:

```
Vadc = 1.65V
```

hesaplanır.

---

# Bonus Görev 1 — Ses Seviyesi Takibi

ADC değerine göre ses seviyesi belirleyin.

Örnek:

```
MIC < 1000

Sessiz


1000 < MIC < 3000

Normal


MIC > 3000

Yüksek ses
```

UART çıktısı:

```
MIC = 3200
LEVEL = LOUD
```

---

# Bonus Görev 2 — Peak Detection

Son okunan değerleri karşılaştırın.

Amaç:

Ani yüksek sesleri algılamak.


Örnek:

```
Normal:

MIC = 2100


Ses patlaması:

MIC = 3500

ALARM!
```

---

# Bonus Görev 3 — Bit İşlemleri ile Durum Kaydı

Sistem durum register'ı oluşturun:

```c
uint8_t mic_status;
```

Bit yapısı:

```
Bit0 : ADC Ready

Bit1 : Sound Detected

Bit2 : High Sound Alarm

Bit3 : UART Active
```

Örnek:

ADC okuma tamamlandı:

```c
mic_status |= (1 << 0);
```

Yüksek ses algılandı:

```c
mic_status |= (1 << 2);
```

UART:

```
STATUS = 0x05
```

---

# Teorik Sorular (Cevapları rapora yaz)

**1.** ADC'nin görevi nedir? Analog sinyal neden doğrudan mikrodenetleyici tarafından işlenemez?


**2.** Analog mikrofon çıkışı neden ADC girişine bağlanır?


**3.** 12 bit ADC kaç farklı dijital değer üretebilir?


**4.** Vref = 3.3V ve ADC çözünürlüğü 12 bit ise 1 ADC adımı kaç mV değerindedir?


**5.** ADC değeri 2048 olan bir sinyalin yaklaşık gerilimi kaç volttur?


**6.** Mikrofon sessizken ve ses varken ADC değerleri neden farklı olur?


**7.** Sampling (örnekleme) nedir? ADC için neden önemlidir?


**8.** Sampling frekansı düşük olursa ses sinyalinde ne gibi problemler oluşabilir?


**9.** Analog mikrofon yerine dijital mikrofon kullanılırsa ADC'ye ihtiyaç olur mu? Açıklayınız.


**10.** ADC kanalını yanlış seçerseniz sistemde nasıl bir problem oluşur?

---

# Kabul

Mentöre gösterirken:

- Mikrofon ADC değerleri okunmalı
- UART terminalde değerler görünmeli
- Sessiz ve sesli durumda ADC değişimi gözlemlenmeli
- ADC raw değeri ve voltaj dönüşümü raporda bulunmalı

---

# Teslim

```
teslimler/Stajyer_X/

├── rapor/
│   └── gunluk_rapor.md
└── proje/

```
