# Gün 13 — Multi-sensor orchestration

| | |
|---|---|
| **Tarih** | 2026-08-05 Çarşamba |
| **Hafta** | 3 |
| **Konu** | Multi-sensor orchestration |
| **Referans** | `Examples/TiremoCortex/` + I2C + ADC örnekleri |

---

## Sabah anlatımı (09:00–10:00)

Birden fazla sensörü aynı loop'ta yönetme

**Herkes (ortak):** Kısmi fail'de diğer sensör devam; öncelik kuralları.

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
| **A** | Dual Bus Client | 4 Must | Stretch: Round-robin öncelik. |
| **B** | Power-aware Sense | 4 Must | Stretch: Kritik bataryada sadece temp. |
| **C** | Noise + Motion | 4 Must | Stretch: Birleşik `ALERT` kodu. |
| **D** | Dashboard v2 | 4 Must | Stretch: 1 Hz compact / event'te verbose. |
| **E** | Fault Injection Drill | 4 Must | Stretch: Otomatik retry backoff. |

---

## Detaylı Must / Stretch

### Stajyer A — Dual Bus Client
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | SHT40+LIS aynı loop | ☐ |
| 2 | Her sensör bağımsız OK | ☐ |
| 3 | Kısmi fail'de diğer devam | ☐ |
| 4 | Orchestration | ☐ |
**Stretch:** Round-robin öncelik.
### Stajyer B — Power-aware Sense
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Batarya düşükse ivme örnekleme yavaşlasın (policy) | ☐ |
| 2 | Log'da policy state | ☐ |
| 3 | Policy tablosu | ☐ |
| 4 | Entegrasyon | ☐ |
**Stretch:** Kritik bataryada sadece temp.
### Stajyer C — Noise + Motion
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Mic zone + shake aynı anda | ☐ |
| 2 | Çakışmada öncelik kuralı dokümante | ☐ |
| 3 | Birleşik davranış | ☐ |
| 4 | Entegrasyon | ☐ |
**Stretch:** Birleşik `ALERT` kodu.
### Stajyer D — Dashboard v2
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Tek satır: temp, RH, |a|, bat, micRMS | ☐ |
| 2 | `compact/verbose` mod | ☐ |
| 3 | Format disiplini | ☐ |
| 4 | Entegrasyon | ☐ |
**Stretch:** 1 Hz compact / event'te verbose.
### Stajyer E — Fault Injection Drill
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Kablo/simülasyon ile fail senaryoları (≥3) | ☐ |
| 2 | Beklenen log | ☐ |
| 3 | Recovery | ☐ |
| 4 | Lab raporu | ☐ |
**Stretch:** Otomatik retry backoff.


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
