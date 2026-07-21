# Gün 02 — MCU temelleri, buton & debounce

| | |
|---|---|
| **Tarih** | 2026-07-21 Salı |
| **Hafta** | 1 |
| **Konu** | Mikroişlemci / mikrodenetleyici · saat · debounce, kısa / uzun basış, event |
| **Referans** | `Examples/GPIO/*` |

---

## Bugün ne yapacağız?

Sabah önce **mikroişlemci vs mikrodenetleyici**, bellek, bus, sistem saati ve proje dosya yapısı (`.c` / `.h`, init) anlatılacak. Ardından buton okumayı güçlendireceğiz: debounce, kısa/uzun basış ve LED ile tepki. Herkes aynı kolay → orta → zor görevlerini yapacak.

Anlatım notları: [`01_Anlatim.md`](01_Anlatim.md)  
Görevler: [`02_Gorevler.md`](02_Gorevler.md)

---

## Günlük ritim

| Saat | Aktivite |
|------|----------|
| 09:00–10:30 | MCU temelleri + sistem saati + `.c`/`.h` / init |
| 10:30–12:30 | Buton & debounce anlatımı · uygulama / kurulum |
| 13:30–14:30 | Konu pekiştirme / mentör turu |
| 14:30–16:30 | Görevler (kolay / orta / zor) |
| 16:30–17:00 | Stand-up + teslim |

---

## Anlatım

1. Mikroişlemci, mikrodenetleyici, farklar  
2. Çalışma prensibi, kesme (kısa)  
3. Sistem saati (HSI / HSE / LSI / LSE / PLL)  
4. `.c` / `.h`, `HAL_Init`, fonksiyon prototipi  
5. Buton, debounce, kısa / uzun basış → görevler  

Detay: [`01_Anlatim.md`](01_Anlatim.md)

---

## Görevler

Herkes aynı listeyi yapar: kolay → orta → zor.  
Detay: [`02_Gorevler.md`](02_Gorevler.md)

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/gunluk_rapor.md
└── proje/
```
