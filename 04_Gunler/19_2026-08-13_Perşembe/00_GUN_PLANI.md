# Gün 19 — Telemetri + alarm kanalları

| | |
|---|---|
| **Tarih** | 2026-08-13 Perşembe |
| **Hafta** | 4 |
| **Konu** | Telemetri + alarm kanalları |
| **Referans** | `Examples/TiremoCortex/` |

---

## Sabah anlatımı (09:00–10:00)

Full telemetry ve ayrı alarm topic'leri

**Herkes (ortak):** Telemetry ile alarm kanalını ayır; latch/ack disiplini.

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
| **A** | Full Telemetry | 4 Must | Stretch: Field enable bitmask. |
| **B** | Temp Alarm Channel | 4 Must | Stretch: Alarm rate-limit. |
| **C** | Mic Alarm Channel | 4 Must | Stretch: Alarm payload'da RMS. |
| **D** | Motion Alarm Channel | 4 Must | Stretch: Orientation change event (opsiyonel). |
| **E** | Publish Visibility | 4 Must | Stretch: Başarı oranı (ok/fail). |

---

## Detaylı Must / Stretch

### Stajyer A — Full Telemetry
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Temp, RH, bat, accel özet, micRMS | ☐ |
| 2 | Period config | ☐ |
| 3 | Broker proof | ☐ |
| 4 | JSON şema | ☐ |
**Stretch:** Field enable bitmask.
### Stajyer B — Temp Alarm Channel
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Ayrı alarm topic | ☐ |
| 2 | Latch/ack | ☐ |
| 3 | Telemetry'den ayrışma | ☐ |
| 4 | Kanıt | ☐ |
**Stretch:** Alarm rate-limit.
### Stajyer C — Mic Alarm Channel
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | LOUD → MQTT | ☐ |
| 2 | Yerel pattern | ☐ |
| 3 | Ack | ☐ |
| 4 | Kanıt | ☐ |
**Stretch:** Alarm payload'da RMS.
### Stajyer D — Motion Alarm Channel
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Shake/fall → MQTT | ☐ |
| 2 | False trigger notu | ☐ |
| 3 | Kanıt | ☐ |
| 4 | Doküman | ☐ |
**Stretch:** Orientation change event (opsiyonel).
### Stajyer E — Publish Visibility
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Her publish'te TX log/LED | ☐ |
| 2 | Fail'de ERR | ☐ |
| 3 | Ardışık fail→state ERROR | ☐ |
| 4 | Görünürlük | ☐ |
**Stretch:** Başarı oranı (ok/fail).


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
