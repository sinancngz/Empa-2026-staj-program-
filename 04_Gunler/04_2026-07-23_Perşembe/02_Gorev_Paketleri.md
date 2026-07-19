# Gün 04 — Görev Paketleri

**Tarih:** 2026-07-23 Perşembe  
**Konu:** IRQ + EINT + karşılaştırma

> Her stajyer **kendi paketini** yapar. Kopyalama yok.

---

## Stajyer A — IRQ Echo Router

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | UART IRQ RX echo | ☐ |
| 2 | Özel karakterler (`L` LED toggle, `S` status) main'de işlensin | ☐ |
| 3 | ISR'da ağır iş yok | ☐ |
| 4 | Flag/queue kullanımı | ☐ |

**Stretch:** RX overrun/hata sayacı.

**Teslim yolu:** `teslimler/Stajyer_A/`

---

## Stajyer B — EINT Button Core

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Buton EINT | ☐ |
| 2 | Debounce (main veya timer tick) | ☐ |
| 3 | Event queue | ☐ |
| 4 | LED/UART consumer | ☐ |

**Stretch:** Rising/falling ayrı sayaç.

**Teslim yolu:** `teslimler/Stajyer_B/`

---

## Stajyer C — Hybrid Control

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | TX polling + RX IRQ | ☐ |
| 2 | Komutla LED | ☐ |
| 3 | Buton EINT aynı projede çakışmadan | ☐ |
| 4 | Flag/queue kullanımı | ☐ |

**Stretch:** Komut `irqstat` ile flag/queue derinliği.

**Teslim yolu:** `teslimler/Stajyer_C/`

---

## Stajyer D — Benchmark Note

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Aynı senaryoyu (buton→LED+log) polling ve IRQ ile iki build/flag'de üret | ☐ |
| 2 | Lab notunda latency/CPU idle gözlemi (≥8 madde) | ☐ |
| 3 | Ölçüm varsa sayı | ☐ |
| 4 | Karşılaştırma tablosu | ☐ |

**Stretch:** Basit "missed event" sayacı.

**Teslim yolu:** `teslimler/Stajyer_D/`

---

## Stajyer E — Safe ISR Pattern

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | EINT → flag → main state machine | ☐ |
| 2 | UART spam yok (event'te 1 log) | ☐ |
| 3 | Yeniden giriş / bounce test prosedürü lab notunda | ☐ |
| 4 | Güvenli ISR alışkanlığı | ☐ |

**Stretch:** Critical section notu (shared değişken `volatile` + neden).

**Teslim yolu:** `teslimler/Stajyer_E/`
