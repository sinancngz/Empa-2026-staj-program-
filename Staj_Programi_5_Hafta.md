# Tiremo Cortex — Staj Programı (Master Metin)

> **Operasyonel takvim:** 20 Temmuz – 14 Ağustos 2026 · **20 iş günü**  
> Günlük klasörler, şablonlar ve teslim yapısı → [`04_Gunler/`](04_Gunler/) · [`README.md`](README.md)  
> Aşağıdaki metinde Hafta 5 (17–21 Ağustos) isteğe bağlı uzatma / referans olarak durur.

**Başlangıç:** 20 Temmuz 2026 (Pazartesi)  
**Bitiş (zorunlu program):** 14 Ağustos 2026 (Cuma) — 20 iş günü  
**Uzatma (opsiyonel):** 17–21 Ağustos 2026 — güvenilirlik & capstone  
**Katılımcı:** 5 stajyer (A / B / C / D / E — isimleri mentör atar)  
**Platform:** Tiremo Cortex (ABOV A34G43x, ARM Cortex-M4F)  
**Repo:** `Tiremo_Cortex` → `Examples/` + `Examples/TiremoCortex/` + `Tiremo/`

---

## Çalışma modeli

- Sabah **aynı konu** anlatılır.
- Sonra her stajyer **kendi farklı görev paketini** yapar (kopyalama yok).
- Her paket: **zorunlu maddeler (Must)** + **ileri maddeler (Stretch)**. Stretch olmadan Cuma demosu “eksik” sayılır; Stretch bitince “tam” sayılır.
- Tek satırlık “LED yak” tipi iş yoktur — her gün birden fazla gereksinim bir arada istenir.
- Cuma: herkes kendi demosunu gösterir (8–10 dk) + Must checklist okunur.

### Günlük ritim

| Saat | Aktivite |
|------|----------|
| 09:00–10:00 | Ortak konu anlatımı |
| 10:00–12:30 | Bireysel görev paketi |
| 13:30–16:30 | Devam + mentör turu / debug |
| 16:30–17:00 | Stand-up (ne bitti / Must’ta kalan / blocker) |

### Teslim (her gün + Cuma)

- Lab notu: mimari karar, takıldığı nokta, UART log, Must/Stretch checklist işaretli
- Kod: state machine / modül ayrımı beklenir (mümkün olduğunca `main` şişirilmez)
- Klasör: `stajyer_X/haftaN_gorev/`

### Değerlendirme

| Kriter | Ağırlık |
|--------|---------|
| Must maddelerini tamamlama | %35 |
| Stretch / derinlik | %15 |
| Kod kalitesi (state, katman, isimlendirme) | %20 |
| Debug becerisi | %15 |
| Lab notu + Cuma demo | %15 |

---

## Kart özeti (ilk gün)

| Bileşen | İşlev | Arayüz |
|---------|--------|--------|
| A34G43x | Ana MCU | — |
| SHT40 | Sıcaklık / nem | I2C2 |
| LIS2DE12 | İvmeölçer | I2C |
| MP23ABS1 | Mikrofon | ADC + Timer1 DMA |
| Batarya | Besleme tahmini | ADC |
| ESP32-C3 | WiFi | UART2 |
| SLM320 | 4G (ileri) | UART1 — `Tiremo/` |
| LED’ler | Durum | GPIO |
| Buton PC9 | Kullanıcı girişi | GPIO |
| Debug UART | Log | UART0 @ 115200 |

**Araçlar:** MCUbrew (`*.mproj`), OpenOCD + SWD, seri terminal

---

## Takvim özeti

| Hafta | Tarihler | Konu |
|-------|----------|------|
| 1 | 20–24 Temmuz 2026 | Ortam, GPIO, UART — etkileşimli paneller |
| 2 | 27–31 Temmuz 2026 | Timer, ADC, WDT — ölçüm + koruma sistemleri |
| 3 | 3–7 Ağustos 2026 | I2C + BSP/APP — edge alarm motoru |
| 4 | 10–14 Ağustos 2026 | TiremoCortex + MQTT — bulut telemetri |
| 5 | 17–21 Ağustos 2026 | CRC/AES/RNG + Capstone ürün |

---

# HAFTA 1 — Ortam, GPIO & UART
**20 – 24 Temmuz 2026**

**Ortak öğrenme:** Pin map, toolchain, GPIO, debounce, EINT, UART polling/IRQ, active-low.

**Referans:** `Examples/GPIO/*` · `Examples/UARTn/UARTn_Polling/` · `UARTn_Interrupt/`

---

### Pazartesi 20 Temmuz 2026 — Kurulum + LED motoru

