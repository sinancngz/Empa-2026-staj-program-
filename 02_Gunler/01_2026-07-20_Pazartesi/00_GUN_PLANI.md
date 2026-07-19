# Gün 01 — Kart tanıtımı, ortam kurulumu & GPIO

| | |
|---|---|
| **Tarih** | 2026-07-20 Pazartesi |
| **Hafta** | 1 |
| **Konu** | Tiremo Cortex tanıtımı · ABOV ortam kurulumu · GPIO |

---

## Bugün ne yapacağız?

Sabah kartı tanıyıp ABOV araçlarını kuracağız. Kurulumdan sonra mentör **ilk proje oluşturmayı** gösterecek (eMStudio32 / MCUBrew32 ile boş veya örnek proje nasıl açılır, derlenir).

Ardından **GPIO anlatılacak** (çıkış / giriş, LED, buton, pull-up / pull-down — detay: [`01_GPIO_Anlatim.md`](01_GPIO_Anlatim.md)). Anlatım bitince herkes aynı görev listesine geçer: kolay → orta → zor.

Gün sonunda kısa stand-up ve teslim.

---

## Günlük ritim

| Saat | Aktivite |
|------|----------|
| 09:00–10:30 | Kart tanıtımı + ABOV kurulum |
| 10:30–12:00 | Kurulum tamamlama · ilk proje oluşturma (mentör gösterir) |
| 13:30–14:30 | GPIO anlatımı |
| 14:30–16:30 | GPIO görevleri (kolay / orta / zor) |
| 16:30–17:00 | Stand-up + teslim |

---

## Sabah — Kart & kurulum

### Tiremo Cortex

- MCU: ABOV A34G43x (ARM Cortex-M4F)
- LED’ler → GPIO çıkış · kullanıcı butonu → GPIO giriş
- USB Type-C (CN6): besleme + debug + seri
- Sensörler / ESP32 bugün sadece tanışma; asıl konu GPIO

Kart özeti: [`kaynaklar/Tiremo_README.md`](kaynaklar/Tiremo_README.md) · `Tiremo.Cortex.pdf` · `tiremo_cortex.pptx`

### Kurulum

Adımlar: [`kaynaklar/SetUp.md`](kaynaklar/SetUp.md)

| Araç | Amaç |
|------|------|
| eMStudio32 | IDE |
| MCUBrew32 | Pin / çevre birimi ayarı |
| aFlasher32 | HEX yükleme |
| Tera Term | Seri terminal |

### İlk proje oluşturma (mentör gösterir)

Mentör ekranda gösterir; stajyerler kendi makinelerinde takip eder:

1. eMStudio32’yi aç  
2. Yeni / örnek proje oluştur veya aç  
3. Gerekirse MCUBrew32 ile cihaz / pin ayarına bak  
4. **Clean → Build**  
5. Karta yükleme yolunu (IDE veya aFlasher32) kısaca göster  

Amaç: herkesin “proje nasıl açılır / derlenir” bilmesi. LED blink’i birlikte yapmıyoruz — onu görevlerde kendileri yapacak.

---

## Öğleden sonra — GPIO

- GPIO anlatımı: [`01_GPIO_Anlatim.md`](01_GPIO_Anlatim.md)  
  (output / input, LED, buton, pull-up / pull-down)  
- Görevler: [`02_Gorevler.md`](02_Gorevler.md)

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/gunluk_rapor.md
└── proje/
```
