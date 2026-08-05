# Gün 15 — Kaynaklar

| Kaynak | Ne için? |
|--------|----------|
| HiveMQ Cloud + Web Client | Broker / doğrulama |
| ESP32 Arduino MQTT lib (ör. PubSubClient) veya mentör iskeleti | Kod |
| Dünkü topic / JSON taslağı | Publish formatı |

### Güvenlik

```
SSID / Wi-Fi şifresi
Broker username / password
```

Bunları kaynak koda hardcode ettiysen bile **commit etme**. Placeholder kullan:

```cpp
const char* WIFI_PASS = "YOUR_PASS";
```