**Anlatım:** Gömülü / A34G43x / MCUbrew / SWD / terminal / active-low LED.

**Herkes (ortak, sabah lab):** Ortam kur, `GPIO_LEDBlinky` flash et.

**Öğleden sonra — bireysel paketler** (hepsi en az 4 Must):

| Stajyer | Görev paketi |
|---------|----------------|
| **A — Pattern Engine** | **Must:** (1) En az 4 LED üzerinde 3 ayrı pattern (ALL, ALTERNATE, CHASE) (2) Pattern’ler arası geçiş yazılım sayaçla (3) Her pattern değişiminde UART log (4) Pattern süresi ayarlanabilir `#define` ile. **Stretch:** Butonla pattern değiştir + “pattern index” UART. |
| **B — Speed Governor** | **Must:** (1) Tek/çoklu LED blink (2) 3 hız kademesi (yavaş/orta/hızlı) (3) Hız değişince UART’da ms değeri (4) Kademe LED göstergesi (1–3 LED). **Stretch:** Hız kademesini non-blocking yaz (busy `delay` yığını yok / minimize). |
| **C — Knight Rider Pro** | **Must:** (1) İleri-geri kara şimşek ≥4 LED (2) Uçta bounce (3) UART’ta yön (`DIR=FWD/REV`) (4) Başlangıçta self-test: tüm LED 200 ms. **Stretch:** “kuyruk” efekti (trailing dim — en az 2 LED aynı anda kontrollü). |
| **D — Bitmask Studio** | **Must:** (1) LED’leri bitmask ile yönet (`0b00010101` gibi) (2) UART’tan hex/bit pattern yazdır (3) 8 hazır pattern sıraya diz, otomatik rotate (4) Kodda `led_write_mask()` API. **Stretch:** Terminalden tek karakter ile mask seç (`0`–`7`). |
| **E — Boot Sequencer** | **Must:** (1) Açılışta 4 adımlı boot animasyonu (2) Her adım UART (`BOOT 1/4`…) (3) Boot bitince “READY” LED sabit (4) Boot sırasında butona basılırsa animasyon skip. **Stretch:** Boot fail simülasyonu: 3. adımda kasıtlı hata → kırmızı pattern + `BOOT_FAIL`. |

---

### Salı 21 Temmuz 2026 — Buton state machine

**Anlatım:** Debounce, kısa/uzun basış, event vs level.

**Herkes Must çekirdeği:** Debounce’lu buton event üretici (`PRESS`, `RELEASE`, `LONG`, isteğe `DOUBLE`).

| Stajyer | Görev paketi |
|---------|----------------|
| **A — Hold & Ramp** | **Must:** Momentary LED + basılı tutma süresini UART ms + 1 sn’de bir “HOLDING…” + bırakınca total hold ms. **Stretch:** Tutma süresine göre 1→N LED yak (ramp). |
| **B — Edge Modes** | **Must:** Toggle modu + “mode LED” + her event’te UART + yanlış bounce’u log’da görünür kıl (raw vs debounced sayaç). **Stretch:** 3 mod: TOGGLE / MOMENTARY / BLINK-WHILE-HOLD. |
| **C — Selector Ring** | **Must:** Her kısa basışta aktif LED index ilerle + seçili LED yanıp sönsün + UART index + uzun basış ile “confirm” (sabit yak). **Stretch:** Confirm sonrası 2 sn idle’da söndür, başa dön. |
| **D — Gesture Parser** | **Must:** SHORT / LONG / DOUBLE ayrımı (zaman pencereli) + her jest farklı LED cevabı + jest sayaçları UART. **Stretch:** “kombo”: SHORT+LONG ardışık → özel pattern. |
| **E — Arm / Disarm UI** | **Must:** Uzun basış ile sistem ARMED/DISARMED + durum LED + kısa basış sadece ARMED iken işlesin + UART state. **Stretch:** DISARM için “2× long” onayı (yanlış basış koruması). |

---

### Çarşamba 22 Temmuz 2026 — UART protokolü (polling)

**Anlatım:** Framing, komut parse, help, hata cevapları.

**Herkes Must çekirdeği:** Satır veya karakter tabanlı komut parser + `ERR` / `OK` cevap standardı.

