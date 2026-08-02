# SHT40 — Sıcaklık ve Nem (I2C)

**Gün 12 · 4 Ağustos 2026 · Tiremo Cortex**

Dün I2C bus’unu, adresi ve ACK’i öğrendin. Bugün aynı hatta **SHT40** ile sıcaklık (°C) ve bağıl nem (%RH) okuyacaksın.

Uygulama: [`02_Gorevler.md`](02_Gorevler.md)

### Bu notu nasıl kullanmalısın?

1. SHT40’ın komut modelini anla (klasik register map değil).  
2. Sensirion gömülü kütüphanesini bul; **HAL katmanını** kendi I2C’ne bağla.  
3. Ölç → CRC kontrol et → °C / %RH’ye çevir → UART’a yaz.  
4. Tek görevi bitir; rapora teori cevaplarını ekle.

### Gün sonu hedefleri

- SHT40 slave adresini ve ölçüm komutunu söyleyebilmek.  
- Sensirion driver’da hangi dosyaların “senin HAL’in” olduğunu bilmek.  
- Sıcaklık + nem’i periyodik UART log’unda görmek.  
- CRC’nin ne işe yaradığını bir cümleyle anlatmak.

---

## 1. Dünden bugüne

| Dün (Pazartesi) | Bugün (Salı) |
|-----------------|--------------|
| I2C teorisi | SHT40 uygulaması |
| Scanner → cihaz adresi | Bilinen adrese ölçüm komutu |
| WHO_AM_I / datasheet | Sıcaklık + nem değeri |
| “Cihaz var mı?” | “Ortam kaç derece / nem?” |

Zincir:

```
MCU (Master)  --I2C--  SHT40 (Slave 0x44)
                 │
                 ▼
         T [°C] + RH [%]
                 │
                 ▼
              UART log
```

---

## 2. SHT40 nedir?

**SHT40**, Sensirion’un dijital **sıcaklık + bağıl nem** sensörüdür.

| Özellik | Tipik |
|---------|--------|
| Arayüz | I2C |
| 7-bit slave address | **`0x44`** (çoğu SHT40 varyantı) |
| Çıkış | Sıcaklık + nem (ham tick → fiziksel birim) |
| Güç | Düşük; ölçüm komutu ile tetiklenir |

Kartında / breakout’ta SDA–SCL–VDD–GND + pull-up olduğunu dünden doğrulamış olmalısın. Scanner’da `0x44` gördüysen doğru yoldasın.

---

## 3. Register map yok — komut modeli var

MPU6050 / LIS2DE12’de “şu register’ı oku” dersin. SHT40’ta çoğu işlem **tek byte (veya kısa) komut** göndermekle başlar.

Tipik yüksek hassasiyet ölçüm akışı (kavramsal):

```
1. START
2. Addr 0x44 + Write
3. Ölçüm komutu (ör. high precision measure)
4. STOP (veya bus serbest)
5. Sensör ölçümü tamamlar (~ birkaç ms; datasheet)
6. START
7. Addr 0x44 + Read
8. 6 byte oku: T_MSB, T_LSB, T_CRC, RH_MSB, RH_LSB, RH_CRC
9. STOP
10. CRC doğrula → tick’leri °C / %RH formülüyle çevir
```

> Kesin komut kodları ve süreler **SHT40 datasheet** / Sensirion driver’dadır. Ezberleme; kaynaktan bak.

### CRC

Her 16-bit ham değere 8-bit **CRC** gelir. Bit hatası / yanlış okuma yakalamak içindir. Kütüphane genelde CRC’yi senin yerinne kontrol eder; sen “CRC fail = ölçümü çöpe at / tekrar dene” mantığını bil.

---

## 4. Ham tick → fiziksel birim

Sensör ham **tick** (unsigned 16-bit) döner. Datasheet formülü kabaca:

- Sıcaklık: tick → °C  
- Nem: tick → %RH  

Sensirion kütüphanesi `sht4x_measure_ticks` / `sht4x_measure` benzeri API ile bunu yapar. Kendi formülünü yazmana gerek yok; ama formülün datasheet’te olduğunu bil.

Örnek UART hedefi:

```
T=23.41 C   RH=47.2 %
T=23.40 C   RH=47.3 %
```

---

## 5. Sensirion kütüphanesi + HAL uyarlama

