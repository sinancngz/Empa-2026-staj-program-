# Gün 01 — Kart tanıtımı, ortam kurulumu & GPIO

| | |
|---|---|
| **Tarih** | 2026-07-20 Pazartesi |
| **Hafta** | 1 |
| **Konu** | Tiremo Cortex tanıtımı · ABOV ortam kurulumu · GPIO |

---

## Bugünün hedefi

1. Tiremo Cortex kartını tanımak  
2. ABOV geliştirme ortamını kurmak (eMStudio32, MCUBrew32, aFlasher32, Tera Term)  
3. GPIO’yu öğrenmek (output / input, LED, buton, pull-up / pull-down)  
4. Ortak GPIO görevlerini tamamlamak (kolay → orta → zor)

---

## Günlük ritim

| Saat | Aktivite |
|------|----------|
| 09:00–10:00 | Kart tanıtımı + ABOV kurulum |
| 10:00–12:30 | Kurulum tamamlama + örnek flash |
| 13:30–14:30 | GPIO anlatımı |
| 14:30–16:30 | GPIO görevleri (kolay / orta / zor) |
| 16:30–17:00 | Stand-up + teslim kontrolü |

---

## Sabah — Kart & kurulum

### Tiremo Cortex (kısa)

- MCU: ABOV A34G43x (ARM Cortex-M4F)
- LED’ler (output), kullanıcı butonu (input)
- Debug UART, USB Type-C (CN6)
- Sensörler ve ESP32 bu günün konusu değil — sadece tanışma

### Kurulum (herkes)

Kaynaklar: [`kaynaklar/`](kaynaklar/)

1. [`SetUp.md`](kaynaklar/SetUp.md) — eMStudio32, MCUBrew32, aFlasher32, Tera Term  
2. [`RunningCode.md`](kaynaklar/RunningCode.md) — proje açma, build, flash  

**Kontrol:** Ortam açılıyor mu? Kart görülüyor mu? Basit bir örnek flash edilebiliyor mu?

---

## Öğleden sonra — GPIO

Anlatım: [`01_Anlatim_Notlari.md`](01_Anlatim_Notlari.md) → GPIO dökümanı  
Görevler: [`02_Gorevler.md`](02_Gorevler.md) — **herkes aynı görevleri** yapar

---

## Teslim (gün sonu)

Her stajyer:

```
teslimler/Stajyer_X/
├── rapor/gunluk_rapor.md
└── proje/                 ← GPIO çalışması / proje klasörü
```

Lab notu ve kanıt klasörü yok. Rapor + proje yeterli.

---

## Mentör kontrol (yapıldı / yapılmadı)

| Stajyer | Kurulum | GPIO Kolay | GPIO Orta | GPIO Zor | Rapor |
|---------|---------|------------|-----------|----------|-------|
| A — Yaşar Uçar | ☐ | ☐ | ☐ | ☐ | ☐ |
| B — Burak Uçar | ☐ | ☐ | ☐ | ☐ | ☐ |
| C — Başar Yıldırım | ☐ | ☐ | ☐ | ☐ | ☐ |
| D — Aykut İsmet Aslantaş | ☐ | ☐ | ☐ | ☐ | ☐ |
| E — Yavuz Selim Konaç | ☐ | ☐ | ☐ | ☐ | ☐ |