| Stajyer | Görev paketi |
|---------|----------------|
| **A — Telemetry Tick** | **Must:** 1 Hz sayaç + uptime + buton state tek satır CSV/JSON-ish + `pause`/`resume` komutları. **Stretch:** Örnekleme periyodu komutla değişsin (`rate 500`). |
| **B — Event Logger** | **Must:** Buton event ring buffer (en az 16) + `dump` komutu ile UART’a bas + buffer overflow sayacı. **Stretch:** `clear` + timestamp (yazılım ms). |
| **C — LED Script** | **Must:** Komutlar: `on N`, `off N`, `mask 0x..`, `status` + geçersiz komutta usage. **Stretch:** `seq 1,2,3,1` ile kısa script çalıştır. |
| **D — Remote Console** | **Must:** `1`/`0` LED, `b` buton oku, `i` info (build tag/isim) + komut echo. **Stretch:** Şifreli giriş: önce `auth 1234` olmadan yazma komutları reddedilsin. |
| **E — Menu Shell** | **Must:** `h/l/s/m` menü + alt menü (LED menü / SYS menü) + breadcrumb prompt (`MAIN>` / `LED>`). **Stretch:** `history` son 5 komut. |

---

### Perşembe 23 Temmuz 2026 — IRQ + EINT + karşılaştırma

**Anlatım:** ISR’da az iş, flag, race; polling vs IRQ.

| Stajyer | Görev paketi |
|---------|----------------|
| **A — IRQ Echo Router** | **Must:** UART IRQ RX echo + özel karakterler (`L` LED toggle, `S` status) main’de işlensin + ISR’da ağır iş yok. **Stretch:** RX overrun/hata sayacı. |
| **B — EINT Button Core** | **Must:** Buton EINT + debounce (main veya timer tick) + event queue + LED/UART consumer. **Stretch:** Rising/falling ayrı sayaç. |
| **C — Hybrid Control** | **Must:** TX polling + RX IRQ + komutla LED + buton EINT aynı projede çakışmadan. **Stretch:** Komut `irqstat` ile flag/queue derinliği. |
| **D — Benchmark Note** | **Must:** Aynı kullanıcı senaryosunu (buton→LED+log) polling ve IRQ ile iki build/flag’de üret + lab notunda latency/CPU idle gözlemi (≥8 madde, ölçüm varsa sayı). **Stretch:** Basit “missed event” sayacı. |
| **E — Safe ISR Pattern** | **Must:** EINT → flag → main state machine + UART spam yok (event’te 1 log) + yeniden giriş / bounce test prosedürü lab notunda. **Stretch:** Critical section notu (shared değişken `volatile` + neden). |

---

### Cuma 24 Temmuz 2026 — Hafta 1 entegrasyon demosu

Her stajyer **küçük bir ürün** çıkarır (Must ≥ 6 madde):

| Stajyer | Mini ürün |
|---------|-----------|
| **A — Interactive Status Panel** | Pattern engine + buton jestleri + UART status + idle timeout (10 sn) + self-test + lab checklist. |
| **B — Dual-Speed Knight Rider Console** | Kara şimşek + 3 hız + UART hız komutu + buton hız + yön log + bounce-end efekti. |
| **C — Binary Control Deck** | 0–7 binary LED + buton inc/dec + UART set (`set 5`) + long press reset + limitte `WRAP/CLAMP` seçimi. |
| **D — Chase Guard** | Chase + arm/disarm + idle sleep LED off + event logger `dump` + çift tık panic (tüm LED flash). |
| **E — UART Command Center** | Alt menülü shell + LED mask API + auth kilidi + `status` zengin satır + hata kodları tablosu lab notunda. |

**Demo:** 8–10 dk · Must checklist mentöre okunur · Stretch varsa ayrı gösterilir.

---

# HAFTA 2 — Timer, ADC, Watchdog
**27 – 31 Temmuz 2026**

**Referans:** `Examples/TIMER1n/` · `FRT/` · `ADC/ADC_Battery/` · `ADC_Microphone/` · `WDT/`

---

### Pazartesi 27 Temmuz 2026 — Timer tabanlı zamanlama omurgası

| Stajyer | Görev paketi |
|---------|----------------|
| **A — Scheduler Lite** | **Must:** Period match ile 1 ms veya sabit tick → yazılımda 10/100/1000 ms task’ler + LED task + UART heartbeat. **Stretch:** Task overrun sayacı. |
| **B — IRQ Blink FSM** | **Must:** Timer IRQ LED FSM (OFF/ON/FAST) + butonla state + UART state adı. **Stretch:** One-shot “pulse 150 ms” state’i. |
| **C — Dual Timebase** | **Must:** İki bağımsız periyot (ör. 200 ms UI, 1000 ms log) tek timer tick’ten türetilsin + her ikisi de görünür (LED + UART). **Stretch:** Periyotları runtime komutla değiştir. |
| **D — Input-timed OneShot** | **Must:** Buton→one-shot LED N ms + iptal (ikinci basış) + kalan süre UART. **Stretch:** Queue: basılı tutarken tekrar tetikleme politikası (ignore/replace). |
| **E — Adaptive Period** | **Must:** 3 kademe period + kademe LED bar + geçişte timer yeniden kurulum + log. **Stretch:** “auto”: belirli sürede basılmazsa yavaş kademeye dön. |

