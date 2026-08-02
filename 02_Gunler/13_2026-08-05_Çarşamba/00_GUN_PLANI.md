# Gün 13 — LIS2DE12 İvme (X Y Z)

| | |
|---|---|
| **Tarih** | 2026-08-05 Çarşamba |
| **Hafta** | 3 |
| **Konu** | LIS2DE12 ile X / Y / Z ivme okuma |
| **Referans** | LIS2DE12 datasheet · `Examples/I2Cn/I2Cn_LIS2DE12TR/` (varsa) |

---

## Bugün ne yapacağız?

LIS2DE12 ivmeölçerden **X, Y, Z** değerlerini okuyup UART’a yazacağız. Ana hedef veri almak; yanında kısa yan görevler ve teori soruları var.

Anlatım notları: [`01_Anlatim.md`](01_Anlatim.md)  
Görevler: [`02_Gorevler.md`](02_Gorevler.md)

---

## Günlük ritim

| Saat | Aktivite |
|------|----------|
| 09:00–10:30 | İvmeölçer + LIS2DE12 register anlatımı |
| 10:30–12:30 | WHO_AM_I + CTRL init + XYZ okuma |
| 13:30–14:30 | Orientasyon testi / debug |
| 14:30–16:30 | Ana görev + yan görevler + teori |
| 16:30–17:00 | Stand-up + teslim |

---

## Anlatım özeti

- g, eksenler, yerçekimi  
- Adres / WHO_AM_I / CTRL / OUT register’ları  
- Signed ham değer; eğince değişim  

Detay: [`01_Anlatim.md`](01_Anlatim.md)

---

## Görevler

- **Ana:** X Y Z oku  
- **Yan:** 1–2 kısa ek  
- **Teori:** rapora cevaplar  

Detay: [`02_Gorevler.md`](02_Gorevler.md)

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/gunluk_rapor.md
└── proje/
```
