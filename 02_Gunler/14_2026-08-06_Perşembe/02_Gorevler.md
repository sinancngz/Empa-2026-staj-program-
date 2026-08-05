# Gün 14 — Görevler (IoT & MQTT Temelleri)

Anlatım: [`01_Anlatim.md`](01_Anlatim.md)

Bugün **ESP32 kodu zorunlu değil**. Amaç: MQTT’yi HiveMQ Web Client ile kavramak.

---

## Ortak hazırlık

- [ ] Anlatım / sunum dinlendi  
- [ ] Mentörden HiveMQ host, port, kullanıcı, şifre alındı  
- [ ] Browser’da Web Client açılıyor  
- [ ] Kendi topic önekin hazır: `staj/<ad>/...`  

> Secret’ları rapora / git’e **yazma**. Sadece “bağlandım” de.

---

## Görev 1 — HiveMQ Web Client (ana pratik)

### İstenenler

1. Broker’a bağlan.  
2. Kendi topic’ine subscribe ol: örn. `staj/ayse/hello`  
3. Aynı topic’e `hello` / `world` publish et; mesajı gör.  
4. Arkadaşının topic’ine (izinle) subscribe olup onun mesajını dinle.  
5. (İsteğe bağlı) Retain’li bir status mesajı dene; sayfayı yenileyip tekrar subscribe et — mesaj geliyor mu?

### Örnek

```
Subscribe:  staj/ayse/hello
Publish:    staj/ayse/hello   →  "world"
```

| # | Madde | Yapıldı |
|---|-------|---------|
| 1 | Broker bağlantısı OK | ☐ |
| 2 | Kendi topic pub/sub | ☐ |
| 3 | En az bir başka topic dinlendi | ☐ |
| 4 | Ekran görüntüsü rapora | ☐ |

---

## Görev 2 — Topic + JSON tasarımı

Yarın ESP32’nin göndereceği yapıyı **şimziden** yaz.

### İstenenler

1. En az 3 topic öner (temp / hum / status veya imu…).  
2. Örnek JSON payload yaz.  
3. QoS seçimini gerekçeyle not et (0 mı 1 mi?).  
4. Last will için topic + mesaj öner (`offline`).

Örnek:

```
Topics:
  staj/ayse/telemetry
  staj/ayse/status

Payload:
  {"temp":28.1,"hum":55,"battery":3.92}

QoS: 0 (telemetri)
Will: staj/ayse/status = offline (retain)
```

| # | Madde | Yapıldı |
|---|-------|---------|
| 1 | Topic listesi | ☐ |
| 2 | Örnek JSON | ☐ |
| 3 | QoS + will notu | ☐ |

---

## Yan görev — Retain farkını göster

1. Retain **kapalı** publish → yeni subscribe → boş.  
2. Retain **açık** publish → yeni subscribe → son mesaj gelir.  

Rapora iki cümleyle yaz.

| # | Madde | Yapıldı |
|---|-------|---------|
| 1 | Retain farkı gözlendi / not edildi | ☐ |

---

## Teorik Sorular (Cevapları rapora yaz)

**1.** IoT zincirinde broker neden vardır? ESP32 doğrudan telefona bağlansa ne kaybedersin?


**2.** IP ile port arasındaki fark nedir? MQTT için tipik portlar nelerdir?


**3.** Publisher, subscriber ve broker rollerini birer cümleyle anlat.


**4.** `cow/12/temp` ile `cow/13/temp` neden ayrı topic olmalı?


**5.** QoS 0 ile QoS 1 farkı nedir? Sıcaklık telemetrisi için hangisini seçersin, neden?


**6.** Retain ne işe yarar? Her mesajda retain kullanmak neden kötü fikir olabilir?


**7.** Last Will ne zaman devreye girer? `online` / `offline` senaryosunu anlat.


**8.** `28.1,55,3.92` yerine JSON kullanmanın en az 2 avantajı nedir?


**9.** Client / server açısından ESP32 ve HiveMQ kimdir?


**10.** Yarın kod yazarken ilk üç adım sırasıyla ne olmalı? (WiFi / MQTT / …)

---

## Kabul

- [ ] Web Client’ta pub/sub çalıştı  
- [ ] Topic + JSON tasarımı raporda  
- [ ] Teori soruları cevaplı  
- [ ] Credential git’te yok  

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/
│   └── gunluk_rapor.md
└── proje/
    └── (ekran görüntüsü / topic taslağı)
```
