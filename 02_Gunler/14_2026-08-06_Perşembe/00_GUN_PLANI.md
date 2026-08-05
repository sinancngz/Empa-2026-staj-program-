# Gün 14 — IoT & MQTT Temelleri

| | |
|---|---|
| **Tarih** | 2026-08-06 Perşembe |
| **Hafta** | 3 |
| **Konu** | IoT büyük resim, TCP/IP kısa, MQTT + HiveMQ |
| **Referans** | HiveMQ Cloud / Web Client (mentör) |

---

## Bugün ne yapacağız?

IoT ve MQTT’nin mantığını öğreneceğiz. ESP32 yazmadan önce browser’dan HiveMQ ile publish / subscribe deneyeceğiz. Yarın sensör verisini ESP32 ile broker’a yollayacağız.

Anlatım: [`01_Anlatim.md`](01_Anlatim.md)  
Görevler: [`02_Gorevler.md`](02_Gorevler.md)

---

## Günlük ritim

| Saat | Aktivite |
|------|----------|
| 09:00–09:15 | IoT büyük resim + broker |
| 09:15–09:30 | TCP/IP (IP, port, client/server) |
| 09:30–10:15 | MQTT, topic, pub/sub |
| 10:15–10:45 | QoS, retain, last will, JSON |
| 10:45–12:30 | HiveMQ Web Client alıştırma |
| 13:30–14:30 | Topic tasarımı + teori soruları |
| 14:30–16:30 | Görevler / mentör turu |
| 16:30–17:00 | Stand-up + teslim |

---

## Anlatım özeti

1. IoT zinciri (sensör → ESP32 → Wi-Fi → broker → dashboard)  
2. IP / port / client–server  
3. MQTT: publisher, subscriber, broker, topic  
4. QoS, retain, last will  
5. JSON payload  
6. HiveMQ Web Client  

Detay: [`01_Anlatim.md`](01_Anlatim.md)

---

## Görevler

HiveMQ browser pratiği + topic tasarımı + teori.  
Detay: [`02_Gorevler.md`](02_Gorevler.md)

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/gunluk_rapor.md
└── proje/          # ekran görüntüsü / not (ESP32 yarın)
```
