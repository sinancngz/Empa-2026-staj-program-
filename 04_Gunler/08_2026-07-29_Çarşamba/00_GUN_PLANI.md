# Gün 08 — Batarya izleme sistemi

| | |
|---|---|
| **Tarih** | 2026-07-29 Çarşamba |
| **Hafta** | 2 |
| **Konu** | Batarya izleme sistemi |
| **Referans** | `Examples/ADC/ADC_Battery/` |

---

## Sabah anlatımı (09:00–10:00)

ADC batarya ölçümü, filtre, histerezis

**Herkes (ortak):** ADC ile batarya mV okuma; güvenilir eşik ve log disiplini.

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
| **A** | Battery Telemetry | 4 Must | Stretch: 1 dakikalık min/max. |
| **B** | Hysteresis Guard | 4 Must | Stretch: 3 seviye (CRIT/LOW/OK). |
| **C** | Filter Pack | 4 Must | Stretch: Basit spike reject (|Δ| büyükse at). |
| **D** | Battery Gauge UI | 4 Must | Stretch: Gauge + sayısal mV birlikte. |
| **E** | On-demand + Trend | 4 Must | Stretch: Trend'e göre LED. |

---

## Detaylı Must / Stretch

### Stajyer A — Battery Telemetry
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | 1 Hz mV + OK flag | ☐ |
| 2 | CSV log | ☐ |
| 3 | `sample` komutu | ☐ |
| 4 | ADC entegrasyonu | ☐ |
**Stretch:** 1 dakikalık min/max.
### Stajyer B — Hysteresis Guard
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | LOW/OK eşikleri histerezisli | ☐ |
| 2 | LED | ☐ |
| 3 | `LOW_BAT` event (spam yok) | ☐ |
| 4 | Histerezis disiplini | ☐ |
**Stretch:** 3 seviye (CRIT/LOW/OK).
### Stajyer C — Filter Pack
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Ham + moving average (N=5/10 seçilebilir) | ☐ |
| 2 | UART ikisini birden | ☐ |
| 3 | Filtre seçimi | ☐ |
| 4 | ADC entegrasyonu | ☐ |
**Stretch:** Basit spike reject (|Δ| büyükse at).
### Stajyer D — Battery Gauge UI
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | 4 kademe LED bar | ☐ |
| 2 | Eşik kalibrasyon tablosu (≥12 ölçüm) lab notu | ☐ |
| 3 | Gauge UI | ☐ |
| 4 | ADC entegrasyonu | ☐ |
**Stretch:** Gauge + sayısal mV birlikte.
### Stajyer E — On-demand + Trend
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Butonla ölç | ☐ |
| 2 | Son 8 örneği RAM'de tut | ☐ |
| 3 | `trend` komutu (up/down/flat kaba) | ☐ |
| 4 | Trend mantığı | ☐ |
**Stretch:** Trend'e göre LED.


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
