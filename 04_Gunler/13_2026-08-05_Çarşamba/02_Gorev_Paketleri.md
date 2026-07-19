# Gün 13 — Görev Paketleri

**Tarih:** 2026-08-05 Çarşamba  
**Konu:** Multi-sensor orchestration

> Her stajyer **kendi paketini** yapar. Kopyalama yok.

---

## Stajyer A — Dual Bus Client

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | SHT40+LIS aynı loop | ☐ |
| 2 | Her sensör bağımsız OK | ☐ |
| 3 | Kısmi fail'de diğer devam | ☐ |
| 4 | Orchestration | ☐ |

**Stretch:** Round-robin öncelik.

**Teslim yolu:** `teslimler/Stajyer_A/`

---

## Stajyer B — Power-aware Sense

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Batarya düşükse ivme örnekleme yavaşlasın (policy) | ☐ |
| 2 | Log'da policy state | ☐ |
| 3 | Policy tablosu | ☐ |
| 4 | Entegrasyon | ☐ |

**Stretch:** Kritik bataryada sadece temp.

**Teslim yolu:** `teslimler/Stajyer_B/`

---

## Stajyer C — Noise + Motion

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Mic zone + shake aynı anda | ☐ |
| 2 | Çakışmada öncelik kuralı dokümante | ☐ |
| 3 | Birleşik davranış | ☐ |
| 4 | Entegrasyon | ☐ |

**Stretch:** Birleşik `ALERT` kodu.

**Teslim yolu:** `teslimler/Stajyer_C/`

---

## Stajyer D — Dashboard v2

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Tek satır: temp, RH, |a|, bat, micRMS | ☐ |
| 2 | `compact/verbose` mod | ☐ |
| 3 | Format disiplini | ☐ |
| 4 | Entegrasyon | ☐ |

**Stretch:** 1 Hz compact / event'te verbose.

**Teslim yolu:** `teslimler/Stajyer_D/`

---

## Stajyer E — Fault Injection Drill

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Kablo/simülasyon ile fail senaryoları (≥3) | ☐ |
| 2 | Beklenen log | ☐ |
| 3 | Recovery | ☐ |
| 4 | Lab raporu | ☐ |

**Stretch:** Otomatik retry backoff.

**Teslim yolu:** `teslimler/Stajyer_E/`