---

### Salı 28 Temmuz 2026 — FRT ölçüm laboratuvarı

| Stajyer | Görev paketi |
|---------|----------------|
| **A — Interval Analyzer** | **Must:** Basış aralıkları istatistik: last / min / max / avg (en az 10 örnek) UART tablo. **Stretch:** Histogram 4 kova. |
| **B — Press Profiler** | **Must:** SHORT/LONG sınırını ölçerek kalibre et + eşikleri `#define` yerine runtime set komutu. **Stretch:** Kalibrasyon sonucu lab’a tablo. |
| **C — Countdown Engine** | **Must:** Ayarlanabilir countdown (UART `cd 15`) + LED progress + iptal + `DONE/ABORT`. **Stretch:** Pause/resume. |
| **D — Reaction Lab** | **Must:** Random bekleme (yazılım) + LED stimulus + reaction ms + early-press fail + 5 deneme özeti. **Stretch:** High-score tut. |
| **E — Uptime + Drift Note** | **Must:** mm:ss uptime + her 60 sn marker + FRT ile “beklenen vs ölçülen” kaba drift notu. **Stretch:** Soft RTC benzeri gün sayacı (lab). |

---

### Çarşamba 29 Temmuz 2026 — Batarya izleme sistemi

| Stajyer | Görev paketi |
|---------|----------------|
| **A — Battery Telemetry** | **Must:** 1 Hz mV + OK flag + CSV log + `sample` komutu. **Stretch:** 1 dakikalık min/max. |
| **B — Hysteresis Guard** | **Must:** LOW/OK eşikleri histerezisli + LED + `LOW_BAT` event (spam yok). **Stretch:** 3 seviye (CRIT/LOW/OK). |
| **C — Filter Pack** | **Must:** Ham + moving average (N=5/10 seçilebilir) + UART ikisini birden. **Stretch:** Basit spike reject (|Δ| büyükse at). |
| **D — Battery Gauge UI** | **Must:** 4 kademe LED bar + eşik kalibrasyon tablosu (≥12 ölçüm) lab notu. **Stretch:** Gauge + sayısal mV birlikte. |
| **E — On-demand + Trend** | **Must:** Butonla ölç + son 8 örneği RAM’de tut + `trend` komutu (up/down/flat kaba). **Stretch:** Trend’e göre LED. |

---

### Perşembe 30 Temmuz 2026 — Mikrofon analiz hattı

| Stajyer | Görev paketi |
|---------|----------------|
| **A — RMS Pipeline** | **Must:** Capture + service loop doğru + RMS 2 Hz log + fail durumunda `MIC_ERR`. **Stretch:** RMS + peak aynı satır. |
| **B — 3-Zone Classifier** | **Must:** SILENT/NORMAL/LOUD + LED + zone değişiminde tek event log (histerezis). **Stretch:** Zone süreleri sayacı. |
| **C — Loud Alarm FSM** | **Must:** LOUD enter/exit + alarm LED pattern + UART + alarm latch (buton ack ile temizle). **Stretch:** Alarm süresi timeout auto-clear. |
| **D — Calibration Kit** | **Must:** Sessiz oda / konuşma / alkış için ≥10’ar örnek tablo + önerilen eşikler + kodda uygula. **Stretch:** `cal` komutu ile eşik yaz. |
| **E — Peak Hold Monitor** | **Must:** 3 sn window peak hold + buton reset + LED “new peak” flash + log. **Stretch:** Çift window (1 sn ve 3 sn). |

---

### Cuma 31 Temmuz 2026 — WDT + haftalık sistem demosu

**Anlatım:** WDT kick, hang, güvenli demo protokolü.

| Stajyer | Mini ürün (Must ≥ 7) |
|---------|----------------------|
| **A — Timed Sensor Desk** | Tick scheduler + batarya telemetry + mic RMS + UART dashboard + LOW_BAT LED + WDT kick + bilinçli hang demosu (mentör eşliğinde) ayrı build/flag. |
| **B — Audio Level Guard** | Mic 3-zone + LED bar + latch alarm + batarya low iken “mute alarm LED önceliği” kuralı + WDT. |
| **C — Dual-Sensor Console** | `BAT`/`MIC` satır formatı + komutlar `rate`/`dump`/`ack` + LOUD/LOW event’leri + FRT uptime. |
| **D — Watchdog Story** | İki firmware: (1) hang→reset kanıt log (2) kick’li güvenli; lab notunda kök neden + ne zaman WDT şart (≥10 madde). |
| **E — Run/Stop Recorder** | Buton run/stop + çalışırken 1 Hz bat+mic kaydı (RAM ring ≥32) + `dump` + stop’ta özet istatistik. |

