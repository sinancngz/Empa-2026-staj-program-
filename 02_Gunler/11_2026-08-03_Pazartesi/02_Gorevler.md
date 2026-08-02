# Gün 11 — Görevler (I2C Temelleri)

Anlatım: [`01_Anlatim.md`](01_Anlatim.md)

**Amaç:** Bus’u anlamak, cihazı bulmak, datasheet’ten register okumak.  
Yarın SHT40 ölçümü için bugün temeli atıyorsun.

---

## Ortak hazırlık

- [ ] I2C pinleri / bus açık (mentörle doğrula)  
- [ ] UART debug çalışıyor  
- [ ] En az bir I2C cihaz bağlı (SHT40, LIS2DE12, MPU6050 vb.)  
- [ ] Anlatım okundu / sunum dinlendi  

---

## Görev 1 — I2C Scanner

En temel görev. Bus’ta kim var, öğren.

### İstenenler

1. `HAL_I2C_IsDeviceReady()` (veya platformdaki eşdeğeri) ile tüm adresleri tara.  
2. Bulduğu adresleri UART’a yazdır.  
3. **`0x08`–`0x77`** aralığını tara.  
4. Cihaz bulununca net mesaj ver (“Device Found” / “Found device at …”).

### Örnek çıktı

```
Scanning I2C Bus...

Found device at 0x44
Found device at 0x68

Scan Finished.
```

### Bu görevle öğreneceklerin

| Kavram | Ne görürsün? |
|--------|----------------|
| Slave Address | Hangi 7-bit adres ACK verdi |
| ACK | Cihaz var demek |
| `HAL_I2C_IsDeviceReady()` | Adrese ping |

### İskelet (pseudo)

```c
printf("Scanning I2C Bus...\r\n\r\n");

for (uint8_t addr = 0x08; addr <= 0x77; addr++) {
    if (HAL_I2C_IsDeviceReady(&hi2c1, addr << 1, 3, 10) == HAL_OK) {
        /* Not: bazı HAL'ler 8-bit (addr<<1), bazıları 7-bit ister — mentörle doğrula */
        printf("Found device at 0x%02X\r\n", addr);
    }
}

printf("\r\nScan Finished.\r\n");
```

| # | Madde | Yapıldı |
|---|-------|---------|
| 1 | Tarama döngüsü `0x08`–`0x77` | ☐ |
| 2 | Bulunan adresler UART’ta | ☐ |
| 3 | Başlangıç / bitiş mesajı | ☐ |
| 4 | Mentöre göster (bağlı cihaz adresi tutuyor mu?) | ☐ |

---

## Görev 2 — WHO_AM_I Oku

Kartta **LIS2DE12**, **MPU6050**, **ISM330** gibi WHO_AM_I register’ı olan bir sensör varsa.

### İstenenler

1. Datasheet’ten **WHO_AM_I** (veya Device ID) register adresini bul.  
2. Register’ı I2C ile oku.  
3. Değeri UART’a yazdır.  
4. Datasheet’teki beklenen değerle karşılaştır.

### Örnek

```
WHO_AM_I = 0x33
```

| Sensör (örnek) | Tipik slave addr | WHO_AM_I reg | Beklenen (örnek) |
|----------------|------------------|--------------|------------------|
| LIS2DE12 | `0x18` / `0x19` | `0x0F` | `0x33` |
| MPU6050 | `0x68` / `0x69` | `0x75` | `0x68` |

> Değerler datasheet’e göre değişir; tablodaki sayıları ezberleme, **kendi datasheet’inden** doğrula.

| # | Madde | Yapıldı |
|---|-------|---------|
| 1 | Register adresi datasheet’ten bulundu | ☐ |
| 2 | Okuma kodu çalışıyor | ☐ |
| 3 | UART çıktısı + beklenen değer notu | ☐ |

**Sensör yoksa:** Mentöre söyle; Görev 4’teki datasheet analizi ile devam et, WHO_AM_I kısmını teorik doldur.

---

## Görev 3 — I2C Teorisi (30–45 dk)

Sunum / anlatım sonunda şu sorulara **raporda yazılı** cevap ver.

| # | Soru | Cevap (rapora yaz) |
|---|------|---------------------|
| 1 | I2C nedir? | |
| 2 | UART ve SPI’dan farkı nedir? | |
| 3 | SDA ve SCL ne işe yarar? | |
| 4 | Master ve Slave nedir? | |
| 5 | 7-bit ve 10-bit adres nedir? | |
| 6 | ACK / NACK nedir? | |
| 7 | START ve STOP koşulları nasıl oluşur? | |
| 8 | Clock Stretching nedir? | |
| 9 | Pull-up direnç neden kullanılır? | |

Kaynak: [`01_Anlatim.md`](01_Anlatim.md)

| # | Madde | Yapıldı |
|---|-------|---------|
| 1 | 9 sorunun cevabı `gunluk_rapor.md` içinde | ☐ |
| 2 | Mentör kısa sözlü kontrol | ☐ |

---

## Görev 4 — Datasheet Analizi

Mentör bir sensör datasheet’i verir. Örnekler:

- **SHT40** (yarın kullanacağın)  
- **LIS2DE12**  
- **MPU6050**

### İstenecekler

1. **Slave Address** nedir? (7-bit / alternatif adres varsa not et)  
2. **WHO_AM_I** register’ı var mı? Varsa adres + beklenen değer  
3. **Ölçüm komutu** nedir? (veya hangi register’dan veri okunur)  
4. **Register yapısını** kısa çıkar (en az 4–5 kritik register / komut)  
5. **Okuma ve yazma sırasını** çiz (START → Addr+W → … → STOP)

Örnek sıra şablonu:

```
START
Addr + W
ACK
Register / Command
ACK
[Sr] Addr + R
ACK
Data ...
NACK / STOP
```

| # | Madde | Yapıldı |
|---|-------|---------|
| 1 | Slave address not edildi | ☐ |
| 2 | WHO_AM_I / ID durumu net | ☐ |
| 3 | Ölçüm komutu / veri kaynağı bulundu | ☐ |
| 4 | Register / komut özeti tablosu | ☐ |
| 5 | Okuma–yazma sırası diyagramı raporda | ☐ |

---

## Kabul

Mentöre gösterirken:

- [ ] Scanner en az bir gerçek cihaz adresi basıyor  
- [ ] (Mümkünse) WHO_AM_I beklenen değerde  
- [ ] Teori soruları raporda  
- [ ] Datasheet analizi tamam  

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/
│   └── gunluk_rapor.md    # teori + datasheet notları
└── proje/
    └── (I2C scanner / WHO_AM_I firmware)
```
