# Gün 14 — Görev Paketleri

**Tarih:** 2026-08-06 Perşembe  
**Konu:** Gerçek BSP/APP ayrımı

> Her stajyer **kendi paketini** yapar. Kopyalama yok.

---

## Stajyer A — APP API Hot/Cold

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | `app_climate.h` API (`IsHot/IsCold/Get`) | ☐ |
| 2 | Main sadece API kullansın | ☐ |
| 3 | Eşikler APP'te | ☐ |
| 4 | Katman ayrımı | ☐ |

**Stretch:** Unit test'e benzer host'suz self-check fonksiyonu.

**Teslim yolu:** `teslimler/Stajyer_A/`

---

## Stajyer B — APP Motion Module

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | `IsShaken/IsFallCandidate/GetOrientation` | ☐ |
| 2 | LED binding APP dışında/process'te | ☐ |
| 3 | Modül ayrımı | ☐ |
| 4 | API netliği | ☐ |

**Stretch:** Callback ile alarm notify.

**Teslim yolu:** `teslimler/Stajyer_B/`

---

## Stajyer C — Architecture Pack

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Kendi koduna göre diyagram | ☐ |
| 2 | Her katmana örnek fonksiyon listesi | ☐ |
| 3 | "Yanlışlıkla HAL'i APP'ten çağırdım" anti-örnek | ☐ |
| 4 | Mimari doküman | ☐ |

**Stretch:** TiremoCortex ile kendi yapını karşılaştırma tablosu.

**Teslim yolu:** `teslimler/Stajyer_C/`

---

## Stajyer D — Configurable Thresholds

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Eşikler struct + setter/getter | ☐ |
| 2 | UART `th get/set` | ☐ |
| 3 | BSP'ye dokunmadan | ☐ |
| 4 | Config katmanı | ☐ |

**Stretch:** Geçersiz aralık reject.

**Teslim yolu:** `teslimler/Stajyer_D/`

---

## Stajyer E — Facade + Report

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | `Sensor_ReadAll` / `Print` / `ClearAlarms` | ☐ |
| 2 | Alarm bitmask | ☐ |
| 3 | Main ≤ ~40 satır mantık | ☐ |
| 4 | Facade | ☐ |

**Stretch:** Report format plugin (CSV/JSON).

**Teslim yolu:** `teslimler/Stajyer_E/`
