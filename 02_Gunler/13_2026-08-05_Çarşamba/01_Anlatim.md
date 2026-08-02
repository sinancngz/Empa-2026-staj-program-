# LIS2DE12 — İvmeölçer (X, Y, Z)

**Gün 13 · 5 Ağustos 2026 · Tiremo Cortex**

Pazartesi I2C’yi, Salı SHT40’ı gördün. Bugün aynı bus’ta **LIS2DE12** (veya LIS2DE12TR) ile **X / Y / Z ivme** okuyacaksın.

Uygulama: [`02_Gorevler.md`](02_Gorevler.md)

### Bu notu nasıl kullanmalısın?

1. İvmeölçerin ne ölçtüğünü ve g / mg birimini anla.  
2. Datasheet’ten adres, WHO_AM_I, CTRL ve OUT register’larını çıkar.  
3. Sensörü aç (ODR + eksen enable) → XYZ oku → UART’a yaz.  
4. Ana görevi bitir; yan görev ve teori sorularını rapora ekle.

### Gün sonu hedefleri

- WHO_AM_I ile sensörü doğrulayabilmek.  
- CTRL register’larıyla ölçümü açabilmek.  
- X, Y, Z’yi periyodik log’da görmek.  
- Kartı eğince hangi eksenin değiştiğini söyleyebilmek.

---

## 1. Dünden bugüne

| Salı | Bugün (Çarşamba) |
|------|------------------|
| SHT40: sıcaklık + nem | LIS2DE12: ivme X/Y/Z |
| Komut gönder → bekle → oku | Register yaz / oku |
| CRC + formül | Ham ivme (+ isteğe bağlı mg) |
| Adres `0x44` | Adres `0x18` veya `0x19` |

Zincir:

```
MCU (Master)  --I2C--  LIS2DE12 (Slave)
                 │
                 ▼
          OUT_X, OUT_Y, OUT_Z
                 │
                 ▼
            UART: X Y Z
```

Aynı I2C hattında SHT40 da duruyor olabilir; farklı slave adresleri ile çakışmaz.

---

## 2. İvmeölçer nedir?

**İvmeölçer (accelerometer)**, birim zamandaki hız değişimini — yani **ivmeyi** — üç eksende ölçer.

| Eksen | Tipik anlam (kart düzken) |
|-------|---------------------------|
| **X** | Sağ–sol |
| **Y** | İleri–geri |
| **Z** | Yukarı–aşağı |

Dünya yerçekimi ≈ **1 g** ≈ 9.81 m/s².

- Kart düz, sabit duruyorsa: bir eksen ≈ **±1 g**, diğerleri ≈ **0** (orientasyona göre).  
- Kartı eğer / sallasın → eksenler değişir.

Bu yüzden “doğru çalışıyor mu?” testi basit: **eğ → değerler değişsin**.

---

## 3. LIS2DE12’ye kısa bakış

ST’nin düşük güçlü 3 eksenli dijital ivmeölçeri.

| Özellik | Tipik |
|---------|--------|
| Arayüz | I2C (SPI de destekler; biz I2C) |
| 7-bit adres | **`0x18`** veya **`0x19`** (SA0 / SDO pinine göre) |
| WHO_AM_I | Register **`0x0F`**, beklenen **`0x33`** |
| Çözünürlük | 8-bit çıktı (LIS2DE12 ailesi) |
| Full-scale | ±2 / ±4 / ±8 / ±16 g (CTRL ile) |

> Kesin register isimleri ve bit alanları **datasheet**’tedir. Aşağıdaki adresler yaygın referanstır; mentör PDF’i ile doğrula.

### Pazartesi köprüsü

Dün/önceki gün WHO_AM_I okuduysan bugün ilk iş aynı:

```
WHO_AM_I (0x0F) == 0x33  →  doğru cihaz, doğru adres
```

Scanner’da `0x18` veya `0x19` görmelisin.

---

## 4. Kritik register’lar

| Register | Adres (hex) | İş |
|----------|-------------|-----|
| `WHO_AM_I` | `0x0F` | Kimlik (`0x33`) |
| `CTRL_REG1` | `0x20` | ODR (örnekleme), X/Y/Z enable, low-power |
| `CTRL_REG4` | `0x23` | Full-scale (±2g …), blok güncelleme vb. |
| `OUT_X` | `0x29` | X ivme (8-bit, signed) |
| `OUT_Y` | `0x2B` | Y ivme |
| `OUT_Z` | `0x2D` | Z ivme |
| `STATUS_REG` | `0x27` | Yeni veri hazır mı? (ZYXDA vb.) |

### Neden “açmak” gerekiyor?

Power-on’da sensör çoğu zaman **ölçüm kapalı / ODR = power-down** gelir. Sadece OUT register okumak yetmez:

1. `WHO_AM_I` doğrula  
2. `CTRL_REG1` ile ODR seç + eksenleri enable et  
3. Gerekirse `CTRL_REG4` ile full-scale ayarla  
4. Sonra `OUT_X/Y/Z` oku  

