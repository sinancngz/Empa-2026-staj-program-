# Tiremo® hakkında

**Tiremo®**, güvenli bağlı cihazların geliştirilmesini ve sahaya alınmasını hızlandırmak için tasarlanmış uçtan uca bir AIoT altyapı platformudur. Donanım, yazılım ve bulut araçlarından oluşan ekosistemiyle siber güvenliğe odaklanır; edge çözümlerinin **RED** ve **CRA** gibi düzenleyici çerçevelerle uyumlu olmasına yardımcı olur. Edge AI ile ölçeklenebilir bulut entegrasyonunu birleştirerek prototipten üretim seviyesine geçişi kolaylaştırır.

---

## Kart hakkında

Bu geliştirme kartı **Empa Electronics** tarafından Edge AI ve bulut-IoT uygulamaları için tasarlanmıştır; yazılım desteğiyle birlikte gelir. Yüksek performanslı **ABOV A34G43ARL2N** mikrodenetleyici (ARM® Cortex®-M4F) kullanır ve üzerinde entegre debugger bulunur.

**Donanım özellikleri:**

- **Sensörler:** Analog MEMS mikrofon, 3 eksenli ivmeölçer, sıcaklık / nem sensörleri
- **Kullanıcı arayüzü:** On kullanıcı LED’i ve bir kullanıcı butonu
- **Bağlantı:** Entegre Wi-Fi ve Bluetooth LE modülü (ilerleyen günlerde buluta veri aktarımı için)
- **Besleme ve debug:** USB Type-C portu (CN6) — besleme, firmware yükleme ve seri debug

**Sistem mimarisi (özet):** Kart üzerindeki sensörler fiziksel ölçümleri elektrik sinyaline çevirir. Veri kenarda işlenebilir veya hafif protokollerle (ör. MQTT) buluta iletilebilir. Bu stajda önce kartı ve çevre birimlerini tek tek öğreneceğiz; ilk gün odak **GPIO** (LED ve buton).

---

## Geliştirme ortamı

Başlamadan önce gerekli araçları kur:

### ↳ [Geliştirme Ortamı Kurulumu](SetUp.md)
