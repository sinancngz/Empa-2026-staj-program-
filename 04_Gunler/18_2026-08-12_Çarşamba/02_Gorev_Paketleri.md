# Gün 18 — Görev Paketleri

**Tarih:** 2026-08-12 Çarşamba  
**Konu:** MQTT oturumu

> Her stajyer **kendi paketini** yapar. Kopyalama yok.

---

## Stajyer A — Hello Cloud

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Connect + hello publish | ☐ |
| 2 | Broker kanıtı | ☐ |
| 3 | Reconnect 1 deneme | ☐ |
| 4 | Oturum iskeleti | ☐ |

**Stretch:** Will/offline mesajı (broker destekliyorsa).

**Teslim yolu:** `teslimler/Stajyer_A/`

---

## Stajyer B — Temp Publisher

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Periyodik temp | ☐ |
| 2 | Topic şeması doküman | ☐ |
| 3 | QoS notu | ☐ |
| 4 | Publish kanıtı | ☐ |

**Stretch:** Değişince publish (delta).

**Teslim yolu:** `teslimler/Stajyer_B/`

---

## Stajyer C — Climate Publisher

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | Temp+RH JSON | ☐ |
| 2 | Timestamp/uptime | ☐ |
| 3 | Hata alanı | ☐ |
| 4 | Publish kanıtı | ☐ |

**Stretch:** Pretty vs compact.

**Teslim yolu:** `teslimler/Stajyer_C/`

---

## Stajyer D — Battery Publisher

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | mV + LOW flag cloud'a | ☐ |
| 2 | Yerel LED ile tutarlılık | ☐ |
| 3 | Publish kanıtı | ☐ |
| 4 | Doküman | ☐ |

**Stretch:** Crit seviyesi ayrı topic.

**Teslim yolu:** `teslimler/Stajyer_D/`

---

## Stajyer E — Connection Observer

| # | Must maddesi | Durum |
|---|--------------|-------|
| 1 | State log (INIT/WIFI/MQTT/PUB/ERR) | ☐ |
| 2 | LED map | ☐ |
| 3 | Hata sayacı | ☐ |
| 4 | Observer | ☐ |

**Stretch:** State geçiş tablosu.

**Teslim yolu:** `teslimler/Stajyer_E/`
