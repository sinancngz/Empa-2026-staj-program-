# Gün 03 — Kesme, harici kesme & NVIC

| | |
|---|---|
| **Tarih** | 2026-07-22 Çarşamba |
| **Hafta** | 1 |
| **Konu** | Interrupt · EXTI · NVIC · pin kenar ayarları |
| **Referans** | GPIO / EXTI örnekleri · pin config (MCUBrew) |

---

## Bugün ne yapacağız?

Sabah **kesme, NVIC ve harici kesme pin ayarları** işlenecek; notları okuyup öğreneceksiniz. Öğleden sonra görevler Pazartesi–Salı–Çarşamba bilgisini birleştirir; raporda teorik sorular cevaplanır.

Anlatım: [`01_Anlatim.md`](01_Anlatim.md)  
Görevler: [`02_Gorevler.md`](02_Gorevler.md)

---

## Günlük ritim

| Saat | Aktivite |
|------|----------|
| 09:00–10:30 | Kesme / NVIC / EXTI + resim3 pin ayarları |
| 10:30–12:30 | Uygulama: ilk harici kesme + LED |
| 13:30–14:30 | Pekiştirme / mentör turu |
| 14:30–16:30 | Görevler (kolay / orta / zor) + rapor teori |
| 16:30–17:00 | Stand-up + teslim |

---

## Anlatım özeti

1. Polling vs kesme  
2. ISR, dönüş, `volatile` flag  
3. Harici kesme (GPIO)  
4. NVIC — öncelik, nested  
5. Pin config (Edge, Rising/Falling, Pull, Debounce filtresi)  

Detay: [`01_Anlatim.md`](01_Anlatim.md) · şekil: [`kaynaklar/resimler/resim3.png`](kaynaklar/resimler/resim3.png)

---

## Görevler

Tek görev / seviye; 3 gün pekiştirme + GitHub (`2026-07-22`) + raporda 10 teori sorusu.  
Detay: [`02_Gorevler.md`](02_Gorevler.md)

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/gunluk_rapor.md
└── proje/
```
