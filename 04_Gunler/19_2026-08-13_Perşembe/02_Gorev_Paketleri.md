# Gün 19 — Görev Paketleri

**Tarih:** 2026-08-13 Perşembe  
**Konu:** Telemetri + alarm kanalları

> Her stajyer **kendi paketini** yapar. Kopyalama yok.

---

## Stajyer A — Full Telemetry

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Temp, RH, bat, accel özet, micRMS | ☐ |
| 2 | Period config | ☐ |
| 3 | Broker proof | ☐ |
| 4 | JSON şema | ☐ |

**Stretch:** Field enable bitmask.

**Teslim yolu:** `teslimler/Stajyer_A/`

---

## Stajyer B — Temp Alarm Channel

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Ayrı alarm topic | ☐ |
| 2 | Latch/ack | ☐ |
| 3 | Telemetry'den ayrışma | ☐ |
| 4 | Kanıt | ☐ |

**Stretch:** Alarm rate-limit.

**Teslim yolu:** `teslimler/Stajyer_B/`

---

## Stajyer C — Mic Alarm Channel

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | LOUD → MQTT | ☐ |
| 2 | Yerel pattern | ☐ |
| 3 | Ack | ☐ |
| 4 | Kanıt | ☐ |

**Stretch:** Alarm payload'da RMS.

**Teslim yolu:** `teslimler/Stajyer_C/`

---

## Stajyer D — Motion Alarm Channel

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Shake/fall → MQTT | ☐ |
| 2 | False trigger notu | ☐ |
| 3 | Kanıt | ☐ |
| 4 | Doküman | ☐ |

**Stretch:** Orientation change event (opsiyonel).

**Teslim yolu:** `teslimler/Stajyer_D/`

---

## Stajyer E — Publish Visibility

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Her publish'te TX log/LED | ☐ |
| 2 | Fail'de ERR | ☐ |
| 3 | Ardışık fail→state ERROR | ☐ |
| 4 | Görünürlük | ☐ |

**Stretch:** Başarı oranı (ok/fail).

**Teslim yolu:** `teslimler/Stajyer_E/`
