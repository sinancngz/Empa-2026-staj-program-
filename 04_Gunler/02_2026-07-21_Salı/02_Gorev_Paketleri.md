# Gün 02 — Görev Paketleri

**Tarih:** 2026-07-21 Salı  
**Konu:** Buton state machine

> Her stajyer **kendi paketini** yapar. Kopyalama yok.

---

## Stajyer A — Hold & Ramp

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Momentary LED + basılı tutma süresini UART ms | ☐ |
| 2 | 1 sn'de bir "HOLDING…" log | ☐ |
| 3 | Bırakınca total hold ms | ☐ |
| 4 | Event üretici entegrasyonu | ☐ |

**Stretch:** Tutma süresine göre 1→N LED yak (ramp).

**Teslim yolu:** `teslimler/Stajyer_A/`

---

## Stajyer B — Edge Modes

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Toggle modu + "mode LED" | ☐ |
| 2 | Her event'te UART | ☐ |
| 3 | Yanlış bounce'u log'da görünür kıl (raw vs debounced sayaç) | ☐ |
| 4 | Event üretici entegrasyonu | ☐ |

**Stretch:** 3 mod: TOGGLE / MOMENTARY / BLINK-WHILE-HOLD.

**Teslim yolu:** `teslimler/Stajyer_B/`

---

## Stajyer C — Selector Ring

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Her kısa basışta aktif LED index ilerle | ☐ |
| 2 | Seçili LED yanıp sönsün | ☐ |
| 3 | UART index | ☐ |
| 4 | Uzun basış ile "confirm" (sabit yak) | ☐ |

**Stretch:** Confirm sonrası 2 sn idle'da söndür, başa dön.

**Teslim yolu:** `teslimler/Stajyer_C/`

---

## Stajyer D — Gesture Parser

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | SHORT / LONG / DOUBLE ayrımı (zaman pencereli) | ☐ |
| 2 | Her jest farklı LED cevabı | ☐ |
| 3 | Jest sayaçları UART | ☐ |
| 4 | Event üretici entegrasyonu | ☐ |

**Stretch:** "Kombo": SHORT+LONG ardışık → özel pattern.

**Teslim yolu:** `teslimler/Stajyer_D/`

---

## Stajyer E — Arm / Disarm UI

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Uzun basış ile sistem ARMED/DISARMED | ☐ |
| 2 | Durum LED | ☐ |
| 3 | Kısa basış sadece ARMED iken işlesin | ☐ |
| 4 | UART state | ☐ |

**Stretch:** DISARM için "2× long" onayı (yanlış basış koruması).

**Teslim yolu:** `teslimler/Stajyer_E/`