Resmi gömülü driver (I2C SHT4x ailesi):

- GitHub: **Sensirion `embedded-i2c-sht4x`**  
  (veya mentörün verdiği aynı aile paket)

Paket genelde şöyle ayrılır:

| Katman | Dosyalar (isimler değişebilir) | Kim yazar? |
|--------|--------------------------------|------------|
| Sensör API | `sht4x.c` / `sht4x.h` | Sensirion — dokunma / az dokun |
| I2C protokol yardımcı | `sensirion_i2c.c` | Sensirion |
| **HAL (platform)** | `sensirion_i2c_hal.c` / `.h` | **Sen** |

### HAL’de senin doldurman gerekenler (tipik)

Kütüphane soyut fonksiyonlar bekler; örnek isimler:

- `sensirion_i2c_hal_init` — I2C peripheral hazır  
- `sensirion_i2c_hal_free` — (gerekirse)  
- `sensirion_i2c_hal_sleep_usec` — bekleme (ölçüm süresi)  
- `sensirion_i2c_hal_select_bus` — (tek bus ise boş/no-op)  
- Transmit / receive: master **write** ve **read** (senin `HAL_I2C_Master_Transmit` / `Receive` veya platform API)

Mantık:

```
sht4x_measure()
    → kütüphane komutu I2C ile gönderir
    → sleep (ölçüm süresi)
    → 6 byte okur
    → CRC + dönüşüm
    → sana T ve RH verir
```

Sen sadece **byte’ları doğru I2C handle ile gönder/al** ve **mikro-saniye sleep** sağla.

### Sağlıklı kullanım checklist

- [ ] Slave address kütüphanede `0x44` (7-bit) ile uyumlu  
- [ ] HAL write/read gerçekten ACK alıyor (dün scanner ile doğrula)  
- [ ] Sleep süresi datasheet / driver’ın istediğinden kısa değil  
- [ ] Dönüş değerleri (`NO_ERROR`) kontrol ediliyor  
- [ ] Hata olunca UART’ta `ERR:SHT` benzeri net log  

Mentör Cube projesine kütüphaneyi nasıl ekleyeceğinizi gösterecek (include path, kaynak dosyaları).

---

## 6. Uygulama iskeleti

```c
/* pseudo — gerçek API isimleri kütüphaneye göre */
int main(void)
{
    System_Init();
    UART_Init();
    sensirion_i2c_hal_init();
    sht4x_init(0x44);   /* örnek */

    while (1) {
        float t_c, rh;
        int16_t err = sht4x_measure_high_precision(&t_c, &rh);
        if (err == 0) {
            printf("T=%.2f C   RH=%.1f %%\r\n", t_c, rh);
        } else {
            printf("ERR:SHT (%d)\r\n", err);
        }
        HAL_Delay(1000);  /* ~1 Hz log */
    }
}
```

---

## 7. Sık yapılan hatalar

| Belirti | Muhtemel neden |
|---------|----------------|
| Scanner’da yok | Kablo, GND, pull-up, yanlış I2C instance |
| Hep CRC / read error | Sleep kısa, yanlış adres (7 vs 8 bit), bus noise |
| Sabit saçma değer | Yanlış dönüşüm / eski buffer / init yok |
| Derleme OK, runtime fail | HAL stub’ları boş bırakılmış (`return 0` sahte) |

---

## 8. Teori (kısa tekrar)

Bugün pratik ağırlıklı; yine de şunları bil:

1. SHT40 neden “WHO_AM_I register” yerine **komut** kullanır?  
2. 6 byte cevabın sırası nedir? CRC neden var?  
3. HAL katmanını değiştirmek neden doğru yaklaşım? (taşınabilirlik)  
4. Ölçüm sonrası neden birkaç ms beklemek gerekir?  
5. `0x44` 7-bit midir, Write frame’de bus’ta ne görünür?

Cevapları rapora yaz — görev dosyasında liste var.

---

## Özet

- SHT40 = I2C sıcaklık + nem, adres çoğu zaman **`0x44`**.  
- Ölçüm = komut gönder → bekle → 6 byte oku → CRC → °C / %RH.  
- Sensirion driver kullan; **sadece HAL’i** platformuna uyarla.  
- Tek ürün hedefi: periyodik, doğru T + RH logu.

Detaylı tek görev: [`02_Gorevler.md`](02_Gorevler.md)
