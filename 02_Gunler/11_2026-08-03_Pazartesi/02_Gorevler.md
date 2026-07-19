# Gün 11 — Görevler

**Herkes aynı görevleri yapar.**  
Sıra: Kolay → Orta → Zor. Bitirdikçe mentöre göster.

Referans: `Examples/I2Cn/I2Cn_SHT40/`

---

## Ortak hazırlık

- [ ] Ortam / proje açılıyor
- [ ] Kart bağlı
- [ ] Bugünün anlatımı yapıldı

---

## Kolay

| # | Görev | Yapıldı |
|---|-------|---------|
| 1 | SHT40 örneğini çalıştır | ☐ |
| 2 | Temp + RH’yi 1 Hz civarı UART’a yaz | ☐ |
| 3 | OK / hata durumunu ayırt et | ☐ |

---

## Orta

| # | Görev | Yapıldı |
|---|-------|---------|
| 1 | Sıcaklık veya RH için zone / eşik LED | ☐ |
| 2 | Hata olunca retry (1–2) dene | ☐ |
| 3 | `ERR:SHT` benzeri net log | ☐ |

---

## Zor

| # | Görev | Yapıldı |
|---|-------|---------|
| 1 | Hot alarm: eşik + histerezis + ack | ☐ |
| 2 | °C/°F birim değiştir (buton veya komut) | ☐ |
| 3 | Rapora ölçüm / eşik notu ekle | ☐ |

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/gunluk_rapor.md
└── proje/
```
