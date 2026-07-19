# Empa 2026 — Tiremo Cortex Staj Programı

**20 Temmuz 2026 → 14 Ağustos 2026 · 20 iş günü · 5 stajyer**

---

## Stajyerler

| Kod | İsim |
|-----|------|
| A | Yaşar Uçar |
| B | Burak Uçar |
| C | Başar Yıldırım |
| D | Aykut İsmet Aslantaş |
| E | Yavuz Selim Konaç |

---

## Hızlı başlangıç

| Rol | Nereden |
|-----|---------|
| **Mentör** | [`00_Genel/Mentor_Kontrol_Listesi.md`](00_Genel/Mentor_Kontrol_Listesi.md) |
| **Bugün** | [`04_Gunler/01_2026-07-20_Pazartesi/00_GUN_PLANI.md`](04_Gunler/01_2026-07-20_Pazartesi/00_GUN_PLANI.md) |
| **Gün şablonu** | [`01_Sablonlar/Gun_Klasoru_Sablonu.md`](01_Sablonlar/Gun_Klasoru_Sablonu.md) |

---

## Klasör yapısı

```
├── 00_Genel/           Özet, takvim, değerlendirme (tik), donanım
├── 01_Sablonlar/       Gün şablonu, rapor, demo checklist
├── 02_Stajyerler/      A–E kişi klasörleri
├── 03_Haftalar/        Haftalık özet
├── 04_Gunler/          20 iş günü
└── Staj_Programi_5_Hafta.md
```

Her gün:

```
04_Gunler/XX_.../
├── 00_GUN_PLANI.md
├── 01_Anlatim_Notlari.md
├── 02_Gorevler.md          ← kolay / orta / zor (herkes aynı)
├── mentor_notlari.md       ← sade tik
├── kaynaklar/              ← o günün dökümanları
└── teslimler/Stajyer_X/
    ├── rapor/
    └── proje/
```

---

## Çalışma modeli

1. Sabah ortak konu + anlatım dökümanı  
2. Ortak görevler: **kolay → orta → zor**  
3. Mentör sadece **yapıldı / yapılmadı** işaretler (puan yok)  
4. Teslim: **rapor + proje**  

---

## 4 hafta

| Hafta | Tarihler | Konu |
|-------|----------|------|
| 1 | 20–24 Temmuz | Ortam, GPIO, UART |
| 2 | 27–31 Temmuz | Timer, ADC, WDT |
| 3 | 3–7 Ağustos | I2C + BSP/APP |
| 4 | 10–14 Ağustos | TiremoCortex + MQTT |
