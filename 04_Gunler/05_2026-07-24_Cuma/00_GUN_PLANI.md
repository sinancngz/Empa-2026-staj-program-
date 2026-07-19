# Gün 05 — Hafta 1 entegrasyon demosu

| | |
|---|---|
| **Tarih** | 2026-07-24 Cuma |
| **Hafta** | 1 |
| **Konu** | Hafta 1 entegrasyon demosu |
| **Referans** | Hafta 1 tüm örnekler |

---

## Sabah anlatımı (09:00–10:00)

GPIO + buton + UART entegrasyon ürünü

**Herkes (ortak):** Her stajyer küçük bir ürün çıkarır (Must ≥ 6 madde). Demo 8–10 dk.

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
| **A** | Interactive Status Panel | 6 Must | Stretch: Stretch varsa ayrı gösterilir. |
| **B** | Dual-Speed Knight Rider Console | 6 Must | Stretch: Stretch varsa ayrı gösterilir. |
| **C** | Binary Control Deck | 6 Must | Stretch: Stretch varsa ayrı gösterilir. |
| **D** | Chase Guard | 6 Must | Stretch: Stretch varsa ayrı gösterilir. |
| **E** | UART Command Center | 6 Must | Stretch: Stretch varsa ayrı gösterilir. |

---

## Detaylı Must / Stretch

### Stajyer A — Interactive Status Panel
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Pattern engine | ☐ |
| 2 | Buton jestleri | ☐ |
| 3 | UART status | ☐ |
| 4 | Idle timeout (10 sn) | ☐ |
| 5 | Self-test | ☐ |
| 6 | Lab checklist | ☐ |
**Stretch:** Stretch varsa ayrı gösterilir.
### Stajyer B — Dual-Speed Knight Rider Console
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Kara şimşek | ☐ |
| 2 | 3 hız | ☐ |
| 3 | UART hız komutu | ☐ |
| 4 | Buton hız | ☐ |
| 5 | Yön log | ☐ |
| 6 | Bounce-end efekti | ☐ |
**Stretch:** Stretch varsa ayrı gösterilir.
### Stajyer C — Binary Control Deck
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | 0–7 binary LED | ☐ |
| 2 | Buton inc/dec | ☐ |
| 3 | UART set (`set 5`) | ☐ |
| 4 | Long press reset | ☐ |
| 5 | Limitte `WRAP/CLAMP` seçimi | ☐ |
| 6 | Lab checklist | ☐ |
**Stretch:** Stretch varsa ayrı gösterilir.
### Stajyer D — Chase Guard
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Chase | ☐ |
| 2 | Arm/disarm | ☐ |
| 3 | Idle sleep LED off | ☐ |
| 4 | Event logger `dump` | ☐ |
| 5 | Çift tık panic (tüm LED flash) | ☐ |
| 6 | Lab checklist | ☐ |
**Stretch:** Stretch varsa ayrı gösterilir.
### Stajyer E — UART Command Center
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Alt menülü shell | ☐ |
| 2 | LED mask API | ☐ |
| 3 | Auth kilidi | ☐ |
| 4 | `status` zengin satır | ☐ |
| 5 | Hata kodları tablosu lab notunda | ☐ |
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
