# Gün 10 — Görevler (Mikrofon Stream + Python Grafik)

Anlatım: [`01_Anlatim.md`](01_Anlatim.md)  
Python örnek: [`kaynaklar/mic_plot.py`](kaynaklar/mic_plot.py)

**Dünün devamı:** Perşembe’de ADC ile mikrofon raw değerini okudun. Bugün aynı hattı **hızlı stream** edip PC’de grafik göreceksin.

---

## Görev

1. MCU’dan mikrofon ADC örneklerini UART üzerinden **sürekli** gönder.  
2. Python ile COM porttan veriyi al, **canlı grafik** çiz.  
3. Telefonda / hoparlörde **1 kHz sinüs** dinleterek grafikte sinüs benzeri dalga gözlemle.

Amaç:

- Örnekleme hızının dalga şekline etkisini anlamak  
- UART stream formatını sabitlemek  
- PC tarafında seri port + grafik pipeline kurmak  
- 1 kHz test tonu ile ölçümü doğrulamak  

---

## Sistem zinciri

```
1 kHz sinüs (telefon)
        │
        ▼
Analog mikrofon  →  ADC (hızlı örnekleme)
        │
        ▼
UART (USB COM)   →  satır satır: 2048\n 2101\n ...
        │
        ▼
Python (pyserial + matplotlib)  →  canlı dalga grafiği
```

---

## Yapılacaklar

| # | Madde | Yapıldı |
|---|-------|---------|
| 1 | Dünkü mikrofon ADC projesini aç / derle | ☐ |
| 2 | UART formatını netleştir: her satırda bir raw (`2048` veya `MIC=2048`) | ☐ |
| 3 | Örnekleri **en az ~5–10 kHz** hedefli gönder (mentörle baud/format konuş) | ☐ |
| 4 | PC’de Python ortamı kur (`pip install -r kaynaklar/requirements.txt`) | ☐ |
| 5 | `mic_plot.py --simulate` ile önce sahte 1 kHz dalgayı gör | ☐ |
| 6 | Gerçek COM port ile bağlan (`--port COMx`) | ☐ |
| 7 | Sessiz ortamda bias civarı düz çizgi / küçük gürültü gözle | ☐ |
| 8 | Telefonda **1 kHz** ton çal → sinüs benzeri salınım gör | ☐ |
| 9 | Ekran görüntüsü + gözlemleri rapora yaz | ☐ |
| 10 | Teorik soruları cevapla | ☐ |

---

## Firmware beklentisi

### Çıktı formatı (önerilen)

Her örnek **tek satır**, sadece sayı (parse kolay):

```
2048
2105
2150
2100
2040
1980
1920
1980
2048
```

Alternatif (Python örnek her ikisini de kabul eder):

```
MIC=2048
MIC=2105
```

### Hız ipucu

| Baud | Kabaca ASCII satır kapasitesi |
|------|-------------------------------|
| 115200 | Düşük–orta (kısa sayılarla birkaç kHz civarı mümkün) |
| Daha yüksek baud / binary | Daha temiz yüksek \(f_s\) |

1 kHz sinüsü **görmek** için pratikte \(f_s \gtrsim 5\,\text{kHz}\) iyi bir hedeftir (Nyquist: en az 2 kHz; görsel kalite için daha yüksek).

Mentöre gösterirken: “kaç örnek/sn gönderiyorum?” sorusuna kabaca cevap verebil.

Örnek iskelet (pseudo):

```c
while (1) {
    uint16_t mic = ADC_ReadMic();
    printf("%u\n", mic);   /* veya Debug_Printf */
    /* örnekleme periyodu: timer / kısa delay — mentörle ayarla */
}
```

> Not: `printf` + çok uzun delay ile sadece “nokta bulutu” görürsün; dalga için delay’i kısalt / timer kullan.

---

## Python tarafı

Kurulum:

```bash
cd 02_Gunler/10_2026-07-31_Cuma/kaynaklar
pip install -r requirements.txt
```

Sahte 1 kHz (kart yokken):

```bash
python mic_plot.py --simulate
```

Gerçek kart:

```bash
python mic_plot.py --port COM5 --baud 115200
```

Windows’ta COM numarasını Aygıt Yöneticisi / mentörden öğren.

Beklenen:

- Sessiz: yatay band (bias)  
- 1 kHz: düzenli sinüs benzeri salınım  
- Konuşma: düzensiz, geniş genlik  

---

## 1 kHz test nasıl yapılır?

1. Telefonda online “tone generator” veya ses uygulaması aç.  
2. Frekansı **1000 Hz** yap, sinüs seç.  
3. Mikrofon yakınına koy (çok yüksek sesle bozma).  
4. Grafikte periyodik dalga göründüğünü kaydet / ekran görüntüsü al.

İsteğe bağlı: aynı testi 500 Hz ve 2 kHz ile karşılaştır (dalga sıklaşır / seyrekleşir).

---

## Bonus

| # | Bonus | Yapıldı |
|---|-------|---------|
| 1 | Python’da min / max / peak-to-peak yazdır | ☐ |
| 2 | Bias’ı çıkararak AC-only grafik (değer − ortalama) | ☐ |
| 3 | LED: genlik eşiği aşılınca yak | ☐ |
| 4 | Binary `uint16` stream (daha yüksek hız) — mentör onayıyla | ☐ |

---

## Teorik Sorular (Cevapları rapora yaz)

**1.** Dün tek tek `MIC = …` yazmak neden dalga şeklini göstermez?


**2.** 1 kHz sinüs için teorik minimum örnekleme frekansı (Nyquist) nedir? Pratikte neden daha yüksek isteriz?


**3.** Örnekleme çok yavaş olursa grafikte ne görürsün?


**4.** Mikrofon sessizken grafik neden sıfırda değil, orta bir seviyede (bias) durur?


**5.** UART baud rate düşük, örnek hızı yüksek olursa ne olur?


**6.** `MIC=2048` ile sadece `2048` satırı arasında Python için fark var mı? Hangisini tercih edersin, neden?


**7.** Peak-to-peak (tepe–tepe) ne demektir? Ses seviyesi ile ilişkisi nedir?


**8.** Aynı 1 kHz tonu daha uzaktan çalarsan grafikte ne değişir, ne değişmez?


**9.** Dijital mikrofon (PDM/I2S) kullansaydık bugünkü UART+ADC grafiği aynı şekilde kurulur muydu?


**10.** Canlı grafikte gördüğün “sinüs” neden laboratuvar osiloskopundaki kadar temiz olmayabilir? (en az 2 sebep)

---

## Kabul

Mentöre gösterirken:

- [ ] UART’tan sürekli örnek geliyor  
- [ ] Python canlı grafik açılıyor  
- [ ] Sessiz / 1 kHz farkı net  
- [ ] 1 kHz’de sinüs benzeri dalga görülüyor (ekran görüntüsü raporda)  
- [ ] Teorik sorular raporda  

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/
│   └── gunluk_rapor.md
└── proje/
    ├── (firmware)
    └── (isteğe bağlı) mic_plot.py / ekran görüntüsü
```
