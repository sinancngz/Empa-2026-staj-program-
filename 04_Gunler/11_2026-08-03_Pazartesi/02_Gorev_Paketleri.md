# Gün 11 — Görev Paketleri

**Tarih:** 2026-08-03 Pazartesi  
**Konu:** SHT40 ürünleştirme

> Her stajyer **kendi paketini** yapar. Kopyalama yok.

---

## Stajyer A — Climate Stream

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Temp+RH 1 Hz + OK flag | ☐ |
| 2 | CSV | ☐ |
| 3 | Hata retry (1–2) | ☐ |
| 4 | `ERR:SHT` | ☐ |

**Stretch:** Ölçüm periyodu komutu.

**Teslim yolu:** `teslimler/Stajyer_A/`

---

## Stajyer B — Comfort Zones

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | RH ve temp için zone LED | ☐ |
| 2 | Histerezis | ☐ |
| 3 | Zone event log | ☐ |
| 4 | I2C okuma | ☐ |

**Stretch:** "Comfort score" 0–100 kaba.

**Teslim yolu:** `teslimler/Stajyer_B/`

---

## Stajyer C — Unit & Format Layer

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | °C/°F + RH | ☐ |
| 2 | Tek `print` API | ☐ |
| 3 | Buton/unit komutu | ☐ |
| 4 | Format katmanı | ☐ |

**Stretch:** JSON satır opsiyonu.

**Teslim yolu:** `teslimler/Stajyer_C/`

---

## Stajyer D — Hot Alarm Engine

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Eşik + histerezis | ☐ |
| 2 | Latch + ack | ☐ |
| 3 | LED pattern | ☐ |
| 4 | UART | ☐ |

**Stretch:** Warning vs Critical iki eşik.

**Teslim yolu:** `teslimler/Stajyer_D/`

---

## Stajyer E — Health Check

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Init fail / read fail ayrımı | ☐ |
| 2 | Boot'ta self-check | ☐ |
| 3 | Periyodik "sensor alive" LED heartbeat | ☐ |
| 4 | Sağlık izleme | ☐ |

**Stretch:** Fail counter threshold → safe mode (ölçümü durdur).

**Teslim yolu:** `teslimler/Stajyer_E/`