---

# HAFTA 3 — I2C sensörler & BSP/APP
**3 – 7 Ağustos 2026**

**Referans:** `Examples/I2Cn/I2Cn_SHT40/` · `I2Cn_LIS2DE12TR/` · `Examples/TiremoCortex/`

---

### Pazartesi 3 Ağustos 2026 — SHT40 ürünleştirme

| Stajyer | Görev paketi |
|---------|----------------|
| **A — Climate Stream** | **Must:** Temp+RH 1 Hz + OK flag + CSV + hata retry (1–2) + `ERR:SHT`. **Stretch:** Ölçüm periyodu komutu. |
| **B — Comfort Zones** | **Must:** RH ve temp için zone LED + histerezis + zone event log. **Stretch:** “comfort score” 0–100 kaba. |
| **C — Unit & Format Layer** | **Must:** °C/°F + RH + tek `print` API + buton/unit komutu. **Stretch:** JSON satır opsiyonu. |
| **D — Hot Alarm Engine** | **Must:** Eşik + histerezis + latch + ack + LED pattern + UART. **Stretch:** Warning vs Critical iki eşik. |
| **E — Health Check** | **Must:** Init fail / read fail ayrımı + boot’ta self-check + periyodik “sensor alive” LED heartbeat. **Stretch:** Fail counter threshold → safe mode (ölçümü durdur). |

---

### Salı 4 Ağustos 2026 — LIS2DE12 hareket zekâsı

| Stajyer | Görev paketi |
|---------|----------------|
| **A — Accel Stream + |a|** | **Must:** XYZ mg + \|a\| + OK + 1 Hz/2 Hz log. **Stretch:** Ham vs mg dönüşüm notu lab. |
| **B — Orientation FSM** | **Must:** ±X/±Y/±Z dominant orientation + debounce zamanı + LED map + event. **Stretch:** UNKNOWN state. |
| **C — Shake Detector** | **Must:** Δg / yüksek geçiş benzeri eşik + cooldown + latch/ack. **Stretch:** Shake yoğunluğu sayacı. |
| **D — Fall Candidate** | **Must:** Free-fall benzeri düşük \|a\| penceresi + doğrulama süresi + `FALL` + false-positive notu. **Stretch:** Fall sonrası “impact” yüksek g. |
| **E — Motion Activity** | **Must:** STILL / MOVE sınıflandırıcı + LED + aktivite yüzdesi (son 10 sn). **Stretch:** UART `activity` komutu. |

---

### Çarşamba 5 Ağustos 2026 — Multi-sensor orchestration

| Stajyer | Görev paketi |
|---------|----------------|
| **A — Dual Bus Client** | **Must:** SHT40+LIS aynı loop, her sensör bağımsız OK, kısmi fail’de diğer devam. **Stretch:** Round-robin öncelik. |
| **B — Power-aware Sense** | **Must:** Batarya düşükse ivme örnekleme yavaşlasın (policy) + log’da policy state. **Stretch:** Kritik bataryada sadece temp. |
| **C — Noise + Motion** | **Must:** Mic zone + shake aynı anda; çakışmada öncelik kuralı dokümante. **Stretch:** Birleşik `ALERT` kodu. |
| **D — Dashboard v2** | **Must:** Tek satır: temp, RH, \|a\|, bat, micRMS + `compact/verbose` mod. **Stretch:** 1 Hz compact / event’te verbose. |
| **E — Fault Injection Drill** | **Must:** Kablo/simülasyon ile fail senaryoları (≥3) + beklenen log + recovery. **Stretch:** Otomatik retry backoff. |

---

### Perşembe 6 Ağustos 2026 — Gerçek BSP/APP ayrımı

**Anlatım:** HAL→BSP→APP→Process; `prv_user_code` ince.

| Stajyer | Görev paketi |
|---------|----------------|
| **A — APP API Hot/Cold** | **Must:** `app_climate.h` API (`IsHot/IsCold/Get`) + main sadece API kullansın + eşikler APP’te. **Stretch:** Unit test’e benzer host’suz self-check fonksiyonu. |
| **B — APP Motion Module** | **Must:** `IsShaken/IsFallCandidate/GetOrientation` + LED binding APP dışında/process’te. **Stretch:** Callback ile alarm notify. |
| **C — Architecture Pack** | **Must:** Kendi koduna göre diyagram + her katmana örnek fonksiyon listesi + “yanlışlıkla HAL’i APP’ten çağırdım” anti-örnek. **Stretch:** TiremoCortex ile kendi yapını karşılaştırma tablosu. |
| **D — Configurable Thresholds** | **Must:** Eşikler struct + setter/getter + UART `th get/set` + BSP’ye dokunmadan. **Stretch:** Geçersiz aralık reject. |
| **E — Facade + Report** | **Must:** `Sensor_ReadAll` / `Print` / `ClearAlarms` + alarm bitmask + main ≤ ~40 satır mantık. **Stretch:** Report format plugin (CSV/JSON). |

