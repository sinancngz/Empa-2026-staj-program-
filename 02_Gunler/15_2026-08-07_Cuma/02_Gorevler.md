# Gün 15 — Görevler (ESP32 → HiveMQ)

Anlatım: [`01_Anlatim.md`](01_Anlatim.md)  
Dün: topic + JSON tasarımın hazır olmalı.

**Haftanın son görevi:** ESP32 ile sensör bilgilerini HiveMQ’ya yollamak.

---

## Ortak hazırlık

- [ ] ESP32 kartı / USB  
- [ ] Wi-Fi SSID + şifre (mentör)  
- [ ] HiveMQ host, port, user, pass  
- [ ] Dünkü Web Client çalışıyor  
- [ ] Sensör bağlantısı net (veya mentörün onayladığı ölçüm kaynağı)  

**Git’e yazma:** Wi-Fi şifresi, broker şifresi, token.

---

## Görev A — Wi-Fi + MQTT bağlantısı

1. `WiFi.begin` ile ağa bağlan; Serial’de IP yaz.  
2. MQTT client ile broker’a bağlan (`1883` veya `8883` + TLS — mentör).  
3. Serial’de `MQTT connected` benzeri net log.  
4. Web Client’tan bağımsız, önce sabit string publish dene:

```
topic:   staj/<ad>/telemetry
payload: {"hello":"esp32"}
```

| # | Madde | Yapıldı |
|---|-------|---------|
| 1 | Wi-Fi OK + IP | ☐ |
| 2 | MQTT connected | ☐ |
| 3 | Test publish Web Client’ta görüldü | ☐ |

---

## Ana / Final görev — Sensör → HiveMQ

### İstenenler

1. ESP32’de sensör oku (sıcaklık, nem, ivme… mentörün verdiği).  
2. JSON payload oluştur (en az **2 alan**).  
3. Periyodik publish (ör. 1–2 sn).  
4. HiveMQ Web Client’ta kendi topic’ini dinle; canlı veri gör.  
5. Fiziksel etki ile değeri değiştir (nefes, el, hareket) — sahte sabit sayı olmasın.  
6. Kısa demo sun.

### Örnek çıktı (Web Client)

```
staj/ayse/telemetry
{"temp":28.14,"hum":47.2}

staj/ayse/telemetry
{"temp":28.51,"hum":52.0}
```

Serial örneği:

```
WiFi OK  IP=192.168.1.42
MQTT connected
PUB staj/ayse/telemetry {"temp":28.14,"hum":47.2}
```

### Yapılacaklar

| # | Madde | Yapıldı |
|---|-------|---------|
| 1 | Sensör okuma çalışıyor | ☐ |
| 2 | JSON en az 2 alan | ☐ |
| 3 | Periyodik publish | ☐ |
| 4 | Web Client’ta canlı izleme | ☐ |
| 5 | Değer fiziksel olarak değişiyor | ☐ |
| 6 | Demo (5–8 dk) | ☐ |

### Kabul

- [ ] Zincir uçtan uca: sensör → ESP32 → HiveMQ → ekran  
- [ ] Topic çakışmıyor (`staj/<ad>/...`)  
- [ ] Secret commit yok  
- [ ] Mentör demoyu gördü  

---

## Yan görev 1 — Status + Last Will

- Bağlanınca `staj/<ad>/status` → `online` (retain).  
- Last will → `offline`.  
- ESP32’yi çekince / resetleyince Web Client’ta `offline` görünür mü?

| # | Madde | Yapıldı |
|---|-------|---------|
| 1 | online retain | ☐ |
| 2 | will / offline gözlemi | ☐ |

---

## Yan görev 2 — Subscribe + callback

- `staj/<ad>/cmd` topic’ine subscribe.  
- Web Client’tan `led:on` / `led:off` (veya `ping`) gönder.  
- Callback Serial’de (ve mümkünse LED’de) tepki versin.  
- `client.loop()` çağrıldığından emin ol.

| # | Madde | Yapıldı |
|---|-------|---------|
| 1 | Subscribe + callback log | ☐ |
| 2 | Web’den komut → ESP32 tepkisi | ☐ |

---

## Teorik Sorular (Cevapları rapora yaz)

**1.** `WiFi.begin` sonrası MQTT’den önce neden IP alınmasını beklersin?


**2.** Program akışında `MQTT Bağlan` ile `Loop` arasına neden bazen `Subscribe` konur?


**3.** `client.loop()` (veya eşdeğeri) çağrılmazsa callback neden çalışmaz?


**4.** Callback’e gelen `topic` ve `payload` ne anlama gelir? Bir örnek yaz.


**5.** Telemetri için QoS 0 seçtiysen demo’da bir paket kaybı felaket midir? Neden?


**6.** JSON’da alan adı kullanmak dashboard tarafında neden işe yarar?


**7.** Aynı HiveMQ’da iki stajyer aynı topic’e publish ederse ne olur? Nasıl önlersin?


**8.** Wi-Fi kopunca ne yapmalısın? (reconnect fikrini 2–3 cümle)


---

## Demo checklist (sunum)

- [ ] Bir cümle: büyük resim  
- [ ] Serial: WiFi + MQTT  
- [ ] Web Client: canlı JSON  
- [ ] Fiziksel değişim  
- [ ] (Bonus) status / callback  

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/
│   └── gunluk_rapor.md    # teori + demo gözlemi + örnek JSON
└── proje/
    └── (ESP32 kodu — şifreler yok / örnek placeholder)
```
