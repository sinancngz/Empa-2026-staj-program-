# IoT, TCP/IP ve MQTT Temelleri

**Gün 14 · 6 Ağustos 2026 · Tiremo Cortex**

Bu döküman, gömülü cihazın internete çıkıp başka sistemlerle konuşmasının arkasındaki büyük resmi anlatır: sensörden başlayıp Wi-Fi, internet ve MQTT broker üzerinden dashboard’a kadar uzanan yol.

---

## 1. IoT nedir?

**IoT (Internet of Things — Nesnelerin İnterneti)**, fiziksel dünyadaki cihazların (sensörler, motorlar, kutular, makineler) internet üzerinden veri alışverişi yapabilmesidir.

Klasik bir gömülü sistemde ölçüm çoğu zaman kartın üzerinde kalır: sıcaklığı okur, UART’a basarsın, LED yakarsın. IoT’de aynı ölçüm **ağ üzerinden** başka bir yere taşınır; telefon, bilgisayar veya buluttaki bir panel bu veriyi canlı izleyebilir.

Tipik zincir şöyledir:

```
Sensör
   │
ESP32
   │ Wi-Fi
Router
   │
Internet
   │
MQTT Broker (HiveMQ)
   │
Dashboard / Telefon / Bilgisayar
```

Adım adım:

1. ESP32 (veya benzeri bir Wi-Fi’li MCU) sensörü okur.  
2. Wi-Fi ile eve / laboratuvara ait routera bağlanır ve internete çıkar.  
3. Ölçülen veriyi bir **MQTT Broker**’a gönderir.  
4. Broker’a abone olan diğer cihazlar (telefon uygulaması, web paneli, PC) bu veriyi alır.

Bu modelde kritik nokta şudur: sensör kartı ile telefonun birbirini “doğrudan tanımasına” gerek yoktur. Ortada ortak bir buluşma noktası vardır.

### Broker kavramı

**Broker**, mesajlaşmanın ortasındaki aracıdır; postacıya benzer.

- ESP32, telefonun IP adresini bilmek zorunda değildir.  
- Telefon, ESP32’nin yerel ağda olup olmadığını bilmek zorunda değildir.  
- Her iki taraf da broker’a bağlanır. Publisher mesajı broker’a bırakır; broker, o konuyu dinleyen herkese iletir.

```
ESP32 ──publish──► Broker ◄──subscribe── Telefon
                      │
                      └──► PC / Dashboard
```

Broker olmasa her cihazın diğer her cihazla ayrı bağlantı kurması gerekir. Cihaz sayısı arttıkça bu yaklaşım hızla karmaşıklaşır. IoT’de broker, sistemi ölçeklenebilir ve düzenli tutar.

---

## 2. TCP/IP temelleri

MQTT’ye geçmeden önce ağın dört temel kavramını netleştirmek yeterlidir. Derin protokol yığınına inmeye gerek yoktur.

| Kavram | Anlam |
|--------|--------|
| **IP** | Ağdaki bir cihazın adresi. Ev numarası gibi düşünülebilir. |
| **Port** | O cihazdaki servis kapısı. Aynı IP’de web, e-posta, MQTT gibi farklı hizmetler farklı portlardan dinler. |
| **Client** | Bağlantıyı başlatan taraf. |
| **Server** | Bağlantıyı bekleyen, hizmet sunan taraf. |

### Günlük örnek: web tarayıcısı

Google’a girdiğinde kabaca şu olur:

| | |
|---|---|
| Hedef | Bir sunucu IP’si (örnek biçimde `142.x.x.x`; gerçek adresler değişebilir) |
| Servis | HTTPS |
| Port | **443** |

Tarayıcı client’tır; Google’ın sunucusu server’dır. “Nereye gideceğim?” sorusunun cevabı IP, “hangi kapıdan gireceğim?” sorusunun cevabı porttur.

### MQTT örneği

| | |
|---|---|
| Broker | Dinleyen taraf; pratikte server rolündedir |
| ESP32, telefon, web client | Broker’a bağlanan client’lardır |
| Yaygın portlar | **1883** (şifresiz MQTT), **8883** (TLS/SSL ile güvenli MQTT) |

HiveMQ Cloud gibi bulut broker’larda genelde **8883** ve kullanıcı adı / şifre kullanılır. Host adı, port ve kimlik bilgileri ortamına göre mentör tarafından verilir.

Özet cümle: **IP = nereye**, **port = hangi kapı**, **MQTT client = broker’a bağlanan yazılım**.

---

## 3. MQTT nedir?

**MQTT (Message Queuing Telemetry Transport)**, özellikle IoT için tasarlanmış hafif bir mesajlaşma protokolüdür. Bant genişliği ve işlem gücü sınırlı cihazlarda bile çalışacak şekilde sade tutulmuştur.

MQTT’nin kalbi **publish / subscribe** modelidir:

```
Publisher
     │
     │  publish
     ▼
  HiveMQ (Broker)
     ▲
     │  subscribe
     │
Subscriber
```

