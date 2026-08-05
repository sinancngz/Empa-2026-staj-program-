# Gün 15 — ESP32 → HiveMQ Demo

| | |
|---|---|
| **Tarih** | 2026-08-07 Cuma |
| **Hafta** | 3 |
| **Konu** | ESP32 Wi-Fi + MQTT; sensör verisini HiveMQ’ya publish |
| **Referans** | Dünkü HiveMQ hesap · ESP32 + sensör (mentör) |

---

## Bugün ne yapacağız?

ESP32’yi Wi-Fi ve MQTT broker’a bağlayıp sensör bilgilerini HiveMQ’ya göndereceğiz. Haftanın kapanış demosu bu.

Anlatım: [`01_Anlatim.md`](01_Anlatim.md)  
Görevler: [`02_Gorevler.md`](02_Gorevler.md)

---

## Günlük ritim

| Saat | Aktivite |
|------|----------|
| 09:00–09:30 | ESP32 Wi-Fi + program akışı + callback |
| 09:30–12:30 | WiFi + MQTT bağlantı; ilk publish |
| 13:30–14:30 | Sensör entegrasyonu + JSON |
| 14:30–16:00 | Final görev + demo hazırlığı |
| 16:00–16:45 | Kısa demolar |
| 16:45–17:00 | Stand-up + teslim |

---

## Anlatım özeti

- `WiFi.begin` → IP → MQTT Connected  
- Kod iskeleti: WiFi → MQTT → loop → publish / callback  
- JSON telemetri + HiveMQ doğrulama  

Detay: [`01_Anlatim.md`](01_Anlatim.md)

---

## Görevler

**Son görev:** ESP32 ile sensör verisini HiveMQ’ya yollamak.  
Detay: [`02_Gorevler.md`](02_Gorevler.md)

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/gunluk_rapor.md
└── proje/          # ESP32 firmware (secret’sız)
```
