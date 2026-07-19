# Gün 12 — LIS2DE12 hareket zekâsı

| | |
|---|---|
| **Tarih** | 2026-08-04 Salı |
| **Hafta** | 3 |
| **Konu** | LIS2DE12 hareket zekâsı |
| **Referans** | `Examples/I2Cn/I2Cn_LIS2DE12TR/` |

---

## Sabah anlatımı (09:00–10:00)

I2C ivmeölçer, orientation, shake, fall

**Herkes (ortak):** LIS2DE12 XYZ okuma; hareket sınıflandırma.

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
| **A** | Accel Stream + |a| | 4 Must | Stretch: Ham vs mg dönüşüm notu lab. |
| **B** | Orientation FSM | 4 Must | Stretch: UNKNOWN state. |
| **C** | Shake Detector | 4 Must | Stretch: Shake yoğunluğu sayacı. |
| **D** | Fall Candidate | 4 Must | Stretch: Fall sonrası "impact" yüksek g. |
| **E** | Motion Activity | 4 Must | Stretch: UART `activity` komutu. |

---

## Detaylı Must / Stretch

### Stajyer A — Accel Stream + |a|
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | XYZ mg + |a| + OK | ☐ |
| 2 | 1 Hz/2 Hz log | ☐ |
| 3 | I2C okuma | ☐ |
| 4 | Birim dönüşümü | ☐ |
**Stretch:** Ham vs mg dönüşüm notu lab.
### Stajyer B — Orientation FSM
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | ±X/±Y/±Z dominant orientation | ☐ |
| 2 | Debounce zamanı | ☐ |
| 3 | LED map | ☐ |
| 4 | Event | ☐ |
**Stretch:** UNKNOWN state.
### Stajyer C — Shake Detector
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Δg / yüksek geçiş benzeri eşik | ☐ |
| 2 | Cooldown | ☐ |
| 3 | Latch/ack | ☐ |
| 4 | Event log | ☐ |
**Stretch:** Shake yoğunluğu sayacı.
### Stajyer D — Fall Candidate
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Free-fall benzeri düşük |a| penceresi | ☐ |
| 2 | Doğrulama süresi | ☐ |
| 3 | `FALL` | ☐ |
| 4 | False-positive notu | ☐ |
**Stretch:** Fall sonrası "impact" yüksek g.
### Stajyer E — Motion Activity
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | STILL / MOVE sınıflandırıcı | ☐ |
| 2 | LED | ☐ |
| 3 | Aktivite yüzdesi (son 10 sn) | ☐ |
| 4 | Sınıflandırıcı | ☐ |
**Stretch:** UART `activity` komutu.


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