| Rol | Görevi |
|-----|--------|
| **Publisher** | Veriyi üretir ve broker’a gönderir |
| **Subscriber** | İlgilendiği konuları dinler ve mesajı alır |
| **Broker** | Publisher ile subscriber’ı birbirine bağlar; yönlendirmeyi yapar |

Aynı fiziksel cihaz her iki rolü de üstlenebilir. Örneğin ESP32 sıcaklık yayınlarken (publisher), uzaktan gelen “LED yak” komutunu da dinleyebilir (subscriber).

### Topic

MQTT’de mesajlar rastgele bir havuza atılmaz; **topic** adı verilen kanallara yazılır. Topic’ler genellikle klasör yolu gibi hiyerarşik isimlendirilir:

```
factory/
factory/temp
factory/humidity
factory/motor1
factory/motor2
```

Çok cihazlı bir sistemde kimlik numarası topic’in içine gömülebilir:

```
cow/12/temp
cow/12/battery
cow/13/temp
cow/13/battery
```

| Topic | Anlam |
|-------|--------|
| `cow/12/temp` | 12 numaralı ünitenin sıcaklığı |
| `cow/13/battery` | 13 numaralı ünitenin batarya bilgisi |

İyi topic tasarımı, ileride filtrelemeyi ve dashboard kurmayı kolaylaştırır. “Her şeyi tek topic’e basmak” kısa vadede işe yarasa da büyüyen sistemlerde karışıklık yaratır.

İleri seviye dinlemede joker (wildcard) kullanılabilir:

- `cow/+/temp` — tüm ünitelerin sıcaklığı  
- `cow/12/#` — 12 numaralı ünitenin altındaki tüm konular  

Temel anlayış için önce düzgün, anlamlı topic isimleri yeterlidir.

Laboratuvar / staj bağlamında herkesin kendi alanında yayın yapması çakışmayı önler:

```
staj/sinan/temp
staj/sinan/hum
staj/sinan/imu
staj/sinan/status
```

---

## 4. Publish – Subscribe mantığı

Somut bir senaryo:

```
ESP32                          Telefon
  │                               │
  │ publish                       │ subscribe
  │ home/room1/temp = 28.4        │ home/room1/temp
  └──────────► Broker ◄───────────┘
                    │
                    └── mesaj telefona iletilir
```

ESP32, `home/room1/temp` topic’ine `28.4` değerini publish eder. Telefon aynı topic’e önceden subscribe olmuştur. Broker mesajı telefona ulaştırır.

Bu modelin gücü şuradadır:

- Telefon veriyi otomatik alır; sürekli ESP32’yi “sorgulamak” zorunda değildir.  
- ESP32’nin telefonu tanımasına gerek yoktur; yalnızca broker’ı ve topic’i bilir.  
- Aynı topic’e yeni bir bilgisayar da subscribe ederse o da aynı akışı alır.

Buna **gevşek bağlı (loosely coupled)** sistem denir. Üretici ile tüketici birbirine sıkı sıkıya kenetlenmez; ikisi de broker üzerinden buluşur. MQTT’nin IoT’de bu kadar sevilmesinin başlıca nedeni budur.

---

## 5. QoS (Quality of Service)

**QoS**, bir mesajın iletiminde ne kadar garanti istendiğini belirtir. Üç seviye vardır:

| QoS | Mantık | Tipik kullanım |
|-----|--------|----------------|
| **0** | Gönder ve unut. Onay beklenmez. | Sık sıcaklık örnekleri; bir paket kaçsa sorun olmayan telemetri |
| **1** | En az bir kez teslim. ACK beklenir; tekrar gönderim olabilir. | Alarm, önemli durum değişimi |
| **2** | Tam bir kez teslim için en sıkı el sıkışma. En güvenli, en yavaş. | Nadiren gerekir; günlük telemetride genelde tercih edilmez |

Daha yüksek QoS daha fazla protokol trafiği ve gecikme demektir. Sürekli akan ortam verisi için QoS 0 veya 1 çoğu senaryoda yeterlidir. “Hiç kaçmasın ve asla tekrar etmesin” ihtiyacı varsa QoS 2 düşünülür; maliyeti bilinerek seçilir.

---

## 6. Retain mesaj

Broker, varsayılan olarak bir topic’e gelen her mesajı o anki abonelere iletir ve geçip gider. Sonradan bağlanan bir client, geçmiş mesajı görmez; yeni bir publish gelmesini bekler.

**Retain** bayrağı ile gönderilen mesaj farklıdır: broker o topic için “son bilinen mesajı” saklar. Yeni bir client subscribe olduğu anda bu saklı mesajı hemen alır.

Örnek:

- Retain olmadan ESP32 `25°C` gönderdiyse, beş dakika sonra bağlanan panel boş ekranla başlar.  
- Retain ile gönderildiyse panel bağlanır bağlanmaz son sıcaklığı görür.

Retain özellikle şu tür bilgiler için uygundur:

