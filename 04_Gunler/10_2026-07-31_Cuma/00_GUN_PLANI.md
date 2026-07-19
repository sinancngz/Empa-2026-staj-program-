# Gün 10 — WDT + haftalık sistem demosu

| | |
|---|---|
| **Tarih** | 2026-07-31 Cuma |
| **Hafta** | 2 |
| **Konu** | WDT + haftalık sistem demosu |
| **Referans** | `Examples/WDT/` + Hafta 2 tüm örnekler |

---

## Sabah anlatımı (09:00–10:00)

Watchdog kick, hang, güvenli demo protokolü

**Herkes (ortak):** WDT kick; mini ürün Must ≥ 7. Demo 8–10 dk.

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
| **A** | Timed Sensor Desk | 7 Must | Stretch: Stretch varsa ayrı gösterilir. |
| **B** | Audio Level Guard | 7 Must | Stretch: Stretch varsa ayrı gösterilir. |
| **C** | Dual-Sensor Console | 7 Must | Stretch: Stretch varsa ayrı gösterilir. |
| **D** | Watchdog Story | 7 Must | Stretch: Stretch varsa ayrı gösterilir. |
| **E** | Run/Stop Recorder | 7 Must | Stretch: Stretch varsa ayrı gösterilir. |

---

## Detaylı Must / Stretch

### Stajyer A — Timed Sensor Desk
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Tick scheduler | ☐ |
| 2 | Batarya telemetry | ☐ |
| 3 | Mic RMS | ☐ |
| 4 | UART dashboard | ☐ |
| 5 | LOW_BAT LED | ☐ |
| 6 | WDT kick | ☐ |
| 7 | Bilinçli hang demosu (mentör eşliğinde) ayrı build/flag | ☐ |
**Stretch:** Stretch varsa ayrı gösterilir.
### Stajyer B — Audio Level Guard
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Mic 3-zone | ☐ |
| 2 | LED bar | ☐ |
| 3 | Latch alarm | ☐ |
| 4 | Batarya low iken mute alarm LED önceliği | ☐ |
| 5 | WDT | ☐ |
| 6 | Dashboard | ☐ |
| 7 | Lab checklist | ☐ |
**Stretch:** Stretch varsa ayrı gösterilir.
### Stajyer C — Dual-Sensor Console
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | `BAT`/`MIC` satır formatı | ☐ |
| 2 | Komutlar `rate`/`dump`/`ack` | ☐ |
| 3 | LOUD/LOW event'leri | ☐ |
| 4 | FRT uptime | ☐ |
| 5 | WDT | ☐ |
| 6 | Dashboard | ☐ |
| 7 | Lab checklist | ☐ |
**Stretch:** Stretch varsa ayrı gösterilir.
### Stajyer D — Watchdog Story
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | İki firmware: hang→reset kanıt log | ☐ |
| 2 | Kick'li güvenli firmware | ☐ |
| 3 | Lab notunda kök neden | ☐ |
| 4 | Ne zaman WDT şart (≥10 madde) | ☐ |
| 5 | Demo protokolü | ☐ |
| 6 | Karşılaştırma | ☐ |
| 7 | Checklist | ☐ |
**Stretch:** Stretch varsa ayrı gösterilir.
### Stajyer E — Run/Stop Recorder
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Buton run/stop | ☐ |
| 2 | Çalışırken 1 Hz bat+mic kaydı (RAM ring ≥32) | ☐ |
| 3 | `dump` | ☐ |
| 4 | Stop'ta özet istatistik | ☐ |
| 5 | WDT | ☐ |
| 6 | Dashboard | ☐ |
| 7 | Lab checklist | ☐ |
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
