# Gün 04 — IRQ + EINT + karşılaştırma

| | |
|---|---|
| **Tarih** | 2026-07-23 Perşembe |
| **Hafta** | 1 |
| **Konu** | IRQ + EINT + karşılaştırma |
| **Referans** | `Examples/UARTn/UARTn_Interrupt/` |

---

## Sabah anlatımı (09:00–10:00)

ISR'da az iş, flag, race; polling vs IRQ

**Herkes (ortak):** ISR'da ağır iş yok; flag/queue → main'de işle.

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
| **A** | IRQ Echo Router | 4 Must | Stretch: RX overrun/hata sayacı. |
| **B** | EINT Button Core | 4 Must | Stretch: Rising/falling ayrı sayaç. |
| **C** | Hybrid Control | 4 Must | Stretch: Komut `irqstat` ile flag/queue derinliği. |
| **D** | Benchmark Note | 4 Must | Stretch: Basit "missed event" sayacı. |
| **E** | Safe ISR Pattern | 4 Must | Stretch: Critical section notu (shared değişken `volatile` + neden). |

---

## Detaylı Must / Stretch

### Stajyer A — IRQ Echo Router
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | UART IRQ RX echo | ☐ |
| 2 | Özel karakterler (`L` LED toggle, `S` status) main'de işlensin | ☐ |
| 3 | ISR'da ağır iş yok | ☐ |
| 4 | Flag/queue kullanımı | ☐ |
**Stretch:** RX overrun/hata sayacı.
### Stajyer B — EINT Button Core
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Buton EINT | ☐ |
| 2 | Debounce (main veya timer tick) | ☐ |
| 3 | Event queue | ☐ |
| 4 | LED/UART consumer | ☐ |
**Stretch:** Rising/falling ayrı sayaç.
### Stajyer C — Hybrid Control
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | TX polling + RX IRQ | ☐ |
| 2 | Komutla LED | ☐ |
| 3 | Buton EINT aynı projede çakışmadan | ☐ |
| 4 | Flag/queue kullanımı | ☐ |
**Stretch:** Komut `irqstat` ile flag/queue derinliği.
### Stajyer D — Benchmark Note
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Aynı senaryoyu (buton→LED+log) polling ve IRQ ile iki build/flag'de üret | ☐ |
| 2 | Lab notunda latency/CPU idle gözlemi (≥8 madde) | ☐ |
| 3 | Ölçüm varsa sayı | ☐ |
| 4 | Karşılaştırma tablosu | ☐ |
**Stretch:** Basit "missed event" sayacı.
### Stajyer E — Safe ISR Pattern
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | EINT → flag → main state machine | ☐ |
| 2 | UART spam yok (event'te 1 log) | ☐ |
| 3 | Yeniden giriş / bounce test prosedürü lab notunda | ☐ |
| 4 | Güvenli ISR alışkanlığı | ☐ |
**Stretch:** Critical section notu (shared değişken `volatile` + neden).


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
