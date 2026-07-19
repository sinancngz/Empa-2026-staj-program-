# Gün 08 — Görev Paketleri

**Tarih:** 2026-07-29 Çarşamba  
**Konu:** Batarya izleme sistemi

> Her stajyer **kendi paketini** yapar. Kopyalama yok.

---

## Stajyer A — Battery Telemetry

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | 1 Hz mV + OK flag | ☐ |
| 2 | CSV log | ☐ |
| 3 | `sample` komutu | ☐ |
| 4 | ADC entegrasyonu | ☐ |

**Stretch:** 1 dakikalık min/max.

**Teslim yolu:** `teslimler/Stajyer_A/`

---

## Stajyer B — Hysteresis Guard

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | LOW/OK eşikleri histerezisli | ☐ |
| 2 | LED | ☐ |
| 3 | `LOW_BAT` event (spam yok) | ☐ |
| 4 | Histerezis disiplini | ☐ |

**Stretch:** 3 seviye (CRIT/LOW/OK).

**Teslim yolu:** `teslimler/Stajyer_B/`

---

## Stajyer C — Filter Pack

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Ham + moving average (N=5/10 seçilebilir) | ☐ |
| 2 | UART ikisini birden | ☐ |
| 3 | Filtre seçimi | ☐ |
| 4 | ADC entegrasyonu | ☐ |

**Stretch:** Basit spike reject (|Δ| büyükse at).

**Teslim yolu:** `teslimler/Stajyer_C/`

---

## Stajyer D — Battery Gauge UI

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | 4 kademe LED bar | ☐ |
| 2 | Eşik kalibrasyon tablosu (≥12 ölçüm) lab notu | ☐ |
| 3 | Gauge UI | ☐ |
| 4 | ADC entegrasyonu | ☐ |

**Stretch:** Gauge + sayısal mV birlikte.

**Teslim yolu:** `teslimler/Stajyer_D/`

---

## Stajyer E — On-demand + Trend

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Butonla ölç | ☐ |
| 2 | Son 8 örneği RAM'de tut | ☐ |
| 3 | `trend` komutu (up/down/flat kaba) | ☐ |
| 4 | Trend mantığı | ☐ |

**Stretch:** Trend'e göre LED.

**Teslim yolu:** `teslimler/Stajyer_E/`
