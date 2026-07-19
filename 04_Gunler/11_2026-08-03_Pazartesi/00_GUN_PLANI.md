# Gün 11 — SHT40 ürünleştirme

| | |
|---|---|
| **Tarih** | 2026-08-03 Pazartesi |
| **Hafta** | 3 |
| **Konu** | SHT40 ürünleştirme |
| **Referans** | `Examples/I2Cn/I2Cn_SHT40/` |

---

## Sabah anlatımı (09:00–10:00)

I2C SHT40 sıcaklık/nem

**Herkes (ortak):** SHT40 okuma; hata/retry; ürün seviyesinde log.

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
| **A** | Climate Stream | 4 Must | Stretch: Ölçüm periyodu komutu. |
| **B** | Comfort Zones | 4 Must | Stretch: "Comfort score" 0–100 kaba. |
| **C** | Unit & Format Layer | 4 Must | Stretch: JSON satır opsiyonu. |
| **D** | Hot Alarm Engine | 4 Must | Stretch: Warning vs Critical iki eşik. |
| **E** | Health Check | 4 Must | Stretch: Fail counter threshold → safe mode (ölçümü durdur). |

---

## Detaylı Must / Stretch

### Stajyer A — Climate Stream
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Temp+RH 1 Hz + OK flag | ☐ |
| 2 | CSV | ☐ |
| 3 | Hata retry (1–2) | ☐ |
| 4 | `ERR:SHT` | ☐ |
**Stretch:** Ölçüm periyodu komutu.
### Stajyer B — Comfort Zones
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | RH ve temp için zone LED | ☐ |
| 2 | Histerezis | ☐ |
| 3 | Zone event log | ☐ |
| 4 | I2C okuma | ☐ |
**Stretch:** "Comfort score" 0–100 kaba.
### Stajyer C — Unit & Format Layer
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | °C/°F + RH | ☐ |
| 2 | Tek `print` API | ☐ |
| 3 | Buton/unit komutu | ☐ |
| 4 | Format katmanı | ☐ |
**Stretch:** JSON satır opsiyonu.
### Stajyer D — Hot Alarm Engine
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Eşik + histerezis | ☐ |
| 2 | Latch + ack | ☐ |
| 3 | LED pattern | ☐ |
| 4 | UART | ☐ |
**Stretch:** Warning vs Critical iki eşik.
### Stajyer E — Health Check
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Init fail / read fail ayrımı | ☐ |
| 2 | Boot'ta self-check | ☐ |
| 3 | Periyodik "sensor alive" LED heartbeat | ☐ |
| 4 | Sağlık izleme | ☐ |
**Stretch:** Fail counter threshold → safe mode (ölçümü durdur).


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
