# Gün 15 — Edge Monitor ürünleri

| | |
|---|---|
| **Tarih** | 2026-08-07 Cuma |
| **Hafta** | 3 |
| **Konu** | Edge Monitor ürünleri |
| **Referans** | Hafta 3 tüm örnekler |

---

## Sabah anlatımı (09:00–10:00)

I2C + BSP/APP entegrasyon ürünü

**Herkes (ortak):** Edge monitor mini ürün. Demo 8–10 dk.

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
| **A** | Climate Sentinel | 6 Must | Stretch: Stretch varsa ayrı gösterilir. |
| **B** | Motion Sentinel | 6 Must | Stretch: Stretch varsa ayrı gösterilir. |
| **C** | Comfort Station | 6 Must | Stretch: Stretch varsa ayrı gösterilir. |
| **D** | Tilt & Fall Desk | 6 Must | Stretch: Stretch varsa ayrı gösterilir. |
| **E** | Edge Hub Lite | 6 Must | Stretch: Stretch varsa ayrı gösterilir. |

---

## Detaylı Must / Stretch

### Stajyer A — Climate Sentinel
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Start/stop gate | ☐ |
| 2 | Hot/cold alarm | ☐ |
| 3 | Histerezis + ack | ☐ |
| 4 | Dashboard | ☐ |
| 5 | APP API | ☐ |
| 6 | Fail-safe | ☐ |
**Stretch:** Stretch varsa ayrı gösterilir.
### Stajyer B — Motion Sentinel
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Shake | ☐ |
| 2 | Orientation UI | ☐ |
| 3 | Cooldown | ☐ |
| 4 | Event log ring | ☐ |
| 5 | APP motion modülü | ☐ |
| 6 | Lab checklist | ☐ |
**Stretch:** Stretch varsa ayrı gösterilir.
### Stajyer C — Comfort Station
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Temp/RH comfort score | ☐ |
| 2 | 3 LED | ☐ |
| 3 | Birim değiştir | ☐ |
| 4 | Verbose/compact | ☐ |
| 5 | Dashboard | ☐ |
| 6 | Lab checklist | ☐ |
**Stretch:** Stretch varsa ayrı gösterilir.
### Stajyer D — Tilt & Fall Desk
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Orientation LED | ☐ |
| 2 | Fall candidate | ☐ |
| 3 | False-positive lab | ☐ |
| 4 | Eşik UART config | ☐ |
| 5 | Dashboard | ☐ |
| 6 | Lab checklist | ☐ |
**Stretch:** Stretch varsa ayrı gösterilir.
### Stajyer E — Edge Hub Lite
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Climate + motion alarm birleşik bitmask | ☐ |
| 2 | Öncelik | ☐ |
| 3 | `Sensor_*` facade | ☐ |
| 4 | 1 sayfa mimari | ☐ |
| 5 | Dashboard | ☐ |
| 6 | Lab checklist | ☐ |
**Stretch:** Stretch varsa ayrı gösterilir.


## Cuma özel

- Her stajyer **8–10 dk** demo yapar.
- Must checklist mentöre okunur.
- Stretch varsa ayrı gösterilir.
- Teslim: lab notu + kod + kanıt (log/screenshot).

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
