# Gün 02 — Buton state machine

| | |
|---|---|
| **Tarih** | 2026-07-21 Salı |
| **Hafta** | 1 |
| **Konu** | Buton state machine |
| **Referans** | `Examples/GPIO/*` |

---

## Sabah anlatımı (09:00–10:00)

Debounce, kısa/uzun basış, event vs level

**Herkes (ortak):** Debounce'lu buton event üretici (`PRESS`, `RELEASE`, `LONG`, isteğe `DOUBLE`).

---

## Günlük ritim

| Saat | Aktivite |
|------|----------|
| 09:00–10:00 | Ortak konu anlatımı |
| 10:00–12:30 | Bireysel görev paketi |
| 13:30–16:30 | Devam + mentör turu / debug |
| 16:30–17:00 | Stand-up (ne bitti / Must'ta kalan / blocker) |

---

## Görev paketleri (özet)

| Stajyer | Paket | Kapsam | Stretch |
|---------|-------|--------|---------|
| **A** | Hold & Ramp | 4 Must | Stretch: Tutma süresine göre 1→N LED yak (ramp). |
| **B** | Edge Modes | 4 Must | Stretch: 3 mod: TOGGLE / MOMENTARY / BLINK-WHILE-HOLD. |
| **C** | Selector Ring | 4 Must | Stretch: Confirm sonrası 2 sn idle'da söndür, başa dön. |
| **D** | Gesture Parser | 4 Must | Stretch: "Kombo": SHORT+LONG ardışık → özel pattern. |
| **E** | Arm / Disarm UI | 4 Must | Stretch: DISARM için "2× long" onayı (yanlış basış koruması). |

---

## Detaylı Must / Stretch

### Stajyer A — Hold & Ramp
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Momentary LED + basılı tutma süresini UART ms | ☐ |
| 2 | 1 sn'de bir "HOLDING…" log | ☐ |
| 3 | Bırakınca total hold ms | ☐ |
| 4 | Event üretici entegrasyonu | ☐ |
**Stretch:** Tutma süresine göre 1→N LED yak (ramp).
### Stajyer B — Edge Modes
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Toggle modu + "mode LED" | ☐ |
| 2 | Her event'te UART | ☐ |
| 3 | Yanlış bounce'u log'da görünür kıl (raw vs debounced sayaç) | ☐ |
| 4 | Event üretici entegrasyonu | ☐ |
**Stretch:** 3 mod: TOGGLE / MOMENTARY / BLINK-WHILE-HOLD.
### Stajyer C — Selector Ring
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Her kısa basışta aktif LED index ilerle | ☐ |
| 2 | Seçili LED yanıp sönsün | ☐ |
| 3 | UART index | ☐ |
| 4 | Uzun basış ile "confirm" (sabit yak) | ☐ |
**Stretch:** Confirm sonrası 2 sn idle'da söndür, başa dön.
### Stajyer D — Gesture Parser
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | SHORT / LONG / DOUBLE ayrımı (zaman pencereli) | ☐ |
| 2 | Her jest farklı LED cevabı | ☐ |
| 3 | Jest sayaçları UART | ☐ |
| 4 | Event üretici entegrasyonu | ☐ |
**Stretch:** "Kombo": SHORT+LONG ardışık → özel pattern.
### Stajyer E — Arm / Disarm UI
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Uzun basış ile sistem ARMED/DISARMED | ☐ |
| 2 | Durum LED | ☐ |
| 3 | Kısa basış sadece ARMED iken işlesin | ☐ |
| 4 | UART state | ☐ |
**Stretch:** DISARM için "2× long" onayı (yanlış basış koruması).


---

## Bugünkü teslim

Her stajyer gün sonunda `teslimler/Stajyer_X/` altına koyar:

```
teslimler/Stajyer_X/
├── rapor/          → günlük rapor (şablondan)
├── lab_notu/       → mimari karar, takılma, UART log, checklist
├── kod/            → ilgili kaynak / diff notu
└── kanitlar/       → screenshot, log dosyası
```

Şablonlar: `../../01_Sablonlar/`

---

## Mentör kontrol

- [ ] Ortak lab tamamlandı
- [ ] Her stajyer kendi paketinde ilerliyor (kopyalama yok)
- [ ] Stand-up yapıldı
- [ ] Teslim klasörleri dolu / boş kontrolü
- [ ] Blocker'lar not edildi (`mentor_notlari.md`)
