# Gün 11 — I2C Temelleri

| | |
|---|---|
| **Tarih** | 2026-08-03 Pazartesi |
| **Hafta** | 3 |
| **Konu** | I2C protokolü: teori, bus tarama, datasheet |
| **Referans** | Kart I2C hattı + sensör datasheet (SHT40 / LIS2DE12 / MPU6050) |

---

## Bugün ne yapacağız?

I2C’nin nasıl çalıştığını öğreneceğiz. Bus’u tarayıp cihaz adreslerini bulacağız, datasheet’ten register okuyacağız. Yarın aynı hatta SHT40 ile sıcaklık / nem ölçümü var.

Anlatım notları: [`01_Anlatim.md`](01_Anlatim.md)  
Görevler: [`02_Gorevler.md`](02_Gorevler.md)

---

## Günlük ritim

| Saat | Aktivite |
|------|----------|
| 09:00–10:30 | I2C teorisi (SDA/SCL, START/STOP, ACK, adres) |
| 10:30–12:30 | Cube/HAL I2C kurulumu + I2C Scanner |
| 13:30–14:30 | WHO_AM_I / datasheet analizi |
| 14:30–16:30 | Görevler + teori soruları rapora |
| 16:30–17:00 | Stand-up + teslim |

---

## Anlatım özeti

- I2C nedir; UART / SPI farkı  
- Master–Slave, SDA–SCL, pull-up  
- 7-bit adres, R/W, ACK/NACK, START/STOP  
- Clock stretching  
- Scanner ve WHO_AM_I mantığı  

Detay: [`01_Anlatim.md`](01_Anlatim.md)

---

## Görevler

1. I2C Scanner  
2. WHO_AM_I oku (kartta sensör varsa)  
3. I2C teorisi soruları  
4. Datasheet analizi  

Detay: [`02_Gorevler.md`](02_Gorevler.md)

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/gunluk_rapor.md
└── proje/
```
