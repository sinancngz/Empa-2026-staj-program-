# Gün 04 — Görevler

**Herkes aynı görevleri yapar.**  
Sıra: Kolay → Orta → Zor. Bitirdikçe mentöre göster.

Referans: `Examples/UARTn/UARTn_Interrupt/`

---

## Ortak hazırlık

- [ ] Ortam / proje açılıyor
- [ ] Kart bağlı
- [ ] Bugünün anlatımı yapıldı

---

## Kolay

| # | Görev | Yapıldı |
|---|-------|---------|
| 1 | Butonu EINT veya IRQ ile yakala | ☐ |
| 2 | ISR’da sadece flag set et | ☐ |
| 3 | Main’de flag’e göre LED yak/söndür | ☐ |

---

## Orta

| # | Görev | Yapıldı |
|---|-------|---------|
| 1 | UART RX’i IRQ ile al (veya örnek üzerinden çalış) | ☐ |
| 2 | Gelen özel bir karakterle LED toggle | ☐ |
| 3 | ISR içinde ağır iş / delay yok | ☐ |

---

## Zor

| # | Görev | Yapıldı |
|---|-------|---------|
| 1 | Buton EINT + LED/UART consumer aynı projede | ☐ |
| 2 | Basit event sayacı (kaç kez basıldı) | ☐ |
| 3 | Kısa lab notu: polling vs IRQ farkı (3–5 madde, rapora yaz) | ☐ |

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/gunluk_rapor.md
└── proje/
```
