# Gün 07 — FRT ölçüm laboratuvarı

| | |
|---|---|
| **Tarih** | 2026-07-28 Salı |
| **Hafta** | 2 |
| **Konu** | FRT ölçüm laboratuvarı |
| **Referans** | `Examples/FRT/` |

---

## Sabah anlatımı (09:00–10:00)

Free Running Timer ile süre ölçümü

**Herkes (ortak):** FRT ile zaman ölçümü; istatistik ve kalibrasyon alışkanlığı.

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
| **A** | Interval Analyzer | 4 Must | Stretch: Histogram 4 kova. |
| **B** | Press Profiler | 4 Must | Stretch: Kalibrasyon sonucu lab'a tablo. |
| **C** | Countdown Engine | 4 Must | Stretch: Pause/resume. |
| **D** | Reaction Lab | 4 Must | Stretch: High-score tut. |
| **E** | Uptime + Drift Note | 4 Must | Stretch: Soft RTC benzeri gün sayacı (lab). |

---

## Detaylı Must / Stretch

### Stajyer A — Interval Analyzer
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Basış aralıkları: last / min / max / avg | ☐ |
| 2 | En az 10 örnek | ☐ |
| 3 | UART tablo | ☐ |
| 4 | FRT kullanımı | ☐ |
**Stretch:** Histogram 4 kova.
### Stajyer B — Press Profiler
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | SHORT/LONG sınırını ölçerek kalibre et | ☐ |
| 2 | Eşikleri runtime set komutu | ☐ |
| 3 | FRT kullanımı | ☐ |
| 4 | Kalibrasyon akışı | ☐ |
**Stretch:** Kalibrasyon sonucu lab'a tablo.
### Stajyer C — Countdown Engine
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Ayarlanabilir countdown (UART `cd 15`) | ☐ |
| 2 | LED progress | ☐ |
| 3 | İptal | ☐ |
| 4 | `DONE/ABORT` | ☐ |
**Stretch:** Pause/resume.
### Stajyer D — Reaction Lab
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Random bekleme (yazılım) + LED stimulus | ☐ |
| 2 | Reaction ms | ☐ |
| 3 | Early-press fail | ☐ |
| 4 | 5 deneme özeti | ☐ |
**Stretch:** High-score tut.
### Stajyer E — Uptime + Drift Note
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | mm:ss uptime | ☐ |
| 2 | Her 60 sn marker | ☐ |
| 3 | FRT ile beklenen vs ölçülen kaba drift notu | ☐ |
| 4 | Lab kaydı | ☐ |
**Stretch:** Soft RTC benzeri gün sayacı (lab).


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
