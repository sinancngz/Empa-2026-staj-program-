# Gün 16 — Kod tabanı haritalama

| | |
|---|---|
| **Tarih** | 2026-08-10 Pazartesi |
| **Hafta** | 4 |
| **Konu** | Kod tabanı haritalama |
| **Referans** | `Examples/TiremoCortex/` |

---

## Sabah anlatımı (09:00–10:00)

TiremoCortex kod tabanı derin inceleme

**Herkes (ortak):** Build/flash; call graph; kritik dosyalar. Credential secret commit yok.

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
| **A** | Bring-up + Trace | 4 Must | Stretch: Bir alarmın tetik zincirini satır satır. |
| **B** | Sensor Contract Sheet | 4 Must | Stretch: `SensorData_t` alan eşlemesi. |
| **C** | Alarm Archaeology | 4 Must | Stretch: Bir eşiği güvenli değiştirip davranış kanıtı. |
| **D** | LED Semantics Map | 4 Must | Stretch: Eksik LED senaryosu öner (1 paragraf). |
| **E** | Config Flag Matrix | 4 Must | Stretch: İki flag birlikte açıkken gözlem. |

---

## Detaylı Must / Stretch

### Stajyer A — Bring-up + Trace
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Build/flash | ☐ |
| 2 | Button dump | ☐ |
| 3 | Call graph (prv→app→sensor) | ☐ |
| 4 | 10 kritik dosya listesi | ☐ |
**Stretch:** Bir alarmın tetik zincirini satır satır.
### Stajyer B — Sensor Contract Sheet
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | UART alanları tablo (birim, kaynak dosya, OK flag) | ☐ |
| 2 | Eksik/garip alan notu | ☐ |
| 3 | Doküman | ☐ |
| 4 | Bring-up | ☐ |
**Stretch:** `SensorData_t` alan eşlemesi.
### Stajyer C — Alarm Archaeology
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Tüm eşiklerin path+satır | ☐ |
| 2 | Varsayılan değerler | ☐ |
| 3 | Nasıl değişir | ☐ |
| 4 | Doküman | ☐ |
**Stretch:** Bir eşiği güvenli değiştirip davranış kanıtı.
### Stajyer D — LED Semantics Map
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Her status LED anlamı | ☐ |
| 2 | Hangi state'te yanar tablosu | ☐ |
| 3 | Doküman | ☐ |
| 4 | Bring-up | ☐ |
**Stretch:** Eksik LED senaryosu öner (1 paragraf).
### Stajyer E — Config Flag Matrix
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | `EMPA_*` flag'leri × davranış matrisi | ☐ |
| 2 | Yanlış kombinasyon riskleri | ☐ |
| 3 | Doküman | ☐ |
| 4 | Bring-up | ☐ |
**Stretch:** İki flag birlikte açıkken gözlem.


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