---

### Cuma 7 Ağustos 2026 — Edge Monitor ürünleri

| Stajyer | Mini ürün |
|---------|-----------|
| **A — Climate Sentinel** | Start/stop gate + hot/cold alarm + histerezis + ack + dashboard + APP API + fail-safe. |
| **B — Motion Sentinel** | Shake + orientation UI + cooldown + event log ring + APP motion modülü. |
| **C — Comfort Station** | Temp/RH comfort score + 3 LED + birim değiştir + verbose/compact. |
| **D — Tilt & Fall Desk** | Orientation LED + fall candidate + false-positive lab + eşik UART config. |
| **E — Edge Hub Lite** | Climate + motion alarm birleşik bitmask + öncelik + `Sensor_*` facade + 1 sayfa mimari. |

---

# HAFTA 4 — TiremoCortex & ESP32 MQTT
**10 – 14 Ağustos 2026**

> Credential mentörden; secret commit yok.

**Referans:** `Examples/TiremoCortex/` · `UARTn_ESP32_AT_Test/` · `tiremo_app_net.c`

---

### Pazartesi 10 Ağustos 2026 — Kod tabanı haritalama (derin)

| Stajyer | Görev paketi |
|---------|----------------|
| **A — Bring-up + Trace** | **Must:** Build/flash + button dump + call graph (prv→app→sensor) + 10 kritik dosya listesi. **Stretch:** Bir alarmın tetik zincirini satır satır. |
| **B — Sensor Contract Sheet** | **Must:** UART alanları tablo (birim, kaynak dosya, OK flag) + eksik/garip alan notu. **Stretch:** `SensorData_t` alan eşlemesi. |
| **C — Alarm Archaeology** | **Must:** Tüm eşiklerin path+satır + varsayılan değerler + nasıl değişir. **Stretch:** Bir eşiği güvenli değiştirip davranış kanıtı. |
| **D — LED Semantics Map** | **Must:** Her status LED anlamı + hangi state’te yanar tablosu. **Stretch:** Eksik LED senaryosu öner (1 paragraf). |
| **E — Config Flag Matrix** | **Must:** `EMPA_*` flag’leri × davranış matrisi + yanlış kombinasyon riskleri. **Stretch:** İki flag birlikte açıkken gözlem. |

---

### Salı 11 Ağustos 2026 — ESP32 AT dayanıklılık

| Stajyer | Görev paketi |
|---------|----------------|
| **A — AT Session Log** | **Must:** AT/OK, versiyon, WiFi mode komutları log dosyası + timeline. **Stretch:** Beklenmeyen cevap parser notu. |
| **B — Join & IP Proof** | **Must:** Join success + IP + RSSI (varsa) + screenshot/log. **Stretch:** Join süresi ölçümü. |
| **C — Negative Testing** | **Must:** Yanlış SSID/şifre, timeout, sinyal yok (≥3 fail) + hata kodları tablosu. **Stretch:** Fail sonrası recovery adımları. |
| **D — Power/Reset Policy** | **Must:** PWR pin power-cycle prosedürü + ne zaman reset gerekir lab. **Stretch:** Soft vs hard reset farkı deneyi. |
| **E — AT Cheat-sheet + SM** | **Must:** Kullandığı AT’ler + sade state machine diyagramı (POWER→AT→WIFI). **Stretch:** Her state’te timeout. |

---

### Çarşamba 12 Ağustos 2026 — MQTT oturumu

| Stajyer | Görev paketi |
|---------|----------------|
| **A — Hello Cloud** | **Must:** Connect + hello publish + broker kanıtı + reconnect 1 deneme. **Stretch:** Will/offline mesajı (broker destekliyorsa). |
| **B — Temp Publisher** | **Must:** Periyodik temp + topic şeması doküman + QoS notu. **Stretch:** Değişince publish (delta). |
| **C — Climate Publisher** | **Must:** Temp+RH JSON + timestamp/uptime + hata alanı. **Stretch:** Pretty vs compact. |
| **D — Battery Publisher** | **Must:** mV + LOW flag cloud’a + yerel LED ile tutarlılık. **Stretch:** Crit seviyesi ayrı topic. |
| **E — Connection Observer** | **Must:** State log (INIT/WIFI/MQTT/PUB/ERR) + LED map + hata sayacı. **Stretch:** State geçiş tablosu. |

