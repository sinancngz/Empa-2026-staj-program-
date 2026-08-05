# ESP32, Wi-Fi ve MQTT Uygulama Mantığı

**Gün 15 · 7 Ağustos 2026 · Tiremo Cortex**

Bu döküman, MQTT teorisinin ESP32 üzerinde nasıl yaşama geçtiğini anlatır: Wi-Fi bağlantısından broker oturumuna, program akışından callback modeline ve JSON telemetriye kadar.

---

## 1. Büyük resmin cihaz tarafı

Önceki günde zincir şu şekilde kurulmuştu:

```
Sensör → ESP32 → Wi-Fi → Internet → MQTT Broker (HiveMQ) → Dashboard / telefon
```

ESP32 bu zincirde iki işi birden yapar:

1. Sensörü okuyan **ölçüm birimi**  
2. Broker’a bağlanan **MQTT client**

Yani kart artık yalnızca yerel UART’a yazan bir MCU değildir; ölçümü alıp internetteki bir topic’e bırakır. Web Client veya başka bir abone aynı topic’i dinlediğinde veriyi görür.

---

## 2. ESP32 Wi-Fi mantığı

MQTT, TCP üzerinden çalışır. TCP için önce cihazın IP ağına çıkmış olması gerekir. Bu yüzden sıra her zaman aynıdır: önce Wi-Fi, sonra MQTT.

```
ESP32
   │
   │  WiFi.begin(ssid, password)
   ▼
Router
   │
   │  DHCP ile IP alır
   ▼
Yerel IP (örnek: 192.168.1.42)
   │
   │  MQTT client.connect(host, port, ...)
   ▼
Broker ile oturum (port 1883 veya 8883)
   │
   ▼
MQTT Connected
```

### Wi-Fi adımı

`WiFi.begin` ile ağın adı (SSID) ve şifresi verilir. Bağlantı anlık olmak zorunda değildir; sürücü router ile el sıkışır, kimlik doğrular ve DHCP üzerinden bir IP alır. IP gelmeden broker’a gitmeye çalışmak çoğu zaman başarısız olur.

Bağlantı durumunu seri porttan izlemek teşhis için kritiktir: “Wi-Fi bağlı mı?”, “IP nedir?” sorularının cevabı net görünmelidir.

### MQTT adımı

Wi-Fi hazır olduktan sonra MQTT kütüphanesine broker bilgileri verilir:

- host (HiveMQ adresi)  
- port (`1883` veya TLS için `8883`)  
- kullanıcı adı / şifre (Cloud ortamında)  
- client id (broker’ın bu oturumu ayırt etmesi için)

`connect` başarılıysa cihaz publish ve subscribe yapabilir. Bağlantı sonradan düşebilir; sağlam uygulamalarda Wi-Fi ve MQTT için yeniden bağlanma (reconnect) mantığı bulunur. En azından kopmanın log’da görünmesi, sorunun sensörde mi yoksa ağda mı olduğunu ayırmaya yardım eder.

Kimlik bilgileri (Wi-Fi şifresi, broker parolası) kaynağa gömülse bile sürüm kontrolüne açık şekilde yazılmamalıdır. Bunlar ortam sırrıdır.

---

## 3. Program akışı

ESP32 üzerindeki yazılımın iskeleti, ağ yaşam döngüsünü yansıtır:

```
Başla
  │
  ▼
Wi-Fi’ye bağlan
  │
  ▼
MQTT broker’a bağlan
  │
  ▼
Gerekirse topic’lere subscribe ol
  │
  ▼
┌────────────── Ana döngü ──────────────┐
│  Sensörü oku                          │
│  JSON payload oluştur                 │
│  Publish et                           │
│  Ağ olaylarını işle (client.loop)     │
│  Gelen mesaj varsa callback çalışır   │
└───────────────────────────────────────┘
```

`setup` benzeri başlangıç bölümünde bir kerelik işler yapılır: seri port, Wi-Fi, MQTT, isteğe bağlı subscribe ve callback kaydı.

`loop` benzeri sürekli bölümde ise iki tür iş vardır:

- **Üretim:** ölç, paketle, publish et  
- **Dinleme:** kütüphanenin ağ tamponunu işlemesi; böylece gelen publish’ler callback’e düşer  

Kavramsal örnek:

```cpp
void setup() {
  Serial.begin(115200);
  wifiConnect();
  mqttConnect();
  client.setCallback(onMqttMessage);
  client.subscribe("staj/ayse/cmd");
}

void loop() {
  if (!client.connected()) {
    mqttConnect();
  }
  client.loop();

  float t = readTemp();
  float h = readHum();

  char payload[128];
  snprintf(payload, sizeof(payload),
           "{\"temp\":%.2f,\"hum\":%.1f}", t, h);

  client.publish("staj/ayse/telemetry", payload);
  delay(2000);
}
```

Bu iskelet kütüphane isimlerinden bağımsızdır. Önemli olan sıra ve sorumluluk ayrımıdır: bağlantı kurulumu bir yerde, periyodik telemetri başka yerde, gelen komutların işlenmesi callback’te.

