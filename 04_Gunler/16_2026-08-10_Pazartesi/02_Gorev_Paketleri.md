# Gün 16 — Görev Paketleri

**Tarih:** 2026-08-10 Pazartesi  
**Konu:** Kod tabanı haritalama

> Her stajyer **kendi paketini** yapar. Kopyalama yok.

---

## Stajyer A — Bring-up + Trace

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Build/flash | ☐ |
| 2 | Button dump | ☐ |
| 3 | Call graph (prv→app→sensor) | ☐ |
| 4 | 10 kritik dosya listesi | ☐ |

**Stretch:** Bir alarmın tetik zincirini satır satır.

**Teslim yolu:** `teslimler/Stajyer_A/`

---

## Stajyer B — Sensor Contract Sheet

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | UART alanları tablo (birim, kaynak dosya, OK flag) | ☐ |
| 2 | Eksik/garip alan notu | ☐ |
| 3 | Doküman | ☐ |
| 4 | Bring-up | ☐ |

**Stretch:** `SensorData_t` alan eşlemesi.

**Teslim yolu:** `teslimler/Stajyer_B/`

---

## Stajyer C — Alarm Archaeology

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Tüm eşiklerin path+satır | ☐ |
| 2 | Varsayılan değerler | ☐ |
| 3 | Nasıl değişir | ☐ |
| 4 | Doküman | ☐ |

**Stretch:** Bir eşiği güvenli değiştirip davranış kanıtı.

**Teslim yolu:** `teslimler/Stajyer_C/`

---

## Stajyer D — LED Semantics Map

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Her status LED anlamı | ☐ |
| 2 | Hangi state'te yanar tablosu | ☐ |
| 3 | Doküman | ☐ |
| 4 | Bring-up | ☐ |

**Stretch:** Eksik LED senaryosu öner (1 paragraf).

**Teslim yolu:** `teslimler/Stajyer_D/`

---

## Stajyer E — Config Flag Matrix

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | `EMPA_*` flag'leri × davranış matrisi | ☐ |
| 2 | Yanlış kombinasyon riskleri | ☐ |
| 3 | Doküman | ☐ |
| 4 | Bring-up | ☐ |

**Stretch:** İki flag birlikte açıkken gözlem.

**Teslim yolu:** `teslimler/Stajyer_E/`
