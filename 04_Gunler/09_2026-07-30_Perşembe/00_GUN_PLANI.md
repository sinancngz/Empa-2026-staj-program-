# Gün 09 — Mikrofon analiz hattı

| | |
|---|---|
| **Tarih** | 2026-07-30 Perşembe |
| **Hafta** | 2 |
| **Konu** | Mikrofon analiz hattı |
| **Referans** | `Examples/ADC/ADC_Microphone/` |

---

## Sabah anlatımı (09:00–10:00)

ADC mikrofon, RMS, zone sınıflandırma

**Herkes (ortak):** Mikrofon capture + service loop; ses seviyesi sınıflandırma.

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
| **A** | RMS Pipeline | 4 Must | Stretch: RMS + peak aynı satır. |
| **B** | 3-Zone Classifier | 4 Must | Stretch: Zone süreleri sayacı. |
| **C** | Loud Alarm FSM | 4 Must | Stretch: Alarm süresi timeout auto-clear. |
| **D** | Calibration Kit | 4 Must | Stretch: `cal` komutu ile eşik yaz. |
| **E** | Peak Hold Monitor | 4 Must | Stretch: Çift window (1 sn ve 3 sn). |

---

## Detaylı Must / Stretch

### Stajyer A — RMS Pipeline
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Capture + service loop doğru | ☐ |
| 2 | RMS 2 Hz log | ☐ |
| 3 | Fail durumunda `MIC_ERR` | ☐ |
| 4 | Pipeline iskeleti | ☐ |
**Stretch:** RMS + peak aynı satır.
### Stajyer B — 3-Zone Classifier
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | SILENT/NORMAL/LOUD | ☐ |
| 2 | LED | ☐ |
| 3 | Zone değişiminde tek event log (histerezis) | ☐ |
| 4 | Sınıflandırıcı | ☐ |
**Stretch:** Zone süreleri sayacı.
### Stajyer C — Loud Alarm FSM
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | LOUD enter/exit | ☐ |
| 2 | Alarm LED pattern | ☐ |
| 3 | UART | ☐ |
| 4 | Alarm latch (buton ack ile temizle) | ☐ |
**Stretch:** Alarm süresi timeout auto-clear.
### Stajyer D — Calibration Kit
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Sessiz oda / konuşma / alkış için ≥10'ar örnek tablo | ☐ |
| 2 | Önerilen eşikler | ☐ |
| 3 | Kodda uygula | ☐ |
| 4 | Kalibrasyon raporu | ☐ |
**Stretch:** `cal` komutu ile eşik yaz.
### Stajyer E — Peak Hold Monitor
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | 3 sn window peak hold | ☐ |
| 2 | Buton reset | ☐ |
| 3 | LED "new peak" flash | ☐ |
| 4 | Log | ☐ |
**Stretch:** Çift window (1 sn ve 3 sn).


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
