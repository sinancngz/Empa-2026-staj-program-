# Gün 09 — Görev Paketleri

**Tarih:** 2026-07-30 Perşembe  
**Konu:** Mikrofon analiz hattı

> Her stajyer **kendi paketini** yapar. Kopyalama yok.

---

## Stajyer A — RMS Pipeline

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Capture + service loop doğru | ☐ |
| 2 | RMS 2 Hz log | ☐ |
| 3 | Fail durumunda `MIC_ERR` | ☐ |
| 4 | Pipeline iskeleti | ☐ |

**Stretch:** RMS + peak aynı satır.

**Teslim yolu:** `teslimler/Stajyer_A/`

---

## Stajyer B — 3-Zone Classifier

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | SILENT/NORMAL/LOUD | ☐ |
| 2 | LED | ☐ |
| 3 | Zone değişiminde tek event log (histerezis) | ☐ |
| 4 | Sınıflandırıcı | ☐ |

**Stretch:** Zone süreleri sayacı.

**Teslim yolu:** `teslimler/Stajyer_B/`

---

## Stajyer C — Loud Alarm FSM

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | LOUD enter/exit | ☐ |
| 2 | Alarm LED pattern | ☐ |
| 3 | UART | ☐ |
| 4 | Alarm latch (buton ack ile temizle) | ☐ |

**Stretch:** Alarm süresi timeout auto-clear.

**Teslim yolu:** `teslimler/Stajyer_C/`

---

## Stajyer D — Calibration Kit

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Sessiz oda / konuşma / alkış için ≥10'ar örnek tablo | ☐ |
| 2 | Önerilen eşikler | ☐ |
| 3 | Kodda uygula | ☐ |
| 4 | Kalibrasyon raporu | ☐ |

**Stretch:** `cal` komutu ile eşik yaz.

**Teslim yolu:** `teslimler/Stajyer_D/`

---

## Stajyer E — Peak Hold Monitor

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | 3 sn window peak hold | ☐ |
| 2 | Buton reset | ☐ |
| 3 | LED "new peak" flash | ☐ |
| 4 | Log | ☐ |

**Stretch:** Çift window (1 sn ve 3 sn).

**Teslim yolu:** `teslimler/Stajyer_E/`