Sensör tarafı projeye göre değişir: sıcaklık-nem, ivme veya mentörün bağladığı başka bir kaynak. Mantık aynı kalır — ölçülen değerler JSON alanlarına dönüşür ve topic’e yazılır.

---

## 4. Callback mantığı

MQTT’de gelen mesajları sürekli elle sorgulamak yerine olay tabanlı model kullanılır.

Yanlış yönelim, “acaba mesaj geldi mi?” diye ana döngüde özel bir protokol parse etmeye çalışmaktır. Doğru yönelim şudur:

```
loop()
   │
   ▼
client.loop()          →  soketten oku, MQTT paketlerini işle
   │
   │  (abonelikte yeni publish varsa)
   ▼
callback(topic, payload)
```

Callback’e genelde iki bilgi gelir:

| Parametre | Anlam |
|-----------|--------|
| **topic** | Mesajın geldiği kanal |
| **payload** | Kanalın taşıdığı içerik (çoğu zaman metin / JSON) |

```cpp
void onMqttMessage(char* topic, byte* payload, unsigned int length) {
  Serial.printf("MSG %s: ", topic);
  for (unsigned i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
}
```

Callback’in çalışması için üç koşul bir araya gelmelidir:

1. Broker’a bağlı olmak  
2. İlgili topic’e subscribe etmiş olmak  
3. Ana döngüde `client.loop()` (veya eşdeğeri) ile kütüphaneye nefes aldırmak  

Yalnızca publish yapan bir cihaz için callback zorunlu değildir. Uzaktan komut, eşik güncelleme veya LED kontrolü gibi dinleme senaryolarında ise callback mimarinin merkezidir.

Bu model, kesme veya olay geri çağrımı ile aynı fikirdir: “sürekli sor” yerine “gelince haber ver”.

---

## 5. JSON telemetri ve status

Broker’a giden gövde (payload) okunabilir olmalıdır. Tipik bir telemetri satırı:

```json
{"temp":28.1,"hum":55.0,"ax":2,"ay":-1,"az":64}
```

Topic’ler anlamı ayırır:

```
staj/<ad>/telemetry     →  periyodik ölçümler
staj/<ad>/status        →  online / offline
staj/<ad>/cmd           →  cihaza giden komutlar (subscribe)
```

Bağlantı kurulduğunda status topic’ine `online` yayınlamak, izleyen tarafa cihazın ayağa kalktığını söyler. Bu mesajın retain ile gitmesi, sonradan açılan panellerin hemen durumu görmesini sağlar.

Last Will ile aynı status topic’ine `offline` bırakılırsa, ani kopuşta broker bu mesajı yayınlar. Böylece telemetri suskunluğu ile “cihaz bilinçli olarak kapandı / koptu” bilgisi birbirinden ayrılabilir.

---

## 6. Uçtan uca doğrulama düşüncesi

Sistemin çalıştığını anlamak için yalnızca “kod derlendi” yetmez. Zincirin her halkası ayrı kontrol edilir:

1. Seri portta Wi-Fi bağlantısı ve alınan IP görünür.  
2. Seri portta MQTT oturumunun kurulduğu yazılır.  
3. Aynı broker’da Web Client, cihazın topic’ine subscribe olur.  
4. Publish edilen JSON satırları panelde akar.  
5. Fiziksel dünya değişince (sıcaklık, nem, hareket) sayılar da değişir — sabit sahte değer zinciri kanıtlamaz.

Bir halka kırıksa teşhis de oradan başlar: IP yoksa sorun Wi-Fi’dedir; IP var ama MQTT yoksa host/port/TLS/kimlik bilgisine bakılır; MQTT var ama panel boşsa topic adı veya yanlış broker kümesi kontrol edilir.

---

## 7. Sık görülen sorunların kökü

| Belirti | Sık neden |
|---------|-----------|
| Wi-Fi bağlanmıyor | SSID / şifre hatası, yalnızca 5 GHz ağ, laboratuvar ağı kısıtı |
| MQTT bağlanmıyor | Yanlış host veya port, TLS gereksinimi, kullanıcı/şifre |
| Publish “başarılı” ama panel boş | Topic yazımı farklı, başka broker’a bakılıyor |
| JSON bozuk görünüyor | Tampon taşması, kaçırılmamış tırnak, eksik süslü parantez |
| Callback hiç tetiklenmiyor | `client.loop()` yok, subscribe unutulmuş, yanlış topic |

Bu tablo, rastgele deneme-yanılma yerine sistematik bakmayı öğretir: önce bağlan, sonra yayınla, en sonda dinle.

---

## Özet

- ESP32 önce Wi-Fi ile IP alır, sonra MQTT broker’a client olarak bağlanır.  
- Yazılım iskeleti: bağlan → (subscribe) → döngüde ölç / publish / loop.  
- Callback, abone olunan topic’e mesaj geldiğinde çalışır; `client.loop()` bu mekanizmayı canlı tutar.  
- Telemetri için JSON; durum için status + isteğe bağlı retain ve last will kullanılır.  
- Doğrulama, seri log ile Web Client’ın aynı topic’te buluşmasıdır.
