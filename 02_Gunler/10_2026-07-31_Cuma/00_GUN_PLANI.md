# Gün 10 — Mikrofon → Python grafik (1 kHz test)

| | |
|---|---|
| **Tarih** | 2026-07-31 Cuma |
| **Hafta** | 2 |
| **Konu** | Mikrofon stream + UART + Python canlı grafik |
| **Referans** | Dün: `Examples/ADC/ADC_Microphone/` · Bugün: `kaynaklar/mic_plot.py` |

---

## Bugün ne yapacağız?

Dünkü mikrofon ADC okumasını **hızlı örnek stream**’e çevirip PC’de Python ile canlı grafik çizeceğiz. Test için telefonda **1 kHz sinüs** dinleterek dalga şeklini doğrulayacağız.

Anlatım notları: [`01_Anlatim.md`](01_Anlatim.md)  
Görevler: [`02_Gorevler.md`](02_Gorevler.md)  
Python örnek: [`kaynaklar/mic_plot.py`](kaynaklar/mic_plot.py)

---

## Günlük ritim

| Saat | Aktivite |
|------|----------|
| 09:00–10:30 | Stream + Nyquist + Python anlatımı |
| 10:30–12:30 | Firmware: hızlı MIC örnek gönderimi |
| 13:30–14:30 | Python kurulum + COM port bağlantı |
| 14:30–16:30 | Canlı grafik + 1 kHz test + rapor |
| 16:30–17:00 | Stand-up + demo + teslim |

---

## Anlatım özeti

- Dünkü tek satır log → bugün zaman eksenli dalga  
- Örnekleme frekansı ve 1 kHz için neden yeterli \(f_s\) lazım  
- UART formatı (satır satır raw)  
- `pyserial` + `matplotlib` ile canlı plot  
- Demo / `--simulate` ile Python’u donanımsız deneme  

Detay: [`01_Anlatim.md`](01_Anlatim.md)

---

## Görevler

Herkes aynı listeyi yapar.  
Detay: [`02_Gorevler.md`](02_Gorevler.md)

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/gunluk_rapor.md
└── proje/          # firmware + (isteğe bağlı) Python script kopyası
```
