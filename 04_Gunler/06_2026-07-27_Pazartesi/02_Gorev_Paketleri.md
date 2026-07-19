# Gün 06 — Görev Paketleri

**Tarih:** 2026-07-27 Pazartesi  
**Konu:** Timer tabanlı zamanlama omurgası

> Her stajyer **kendi paketini** yapar. Kopyalama yok.

---

## Stajyer A — Scheduler Lite

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Period match ile 1 ms veya sabit tick | ☐ |
| 2 | Yazılımda 10/100/1000 ms task'ler | ☐ |
| 3 | LED task | ☐ |
| 4 | UART heartbeat | ☐ |

**Stretch:** Task overrun sayacı.

**Teslim yolu:** `teslimler/Stajyer_A/`

---

## Stajyer B — IRQ Blink FSM

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Timer IRQ LED FSM (OFF/ON/FAST) | ☐ |
| 2 | Butonla state | ☐ |
| 3 | UART state adı | ☐ |
| 4 | Temiz FSM geçişleri | ☐ |

**Stretch:** One-shot "pulse 150 ms" state'i.

**Teslim yolu:** `teslimler/Stajyer_B/`

---

## Stajyer C — Dual Timebase

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | İki bağımsız periyot (ör. 200 ms UI, 1000 ms log) | ☐ |
| 2 | Tek timer tick'ten türetilsin | ☐ |
| 3 | Her ikisi de görünür (LED + UART) | ☐ |
| 4 | Tick omurgası | ☐ |

**Stretch:** Periyotları runtime komutla değiştir.

**Teslim yolu:** `teslimler/Stajyer_C/`

---

## Stajyer D — Input-timed OneShot

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Buton→one-shot LED N ms | ☐ |
| 2 | İptal (ikinci basış) | ☐ |
| 3 | Kalan süre UART | ☐ |
| 4 | Timer entegrasyonu | ☐ |

**Stretch:** Queue: basılı tutarken tekrar tetikleme politikası (ignore/replace).

**Teslim yolu:** `teslimler/Stajyer_D/`

---

## Stajyer E — Adaptive Period

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | 3 kademe period | ☐ |
| 2 | Kademe LED bar | ☐ |
| 3 | Geçişte timer yeniden kurulum | ☐ |
| 4 | Log | ☐ |

**Stretch:** "Auto": belirli sürede basılmazsa yavaş kademeye dön.

**Teslim yolu:** `teslimler/Stajyer_E/`
