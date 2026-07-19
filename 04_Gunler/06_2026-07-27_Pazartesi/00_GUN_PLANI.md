# Gün 06 — Timer tabanlı zamanlama omurgası

| | |
|---|---|
| **Tarih** | 2026-07-27 Pazartesi |
| **Hafta** | 2 |
| **Konu** | Timer tabanlı zamanlama omurgası |
| **Referans** | `Examples/TIMER1n/` |

---

## Sabah anlatımı (09:00–10:00)

Period match, tick, yazılım task'leri

**Herkes (ortak):** Timer tick omurgası kur; busy-wait yerine zaman tabanlı görev.

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
| **A** | Scheduler Lite | 4 Must | Stretch: Task overrun sayacı. |
| **B** | IRQ Blink FSM | 4 Must | Stretch: One-shot "pulse 150 ms" state'i. |
| **C** | Dual Timebase | 4 Must | Stretch: Periyotları runtime komutla değiştir. |
| **D** | Input-timed OneShot | 4 Must | Stretch: Queue: basılı tutarken tekrar tetikleme politikası (ignore/r… |
| **E** | Adaptive Period | 4 Must | Stretch: "Auto": belirli sürede basılmazsa yavaş kademeye dön. |

---

## Detaylı Must / Stretch

### Stajyer A — Scheduler Lite
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Period match ile 1 ms veya sabit tick | ☐ |
| 2 | Yazılımda 10/100/1000 ms task'ler | ☐ |
| 3 | LED task | ☐ |
| 4 | UART heartbeat | ☐ |
**Stretch:** Task overrun sayacı.
### Stajyer B — IRQ Blink FSM
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Timer IRQ LED FSM (OFF/ON/FAST) | ☐ |
| 2 | Butonla state | ☐ |
| 3 | UART state adı | ☐ |
| 4 | Temiz FSM geçişleri | ☐ |
**Stretch:** One-shot "pulse 150 ms" state'i.
### Stajyer C — Dual Timebase
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | İki bağımsız periyot (ör. 200 ms UI, 1000 ms log) | ☐ |
| 2 | Tek timer tick'ten türetilsin | ☐ |
| 3 | Her ikisi de görünür (LED + UART) | ☐ |
| 4 | Tick omurgası | ☐ |
**Stretch:** Periyotları runtime komutla değiştir.
### Stajyer D — Input-timed OneShot
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Buton→one-shot LED N ms | ☐ |
| 2 | İptal (ikinci basış) | ☐ |
| 3 | Kalan süre UART | ☐ |
| 4 | Timer entegrasyonu | ☐ |
**Stretch:** Queue: basılı tutarken tekrar tetikleme politikası (ignore/replace).
### Stajyer E — Adaptive Period
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | 3 kademe period | ☐ |
| 2 | Kademe LED bar | ☐ |
| 3 | Geçişte timer yeniden kurulum | ☐ |
| 4 | Log | ☐ |
**Stretch:** "Auto": belirli sürede basılmazsa yavaş kademeye dön.


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