- cihaz durumu (`online` / `offline`)  
- son bilinen kritik ölçüm  
- nadiren değişen yapılandırma özeti  

Her saniye akan ham telemetrinin tamamını retain yapmak genelde iyi fikir değildir; broker’da gereksiz “son değer” yükü ve kafa karışıklığı yaratır.

---

## 7. Last Will (LWT)

**Last Will and Testament**, cihazın beklenmedik şekilde koptuğunda broker’ın onun adına yayınlayacağı mesajdır.

Sağlıklı çalışmada ESP32 periyodik olarak hayatta olduğunu belli eder veya status olarak `online` tutar. Bir anda elektrik kesilir, reset olur veya Wi-Fi düşerse cihaz kibarca “ben gidiyorum” diyemez. Bağlantı kurulurken broker’a bırakılan will sayesinde broker şunu yapabilir:

```
ESP32:  Alive … Alive … Alive …
        (ani kopma)
Broker: device/status → offline
```

Bağlantı sırasında tipik olarak şunlar tanımlanır:

- will topic (örnek: `staj/sinan/status`)  
- will mesajı (`offline`)  
- isteğe bağlı olarak retain  

Cihaz ayağa kalkınca kendi status’unu `online` publish eder. Böylece izleyen taraf, cihazın gerçekten yaşayıp yaşamadığını topic üzerinden takip edebilir.

---

## 8. JSON neden kullanılır?

MQTT payload’ı teknik olarak herhangi bir bayt dizisi olabilir. En sade biçim virgülle ayrılmış sayılardır:

```
28.1,55,3.92
```

Aynı bilgi JSON ile şöyle yazılır:

```json
{
  "temp": 28.1,
  "hum": 55,
  "battery": 3.92
}
```

JSON tercihinin nedenleri:

| | Düz metin / CSV | JSON |
|---|-----------------|------|
| Okunabilirlik | Alanların anlamı belirsizdir | Her değerin adı vardır |
| Sıra değişimi | Kolay kırılır | Anahtar ile okunur; sıra esnektir |
| Yeni alan ekleme | Eski alıcılar bozulabilir | Örn. `"imu_z": 0.1` eklenir; eski alanlar durur |
| Yazılım desteği | Elle parse | Neredeyse her dilde hazır kütüphane |

Dashboard, telefon uygulaması veya başka bir gömülü dinleyici için JSON, hem insan hem makine tarafından rahat okunan bir sözleşmedir. IoT telemetrisinde MQTT + JSON çifti bu yüzden çok yaygındır.

---

## 9. HiveMQ

**HiveMQ**, MQTT broker sağlayan bir platformdur. Bulut (Cloud) hesabı veya test ortamı üzerinden cihazlar ortak bir broker’a bağlanabilir.

HiveMQ etrafında sık geçen kavramlar:

| Kavram | Açıklama |
|--------|----------|
| **Broker** | Mesajları alan, saklayan (retain) ve abonelere dağıtan sunucu |
| **Web Client** | Tarayıcıdan broker’a bağılıp publish / subscribe yapmayı sağlayan arayüz |
| **Topic** | Yayınlanan ve dinlenen kanal adı |
| **Credentials** | Cloud ortamında kullanıcı adı ve şifre |

Web Client’ın değeri şudur: henüz ESP32 kodu yazmadan MQTT’nin kendisi görülebilir. Bir sekmede bir topic’e subscribe olunur, başka bir yerden aynı topic’e `hello` / `world` publish edilir; mesajın anında düşmesi, broker’ın ne iş yaptığını somutlaştırır. Donanım tarafına geçildiğinde aynı topic’ler ve aynı broker kullanılacağı için zihinsel model hazırdır.

---

## 10. Sonraki adımın iskeleti

Teori oturduktan sonraki pratik akış doğal olarak şöyle ilerler:

```
Başla
  → Wi-Fi’ye bağlan
  → MQTT broker’a bağlan
  → Gerekirse ilgili topic’lere subscribe ol
  → Döngüde:
        sensörü oku
        JSON oluştur
        publish et
        gelen mesaj varsa callback ile işle
```

Bu sıra, bir IoT cihazının “ölç → paylaş → dinle” yaşam döngüsüdür. Wi-Fi olmadan MQTT olmaz; MQTT olmadan da uzak dashboard’a düzenli telemetri gitmez.

---

## Özet

- IoT, fiziksel ölçümü internet üzerinden paylaşılabilir kılar.  
- Broker, publisher ile subscriber’ı birbirine bağlayan ortaktır.  
- IP hedefi, port servisi; MQTT client’ları broker’a bağlanır.  
- Topic, mesajın adresidir; iyi isimlendirme sistemi düzenler.  
- QoS iletim garantisini, retain son bilinen değeri, last will ani kopuşu yönetir.  
- JSON, payload’ı okunabilir ve genişletilebilir yapar.  
- HiveMQ gibi bir broker ve Web Client, bu modeli somut olarak gösterir.
