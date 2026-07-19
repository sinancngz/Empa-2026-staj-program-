# Gün 17 — ESP32 AT dayanıklılık

| | |
|---|---|
| **Tarih** | 2026-08-11 Salı |
| **Hafta** | 4 |
| **Konu** | ESP32 AT dayanıklılık |
| **Referans** | `Examples/UARTn_ESP32_AT_Test/` |

---

## Sabah anlatımı (09:00–10:00)

ESP32 AT komutları, WiFi join, negatif test

**Herkes (ortak):** AT session; join/IP; fail senaryoları. Credential mentörden.

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
| **A** | AT Session Log | 4 Must | Stretch: Beklenmeyen cevap parser notu. |
| **B** | Join & IP Proof | 4 Must | Stretch: Join süresi ölçümü. |
| **C** | Negative Testing | 4 Must | Stretch: Fail sonrası recovery adımları. |
| **D** | Power/Reset Policy | 4 Must | Stretch: Soft vs hard reset farkı deneyi. |
| **E** | AT Cheat-sheet + SM | 4 Must | Stretch: Her state'te timeout. |

---

## Detaylı Must / Stretch

### Stajyer A — AT Session Log
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | AT/OK, versiyon, WiFi mode komutları log dosyası | ☐ |
| 2 | Timeline | ☐ |
| 3 | Kanıt | ☐ |
| 4 | Session disiplini | ☐ |
**Stretch:** Beklenmeyen cevap parser notu.
### Stajyer B — Join & IP Proof
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Join success + IP | ☐ |
| 2 | RSSI (varsa) | ☐ |
| 3 | Screenshot/log | ☐ |
| 4 | Kanıt paketi | ☐ |
**Stretch:** Join süresi ölçümü.
### Stajyer C — Negative Testing
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Yanlış SSID/şifre, timeout, sinyal yok (≥3 fail) | ☐ |
| 2 | Hata kodları tablosu | ☐ |
| 3 | Lab kaydı | ☐ |
| 4 | Negatif test disiplini | ☐ |
**Stretch:** Fail sonrası recovery adımları.
### Stajyer D — Power/Reset Policy
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | PWR pin power-cycle prosedürü | ☐ |
| 2 | Ne zaman reset gerekir lab | ☐ |
| 3 | Politika dokümanı | ☐ |
| 4 | Deney | ☐ |
**Stretch:** Soft vs hard reset farkı deneyi.
### Stajyer E — AT Cheat-sheet + SM
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Kullandığı AT'ler | ☐ |
| 2 | Sade state machine diyagramı (POWER→AT→WIFI) | ☐ |
| 3 | Cheat-sheet | ☐ |
| 4 | SM dokümanı | ☐ |
**Stretch:** Her state'te timeout.


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