### ODR nedir?

**Output Data Rate** — saniyede kaç örnek üretir.  
Örnek: 25 Hz, 100 Hz… Staj log’u için düşük ODR + 100–200 ms UART periyodu yeter.

### Full-scale

| Ayar | Aralık | Hassasiyet hissi |
|------|--------|------------------|
| ±2 g | Dar | Daha ince (küçük hareket) |
| ±16 g | Geniş | Sert sarsıntı; ince detay kaybolur |

Başlangıç: **±2 g** veya **±4 g**.

---

## 5. Okuma sırası (I2C)

Tek register okuma (Pazartesi’deki klasik yol):

```
START
Addr + W
ACK
Register adresi (ör. 0x0F)
ACK
Sr (Repeated START)
Addr + R
ACK
Data
NACK + STOP
```

XYZ için üç kez tekil okuma veya (destekleniyorsa) **auto-increment** ile ardışık okuma kullanılabilir. Mentörün HAL’i `Mem_Read` sunuyorsa:

```c
HAL_I2C_Mem_Read(&hi2c, DevAddr, REG, I2C_MEMADD_SIZE_8BIT, &data, 1, timeout);
```

### İşaretli değer

`OUT_*` genelde **signed 8-bit** (`int8_t`).  
`uint8_t` sanırsan eğince “255, 254…” gibi saçma pozitifler görürsün — önce `int8_t`’e cast et.

```c
int8_t x = (int8_t)raw_x;
int8_t y = (int8_t)raw_y;
int8_t z = (int8_t)raw_z;
```

---

## 6. Ham değer → mg / g (isteğe bağlı)

8-bit + full-scale’e göre her LSB’nin mg karşılığı datasheet’te tablo ile verilir.

Kabaca fikir (±2 g, 8-bit):

- Yaklaşık hassasiyet satırına datasheet’ten bak  
- `mg = raw * sensitivity_mg_per_lsb`

Ana görev için **ham X Y Z** yeter. Yan görevde mg’ye çevirmek güzel olur.

---

## 7. Uygulama iskeleti

```c
/* pseudo */
#define LIS_ADDR_7BIT   0x18
#define REG_WHO_AM_I    0x0F
#define REG_CTRL_REG1   0x20
#define REG_OUT_X       0x29
#define REG_OUT_Y       0x2B
#define REG_OUT_Z       0x2D

uint8_t who = 0;
I2C_ReadReg(LIS_ADDR_7BIT, REG_WHO_AM_I, &who);
printf("WHO_AM_I = 0x%02X\r\n", who);   /* beklenen 0x33 */

/* ODR + Xen Yen Zen — bit değerlerini datasheet'ten doldur */
I2C_WriteReg(LIS_ADDR_7BIT, REG_CTRL_REG1, 0x57);  /* örnek; doğrula! */

while (1) {
    int8_t x, y, z;
    I2C_ReadReg(LIS_ADDR_7BIT, REG_OUT_X, (uint8_t *)&x);
    I2C_ReadReg(LIS_ADDR_7BIT, REG_OUT_Y, (uint8_t *)&y);
    I2C_ReadReg(LIS_ADDR_7BIT, REG_OUT_Z, (uint8_t *)&z);

    printf("X=%d  Y=%d  Z=%d\r\n", x, y, z);
    Delay_ms(200);
}
```

> `0x57` gibi magic number’ı körü körüne kopyalama; CTRL bitlerini datasheet tablosundan kendin seç.

---

## 8. Orientasyon testi (elle)

Kartı düz tut → bir eksen büyük (|~1 g ham karşılığı|), diğerleri küçük.  
Sonra:

| Hareket | Beklenti |
|---------|----------|
| X etrafında yatır | X değişir / Z ile yer değiştirir |
| Y etrafında yatır | Y değişir |
| Sert salla | Üç eksende ani sıçrama |

UART’ta sayıların **canlı** değişmesi ana kabul kriteridir.

---

## 9. Sık hatalar

| Belirti | Muhtemel neden |
|---------|----------------|
| WHO_AM_I yanlış / NACK | Yanlış adres (`0x18` vs `0x19`), kablo, pull-up |
| Hep 0 | CTRL yazılmadı; ODR = power-down; yanlış register |
| Sabit saçma | `int8_t` unutuldu; yanlış full-scale varsayımı |
| SHT40 bozuldu | Aynı bus OK; ayrı adres — init sırası / bus hang kontrol et |

---

## Özet

- LIS2DE12 = 3 eksen ivme, I2C, WHO_AM_I = `0x33`.  
- Önce kimlik → CTRL ile aç → OUT_X/Y/Z oku.  
- Ana ürün: UART’ta canlı **X Y Z**.  
- Eğince değişmeyen sayı = henüz bitmedi.

Detay: [`02_Gorevler.md`](02_Gorevler.md)
