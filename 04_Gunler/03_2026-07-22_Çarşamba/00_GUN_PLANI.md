# Gün 03 — UART protokolü (polling)

| | |
|---|---|
| **Tarih** | 2026-07-22 Çarşamba |
| **Hafta** | 1 |
| **Konu** | UART protokolü (polling) |
| **Referans** | `Examples/UARTn/UARTn_Polling/` |

---

## Sabah anlatımı (09:00–10:00)

Framing, komut parse, help, hata cevapları

**Herkes (ortak):** Satır veya karakter tabanlı komut parser + `ERR` / `OK` cevap standardı.

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
| **A** | Telemetry Tick | 4 Must | Stretch: Örnekleme periyodu komutla değişsin (`rate 500`). |
| **B** | Event Logger | 4 Must | Stretch: `clear` + timestamp (yazılım ms). |
| **C** | LED Script | 4 Must | Stretch: `seq 1,2,3,1` ile kısa script çalıştır. |
| **D** | Remote Console | 4 Must | Stretch: Şifreli giriş: önce `auth 1234` olmadan yazma komutları redd… |
| **E** | Menu Shell | 4 Must | Stretch: `history` son 5 komut. |

---

## Detaylı Must / Stretch

### Stajyer A — Telemetry Tick
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | 1 Hz sayaç + uptime | ☐ |
| 2 | Buton state tek satır CSV/JSON-ish | ☐ |
| 3 | `pause`/`resume` komutları | ☐ |
| 4 | ERR/OK standardı | ☐ |
**Stretch:** Örnekleme periyodu komutla değişsin (`rate 500`).
### Stajyer B — Event Logger
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Buton event ring buffer (en az 16) | ☐ |
| 2 | `dump` komutu ile UART'a bas | ☐ |
| 3 | Buffer overflow sayacı | ☐ |
| 4 | ERR/OK standardı | ☐ |
**Stretch:** `clear` + timestamp (yazılım ms).
### Stajyer C — LED Script
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Komutlar: `on N`, `off N`, `mask 0x..`, `status` | ☐ |
| 2 | Geçersiz komutta usage | ☐ |
| 3 | ERR/OK standardı | ☐ |
| 4 | Parser iskeleti | ☐ |
**Stretch:** `seq 1,2,3,1` ile kısa script çalıştır.
### Stajyer D — Remote Console
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | `1`/`0` LED, `b` buton oku, `i` info (build tag/isim) | ☐ |
| 2 | Komut echo | ☐ |
| 3 | ERR/OK standardı | ☐ |
| 4 | Parser iskeleti | ☐ |
**Stretch:** Şifreli giriş: önce `auth 1234` olmadan yazma komutları reddedilsin.
### Stajyer E — Menu Shell
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | `h/l/s/m` menü + alt menü (LED menü / SYS menü) | ☐ |
| 2 | Breadcrumb prompt (`MAIN>` / `LED>`) | ☐ |
| 3 | ERR/OK standardı | ☐ |
| 4 | Parser iskeleti | ☐ |
**Stretch:** `history` son 5 komut.


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
