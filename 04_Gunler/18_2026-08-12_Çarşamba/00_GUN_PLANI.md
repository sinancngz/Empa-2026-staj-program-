# Gün 18 — MQTT oturumu

| | |
|---|---|
| **Tarih** | 2026-08-12 Çarşamba |
| **Hafta** | 4 |
| **Konu** | MQTT oturumu |
| **Referans** | `tiremo_app_net.c` · `Examples/TiremoCortex/` |

---

## Sabah anlatımı (09:00–10:00)

Broker connect, publish, reconnect

**Herkes (ortak):** MQTT connect + publish. Secret commit yok.

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
| **A** | Hello Cloud | 4 Must | Stretch: Will/offline mesajı (broker destekliyorsa). |
| **B** | Temp Publisher | 4 Must | Stretch: Değişince publish (delta). |
| **C** | Climate Publisher | 4 Must | Stretch: Pretty vs compact. |
| **D** | Battery Publisher | 4 Must | Stretch: Crit seviyesi ayrı topic. |
| **E** | Connection Observer | 4 Must | Stretch: State geçiş tablosu. |

---

## Detaylı Must / Stretch

### Stajyer A — Hello Cloud
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Connect + hello publish | ☐ |
| 2 | Broker kanıtı | ☐ |
| 3 | Reconnect 1 deneme | ☐ |
| 4 | Oturum iskeleti | ☐ |
**Stretch:** Will/offline mesajı (broker destekliyorsa).
### Stajyer B — Temp Publisher
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Periyodik temp | ☐ |
| 2 | Topic şeması doküman | ☐ |
| 3 | QoS notu | ☐ |
| 4 | Publish kanıtı | ☐ |
**Stretch:** Değişince publish (delta).
### Stajyer C — Climate Publisher
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Temp+RH JSON | ☐ |
| 2 | Timestamp/uptime | ☐ |
| 3 | Hata alanı | ☐ |
| 4 | Publish kanıtı | ☐ |
**Stretch:** Pretty vs compact.
### Stajyer D — Battery Publisher
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | mV + LOW flag cloud'a | ☐ |
| 2 | Yerel LED ile tutarlılık | ☐ |
| 3 | Publish kanıtı | ☐ |
| 4 | Doküman | ☐ |
**Stretch:** Crit seviyesi ayrı topic.
### Stajyer E — Connection Observer
| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | State log (INIT/WIFI/MQTT/PUB/ERR) | ☐ |
| 2 | LED map | ☐ |
| 3 | Hata sayacı | ☐ |
| 4 | Observer | ☐ |
**Stretch:** State geçiş tablosu.


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
