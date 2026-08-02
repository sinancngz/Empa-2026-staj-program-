# Gün 12 — SHT40 Sıcaklık & Nem

| | |
|---|---|
| **Tarih** | 2026-08-04 Salı |
| **Hafta** | 3 |
| **Konu** | SHT40 ile I2C sıcaklık / nem okuma |
| **Referans** | Sensirion `embedded-i2c-sht4x` + kendi I2C HAL |

---

## Bugün ne yapacağız?

Dünkü I2C bilgisini kullanarak SHT40’tan **sıcaklık ve nem** okuyacağız. Sensirion’un resmi kütüphanesini projeye ekleyip **HAL katmanını** kartımıza uyarlayacağız.

Anlatım notları: [`01_Anlatim.md`](01_Anlatim.md)  
Görevler: [`02_Gorevler.md`](02_Gorevler.md)

---

## Günlük ritim

| Saat | Aktivite |
|------|----------|
| 09:00–10:30 | SHT40 + Sensirion kütüphane / HAL anlatımı |
| 10:30–12:30 | Kütüphane entegrasyonu + HAL yazımı |
| 13:30–14:30 | Ölçüm debug (CRC, adres, sleep) |
| 14:30–16:30 | Tek görev: T + RH UART log |
| 16:30–17:00 | Stand-up + teslim |

---

## Anlatım özeti

- SHT40 komut modeli ve `0x44`  
- 6 byte cevap + CRC + birim dönüşümü  
- Sensirion driver mimarisi; HAL’i kim yazar?  
- Sağlıklı hata log’u  

Detay: [`01_Anlatim.md`](01_Anlatim.md)

---

## Görevler

Bugün **tek görev:** SHT40’tan sıcaklık ve nem ölçmek.  
Detay: [`02_Gorevler.md`](02_Gorevler.md)

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/gunluk_rapor.md
└── proje/
```
