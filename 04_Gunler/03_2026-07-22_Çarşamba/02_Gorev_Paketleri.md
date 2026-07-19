# Gün 03 — Görev Paketleri

**Tarih:** 2026-07-22 Çarşamba  
**Konu:** UART protokolü (polling)

> Her stajyer **kendi paketini** yapar. Kopyalama yok.

---

## Stajyer A — Telemetry Tick

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | 1 Hz sayaç + uptime | ☐ |
| 2 | Buton state tek satır CSV/JSON-ish | ☐ |
| 3 | `pause`/`resume` komutları | ☐ |
| 4 | ERR/OK standardı | ☐ |

**Stretch:** Örnekleme periyodu komutla değişsin (`rate 500`).

**Teslim yolu:** `teslimler/Stajyer_A/`

---

## Stajyer B — Event Logger

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Buton event ring buffer (en az 16) | ☐ |
| 2 | `dump` komutu ile UART'a bas | ☐ |
| 3 | Buffer overflow sayacı | ☐ |
| 4 | ERR/OK standardı | ☐ |

**Stretch:** `clear` + timestamp (yazılım ms).

**Teslim yolu:** `teslimler/Stajyer_B/`

---

## Stajyer C — LED Script

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Komutlar: `on N`, `off N`, `mask 0x..`, `status` | ☐ |
| 2 | Geçersiz komutta usage | ☐ |
| 3 | ERR/OK standardı | ☐ |
| 4 | Parser iskeleti | ☐ |

**Stretch:** `seq 1,2,3,1` ile kısa script çalıştır.

**Teslim yolu:** `teslimler/Stajyer_C/`

---

## Stajyer D — Remote Console

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | `1`/`0` LED, `b` buton oku, `i` info (build tag/isim) | ☐ |
| 2 | Komut echo | ☐ |
| 3 | ERR/OK standardı | ☐ |
| 4 | Parser iskeleti | ☐ |

**Stretch:** Şifreli giriş: önce `auth 1234` olmadan yazma komutları reddedilsin.

**Teslim yolu:** `teslimler/Stajyer_D/`

---

## Stajyer E — Menu Shell

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | `h/l/s/m` menü + alt menü (LED menü / SYS menü) | ☐ |
| 2 | Breadcrumb prompt (`MAIN>` / `LED>`) | ☐ |
| 3 | ERR/OK standardı | ☐ |
| 4 | Parser iskeleti | ☐ |

**Stretch:** `history` son 5 komut.

**Teslim yolu:** `teslimler/Stajyer_E/`
