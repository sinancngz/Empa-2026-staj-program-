# Gün 12 — Görev Paketleri

**Tarih:** 2026-08-04 Salı  
**Konu:** LIS2DE12 hareket zekâsı

> Her stajyer **kendi paketini** yapar. Kopyalama yok.

---

## Stajyer A — Accel Stream + |a|

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | XYZ mg + |a| + OK | ☐ |
| 2 | 1 Hz/2 Hz log | ☐ |
| 3 | I2C okuma | ☐ |
| 4 | Birim dönüşümü | ☐ |

**Stretch:** Ham vs mg dönüşüm notu lab.

**Teslim yolu:** `teslimler/Stajyer_A/`

---

## Stajyer B — Orientation FSM

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | ±X/±Y/±Z dominant orientation | ☐ |
| 2 | Debounce zamanı | ☐ |
| 3 | LED map | ☐ |
| 4 | Event | ☐ |

**Stretch:** UNKNOWN state.

**Teslim yolu:** `teslimler/Stajyer_B/`

---

## Stajyer C — Shake Detector

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Δg / yüksek geçiş benzeri eşik | ☐ |
| 2 | Cooldown | ☐ |
| 3 | Latch/ack | ☐ |
| 4 | Event log | ☐ |

**Stretch:** Shake yoğunluğu sayacı.

**Teslim yolu:** `teslimler/Stajyer_C/`

---

## Stajyer D — Fall Candidate

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Free-fall benzeri düşük |a| penceresi | ☐ |
| 2 | Doğrulama süresi | ☐ |
| 3 | `FALL` | ☐ |
| 4 | False-positive notu | ☐ |

**Stretch:** Fall sonrası "impact" yüksek g.

**Teslim yolu:** `teslimler/Stajyer_D/`

---

## Stajyer E — Motion Activity

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | STILL / MOVE sınıflandırıcı | ☐ |
| 2 | LED | ☐ |
| 3 | Aktivite yüzdesi (son 10 sn) | ☐ |
| 4 | Sınıflandırıcı | ☐ |

**Stretch:** UART `activity` komutu.

**Teslim yolu:** `teslimler/Stajyer_E/`