---

### Perşembe 13 Ağustos 2026 — Telemetri + alarm kanalları

| Stajyer | Görev paketi |
|---------|----------------|
| **A — Full Telemetry** | **Must:** temp, RH, bat, accel özet, micRMS + period config + broker proof. **Stretch:** Field enable bitmask. |
| **B — Temp Alarm Channel** | **Must:** Ayrı alarm topic + latch/ack + telemetry’den ayrışma. **Stretch:** Alarm rate-limit. |
| **C — Mic Alarm Channel** | **Must:** LOUD → MQTT + yerel pattern + ack. **Stretch:** Alarm payload’da RMS. |
| **D — Motion Alarm Channel** | **Must:** Shake/fall → MQTT + false trigger notu. **Stretch:** Orientation change event (opsiyonel). |
| **E — Publish Visibility** | **Must:** Her publish’te TX log/LED + fail’de ERR + ardışık fail→state ERROR. **Stretch:** Başarı oranı (ok/fail). |

---

### Cuma 14 Ağustos 2026 — Cloud ürün demoları

| Stajyer | Mini ürün |
|---------|-----------|
| **A — Telemetry Beacon Pro** | Full JSON 5 sn + button gate + connection observer + broker screenshots (≥3 senaryo). |
| **B — Climate Cloud Guard** | Temp(+RH) telemetry + temp alarm channel + histerezis + ack. |
| **C — Acoustic Cloud Guard** | Mic zones + LOUD MQTT + yerel latch + kalibrasyon özeti. |
| **D — Motion Cloud Guard** | Shake/fall cloud + button-gated sensing + LED semantics. |
| **E — Link Reliability Report** | Bilinçli koparma testleri + yeniden bağlanma + 1 sayfa SM + metrikler (süre, deneme). |

---

# HAFTA 5 — Güvenilirlik & Capstone
**17 – 21 Ağustos 2026**

**Referans:** `Examples/CRC/` · `AES/` · `RNG/` · `FMC/` · `Tiremo/` / `MEIG_SLM3XX/`

---

### Pazartesi 17 Ağustos 2026 — CRC + RNG paket protokolü

| Stajyer | Görev paketi |
|---------|----------------|
| **A — Framed Telemetry** | **Must:** `HDR | LEN | PAYLOAD | CRC` UART çerçevesi + parser. **Stretch:** Version byte. |
| **B — Tamper Drill** | **Must:** Bilerek boz + `CRC_ERR` + iyi paketlerden ayır + sayaçlar. **Stretch:** Hata enjekte komutu. |
| **C — Session Identity** | **Must:** RNG session id boot’ta + tüm loglara id prefix. **Stretch:** Id’yi MQTT client id/topic’te kullan. |
| **D — Nonce per Sample** | **Must:** Her ölçüme nonce + tekrar eden nonce yakalama testi. **Stretch:** Nonce’u CRC kapsamına al. |
| **E — Secure-ish Datagram** | **Must:** Nonce+CRC birleşik demo + lab’da “ne korur / ne korumaz” tablosu. **Stretch:** Replay üzerine 1 paragraf. |

---

### Salı 18 Ağustos 2026 — AES + FMC hazırlığı

| Stajyer | Görev paketi |
|---------|----------------|
| **A — AES Encrypt Path** | **Must:** Örnek key/plaintext → ciphertext log + kod yolu işaretli. **Stretch:** Aynı plaintext iki kez (IV yoksa risk notu). |
| **B — Round-trip Harness** | **Must:** Enc→dec eşitlik assert/log + fail senaryosu. **Stretch:** Yanlış key ile fail. |
| **C — Secret Threshold Lab** | **Must:** Eşik benzeri değeri şifreli saklama deneyi + çözüp kullan. **Stretch:** Key’i kodda hardcode etmenin riski lab. |
| **D — Flash Wear Brief** | **Must:** FMC örneğini çalıştır/oku + wear/page/align notu (≥8 madde) + “config ne sıklıkla yazılır?” politikası. **Stretch:** Dummy config struct layout. |
| **E — Capstone Storage Design** | **Must:** Kendi capstone’u için storage karar dokümanı (RAM only / FMC / yok) + risk. **Stretch:** FMC kullanacaksa page map taslağı. |

---

### Çarşamba 19 Ağustos 2026 — Capstone kickoff (ağır ürünler)

Her stajyer kendi ürününü alır. **Must ortak:** çalışan dikey dilim + ≥12 maddelik test checklist + mimari taslak + demo script.

