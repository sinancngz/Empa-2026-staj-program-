# Gün 20 — Cloud ürün demoları + final

| | |
|---|---|
| **Tarih** | 2026-08-14 Cuma |
| **Hafta** | 4 |
| **Konu** | Cloud ürün demoları + final |
| **Referans** | Hafta 4 tüm örnekler |

---

## Sabah anlatımı (09:00–10:00)

MQTT cloud ürün demosu ve staj kapanışı

**Herkes (ortak):** Final demo + portföy teslimi. Demo 8–10 dk. Yansıma zorunlu.

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
| **A** | Telemetry Beacon Pro | 6 Must | Stretch: Yansıma + Must/Stretch işaretli lab özeti. |
| **B** | Climate Cloud Guard | 6 Must | Stretch: Yansıma + Must/Stretch işaretli lab özeti. |
| **C** | Acoustic Cloud Guard | 6 Must | Stretch: Yansıma + Must/Stretch işaretli lab özeti. |
| **D** | Motion Cloud Guard | 6 Must | Stretch: Yansıma + Must/Stretch işaretli lab özeti. |
| **E** | Link Reliability Report | 6 Must | Stretch: Yansıma + Must/Stretch işaretli lab özeti. |

---

## Detaylı Must / Stretch

### Stajyer A — Telemetry Beacon Pro
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Full JSON 5 sn | ☐ |
| 2 | Button gate | ☐ |
| 3 | Connection observer | ☐ |
| 4 | Broker screenshots (≥3 senaryo) | ☐ |
| 5 | Mimari 1 sayfa | ☐ |
| 6 | Test checklist ≥12 | ☐ |
**Stretch:** Yansıma + Must/Stretch işaretli lab özeti.
### Stajyer B — Climate Cloud Guard
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Temp(+RH) telemetry | ☐ |
| 2 | Temp alarm channel | ☐ |
| 3 | Histerezis + ack | ☐ |
| 4 | Broker kanıtı | ☐ |
| 5 | Mimari 1 sayfa | ☐ |
| 6 | Test checklist ≥12 | ☐ |
**Stretch:** Yansıma + Must/Stretch işaretli lab özeti.
### Stajyer C — Acoustic Cloud Guard
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Mic zones | ☐ |
| 2 | LOUD MQTT | ☐ |
| 3 | Yerel latch | ☐ |
| 4 | Kalibrasyon özeti | ☐ |
| 5 | Mimari 1 sayfa | ☐ |
| 6 | Test checklist ≥12 | ☐ |
**Stretch:** Yansıma + Must/Stretch işaretli lab özeti.
### Stajyer D — Motion Cloud Guard
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Shake/fall cloud | ☐ |
| 2 | Button-gated sensing | ☐ |
| 3 | LED semantics | ☐ |
| 4 | Broker kanıtı | ☐ |
| 5 | Mimari 1 sayfa | ☐ |
| 6 | Test checklist ≥12 | ☐ |
**Stretch:** Yansıma + Must/Stretch işaretli lab özeti.
### Stajyer E — Link Reliability Report
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Bilinçli koparma testleri | ☐ |
| 2 | Yeniden bağlanma | ☐ |
| 3 | 1 sayfa SM | ☐ |
| 4 | Metrikler (süre, deneme) | ☐ |
| 5 | Mimari 1 sayfa | ☐ |
| 6 | Test checklist ≥12 | ☐ |
**Stretch:** Yansıma + Must/Stretch işaretli lab özeti.


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
