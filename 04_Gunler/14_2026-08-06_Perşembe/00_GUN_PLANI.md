# Gün 14 — Gerçek BSP/APP ayrımı

| | |
|---|---|
| **Tarih** | 2026-08-06 Perşembe |
| **Hafta** | 3 |
| **Konu** | Gerçek BSP/APP ayrımı |
| **Referans** | `Examples/TiremoCortex/` |

---

## Sabah anlatımı (09:00–10:00)

HAL→BSP→APP→Process; `prv_user_code` ince

**Herkes (ortak):** Katmanlı mimari; main şişmesin; APP API net olsun.

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
| **A** | APP API Hot/Cold | 4 Must | Stretch: Unit test'e benzer host'suz self-check fonksiyonu. |
| **B** | APP Motion Module | 4 Must | Stretch: Callback ile alarm notify. |
| **C** | Architecture Pack | 4 Must | Stretch: TiremoCortex ile kendi yapını karşılaştırma tablosu. |
| **D** | Configurable Thresholds | 4 Must | Stretch: Geçersiz aralık reject. |
| **E** | Facade + Report | 4 Must | Stretch: Report format plugin (CSV/JSON). |

---

## Detaylı Must / Stretch

### Stajyer A — APP API Hot/Cold
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | `app_climate.h` API (`IsHot/IsCold/Get`) | ☐ |
| 2 | Main sadece API kullansın | ☐ |
| 3 | Eşikler APP'te | ☐ |
| 4 | Katman ayrımı | ☐ |
**Stretch:** Unit test'e benzer host'suz self-check fonksiyonu.
### Stajyer B — APP Motion Module
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | `IsShaken/IsFallCandidate/GetOrientation` | ☐ |
| 2 | LED binding APP dışında/process'te | ☐ |
| 3 | Modül ayrımı | ☐ |
| 4 | API netliği | ☐ |
**Stretch:** Callback ile alarm notify.
### Stajyer C — Architecture Pack
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Kendi koduna göre diyagram | ☐ |
| 2 | Her katmana örnek fonksiyon listesi | ☐ |
| 3 | "Yanlışlıkla HAL'i APP'ten çağırdım" anti-örnek | ☐ |
| 4 | Mimari doküman | ☐ |
**Stretch:** TiremoCortex ile kendi yapını karşılaştırma tablosu.
### Stajyer D — Configurable Thresholds
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Eşikler struct + setter/getter | ☐ |
| 2 | UART `th get/set` | ☐ |
| 3 | BSP'ye dokunmadan | ☐ |
| 4 | Config katmanı | ☐ |
**Stretch:** Geçersiz aralık reject.
### Stajyer E — Facade + Report
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | `Sensor_ReadAll` / `Print` / `ClearAlarms` | ☐ |
| 2 | Alarm bitmask | ☐ |
| 3 | Main ≤ ~40 satır mantık | ☐ |
| 4 | Facade | ☐ |
**Stretch:** Report format plugin (CSV/JSON).


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