| Stajyer | Capstone (zorunlu kapsam) |
|---------|---------------------------|
| **A — Smart Desk Guard** | Sensör okuma + ≥2 yerel alarm (histerezis/ack) + MQTT telemetry + alarm channel + button run/stop + connection LED/state + lab kanıtları. |
| **B — Threshold Tuner Device** | UART menü ile ≥3 eşik get/set + validate + (hedef) FMC persist + reboot sonrası doğrula; FMC yoksa “persist stub + neden” ama RAM profil + export/import komutu zorunlu. |
| **C — Offline Buffer Gateway** | Ring buffer N≥32 telemetry; online/offline SM; flush politikası (burst limit); overflow sayacı; MQTT gelince drain; test: bilinçli WiFi kes. |
| **D — Power-aware Device UI** | 3–4 batarya kademesi LED politikası + low/crit alarm (yerel+MQTT) + düşük güçte sense rate düşürme + politika tablosu doküman. |
| **E — Link & Alarm Console** | Bağlantı SM LED’leri + telemetry + seçilen 1 alarm cloud + negatif-limit + 1 sayfa SM + koparma/rejoin deney raporu. |

*(Mentör onayı + donanım varsa: ek stretch olarak SLM320 tek publish — ana Must’un yerine geçmez.)*

---

### Perşembe 20 Ağustos 2026 — Sertleştirme günü

| Stajyer | Bugünkü Must |
|---------|----------------|
| **A** | Alarm spam yok; reconnect sonrası publish; demo 3 senaryo prova (normal/alarm/offline). |
| **B** | Geçersiz eşik reject; reboot persistence kanıtı (veya export/import); menü help tam. |
| **C** | Overflow davranışı demo; flush sırası doğru; N doldur-boşalt otomatik test. |
| **D** | Policy geçişleri histerezisli; crit’te agresif uyarı; sense-rate değişimi log’da. |
| **E** | Metrikler (fail count, rejoin time); diyagram final; demo script cronometreli. |

**Herkes Stretch (ortak havuz — en az 1 seç):** CRC’li UART debug frame · alarm rate-limit · JSON schema notu · WDT kick · field enable bitmask.

---

### Cuma 21 Ağustos 2026 — Final

| Saat | Aktivite |
|------|----------|
| 09:00–09:30 | Prova |
| 09:30–10:30 | A & B |
| 10:45–11:45 | C & D |
| 11:45–12:30 | E |
| 13:30–14:30 | Geri bildirim / kapanış |
| 14:30–16:00 | Portföy + 1:1 |

**Final teslim:** Demo · mimari 1 sayfa · test checklist ≥12 · yansıma · Must/Stretch işaretli lab özeti

---

## Mentör hazırlık

### Donanım / yazılım
- [ ] Kart + SWD + terminal (kişi başı)
- [ ] 10 Ağustos öncesi WiFi + MQTT broker
- [ ] MCUbrew / OpenOCD / repo
- [ ] Credential şablonu (secret’sız)

### Stajyer eşlemesi

| Kod | İsim |
|-----|------|
| A | |
| B | |
| C | |
| D | |
| E | |

---

## Portföy

```
stajyer_X/
├── 2026-07_hafta1_gpio_uart/
├── 2026-07_hafta2_timer_adc/
├── 2026-08_hafta3_i2c/
├── 2026-08_hafta4_mqtt/
├── 2026-08_hafta5_capstone/
│   ├── mimari.md
│   ├── test_checklist.md
│   └── yansima.md
└── ozet.md
```

---

## Cuma rubriği

| Madde | 0 | 1 | 2 | 3 |
|-------|---|---|---|---|
| Must kapsamı | <50% | Çoğu | Hepsi | Hepsi + temiz |
| Stretch | Yok | Denendi | Bitti | Bitti + iyi |
| Tasarım (FSM/katman) | Yok | Kısmi | Net | Net + anlatabiliyor |
| Kanıt (log/screenshot) | Yok | Zayıf | Yeterli | Güçlü |
| Demo anlatımı | Kopuk | Temel | İyi | Mentor gibi |

---

## Mentör notları

1. Görevler kasıtlı dolu: gün içinde Must’un %70’i hedef; Stretch ayrıştırıcı.
2. Takılınca ipucu ver, çözüm kodunu verme.
3. Hafta 1’de bile parser/FSM beklenir — “sadece delay ile blink” kabul değil (A hariç ilk sabah ortak lab).
4. Capstone kapsam şişmesin diye Perşembe’de feature freeze.

---

*20 Temmuz – 21 Ağustos 2026. Tatilde kaydırma mentörde.*
