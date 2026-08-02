# I2C Haberleşme Protokolü

**Gün 11 · 3 Ağustos 2026 · Tiremo Cortex**

Bu not **I2C teorisi** notudur. Okuduktan sonra uygula: [`02_Gorevler.md`](02_Gorevler.md).  
Yarın (Salı): aynı bus üzerinden **SHT40** ile sıcaklık / nem okuyacaksın.

### Bu notu nasıl kullanmalısın?

1. UART / SPI ile I2C farkını netleştir.  
2. SDA–SCL, START–STOP, adres + R/W, ACK/NACK zincirini ezberle.  
3. Pull-up ve clock stretching’in nedenini bir cümleyle söyleyebil.  
4. Görevlerde: bus tara → WHO_AM_I oku → datasheet’ten register çıkar.

### Gün sonu hedefleri

- “I2C nedir?” sorusuna **iki hat + adres + ACK** ile cevap verebilmek.  
- 7-bit slave adresin bus’ta nasıl 8-bit frame’e döndüğünü anlatmak.  
- `HAL_I2C_IsDeviceReady()` ile taramanın ne yaptığını bilmek.  
- Datasheet’te slave address / WHO_AM_I / okuma sırasını bulabilmek.

---

## 1. I2C nedir?

**I2C** (*Inter-Integrated Circuit*), iki hat üzerinden çalışan **senkron** bir seri haberleşme protokolüdür.

| | |
|---|---|
| **Hatlar** | **SCL** (clock) + **SDA** (data) |
| **Mimari** | Master–Slave |
| **Seçim** | Her slave’in benzersiz **adresi** vardır |
| **Boşta** | Her iki hat da **HIGH** (pull-up sayesinde) |

Kısaca: ortak bir bus’ta birçok cihaz; master kime konuşacağını **adres** ile seçer.

---

## 2. UART ve SPI’dan farkı

| | UART | SPI | I2C |
|---|------|-----|-----|
| Hat sayısı | 2 (TX/RX) + GND | 4+ (SCLK, MOSI, MISO, CS…) | **2** (SCL, SDA) |
| Clock | Yok (asenkron) | Var | **Var** |
| Cihaz seçimi | Noktadan noktaya | Chip Select (CS) pini | **Slave adresi** |
| Çoklu cihaz | Zor (çok UART / mux) | Her cihaz için ekstra CS | Aynı 2 hatta birçok slave |
| Hız (kabaca) | Orta | Çok yüksek | Orta (SPI’dan yavaş) |
| Tipik kullanım | Debug, PC, modem | Flash, display, hızlı ADC | Sensör, EEPROM, RTC |

**Ne zaman I2C?** Az pin, birden fazla yavaş/orta hızlı sensör aynı hatta.

---

## 3. SDA ve SCL

| Hat | Adı | İş |
|-----|-----|-----|
| **SCL** | Serial Clock Line | Master genelde clock üretir; her bit bir clock darbesiyle senkronize edilir |
| **SDA** | Serial Data Line | Adres, komut ve veri bu hattan gider; hem master hem slave sürebilir (open-drain) |

Boşta her iki hat **HIGH**’tır. Cihazlar hattı **LOW**’a çeker; HIGH’a kendileri “itmez”, **pull-up direnç** yükseltir.

---

## 4. Master ve Slave

| Rol | Ne yapar? |
|-----|-----------|
| **Master** | İletişimi başlatır (START), clock üretir, adresi gönderir, STOP ile bitirir |
| **Slave** | Adresi dinler; kendisine gelince ACK verir; komuta göre veri okur/yazar |

Olası topolojiler:

- Tek master – çok slave (en yaygın)  
- Çok master – tek/çok slave (nadir; arbitration gerekir)

Kartında MCU = **master**, SHT40 / ivmeölçer / EEPROM = **slave**.

---

## 5. Adresleme: 7-bit ve 10-bit

### 7-bit (standart, senin işin)

Her slave’in **7-bit** adresi vardır. Örnek: `0x44`, `0x68`.

Bus’ta gönderilen ilk byte aslında **8 bit**:

```
[ 7-bit slave adresi ][ R/W ]
```

- **R/W = 0** → Master **yazar** (Write)  
- **R/W = 1** → Master **okur** (Read)

Nasıl üretilir?

1. 7-bit adresi **1 bit sola kaydır**.  
2. LSB’ye R/W koy.

Örnek — slave `0x50` (`1010000`):

| İşlem | Değer |
|-------|-------|
| 7-bit adres | `0x50` |
| 1 bit sola | `0xA0` |
| Write (R/W=0) | `0xA0` |
| Read (R/W=1) | `0xA1` |

> **Dikkat:** Datasheet bazen “7-bit address = 0x44”, bazen “8-bit write address = 0x88” yazar. Hangisini kullandığını bil; HAL fonksiyonları genelde **7-bit** ister.

### 10-bit

Daha geniş adres alanı; iki byte’lık özel format. Günlük sensör işinde nadir. Bugün odak **7-bit**.

### Tarama aralığı

Geçerli 7-bit kullanıcı adresleri pratikte çoğunlukla **`0x08`–`0x77`**. Reserved adresler (genel call vb.) bu aralığın dışında / özeldir. Scanner görevinde bu aralığı tara.

---

## 6. START ve STOP

Hatlar boşta HIGH iken:

| Koşul | Nasıl oluşur? | Anlam |
|-------|----------------|-------|
| **START** | SCL = HIGH iken SDA **HIGH → LOW** | “Konuşma başlıyor” |
| **STOP** | SCL = HIGH iken SDA **LOW → HIGH** | “Konuşma bitti, bus serbest” |

**Repeated START:** STOP olmadan yeni bir START. Tipik kullanım: önce register adresi yaz (Write), sonra Repeated START + Read ile veriyi al.

---

## 7. ACK / NACK

Her 8 bitlik byte’tan sonra **1 bit** cevap:

| | SDA | Anlam |
|---|-----|-------|
| **ACK** | LOW | “Aldım / buradayım / devam” |
| **NACK** | HIGH (bırakılmış) | “Yokum / istemiyorum / son byte” |

Örnekler:

- Slave, kendi adresini görünce **ACK** verir → cihaz var.  
- Adres yanlış / cihaz yok → **NACK** (veya timeout).  
- Master okurken son byte’ta genelde **NACK** gönderir → “yeter, bitir”.

`HAL_I2C_IsDeviceReady()` özünde şunu yapar: adrese Write dener → ACK gelirse cihaz **hazır**.

---

## 8. Tipik I2C işlem sırası

Sensörden register okuma (klasik):

```
1. START
2. Slave adresi + Write
3. Slave ACK
4. Register adresi (ör. WHO_AM_I)
5. Slave ACK
6. Repeated START
7. Slave adresi + Read
8. Slave ACK
9. Slave veri gönderir (ör. 0x33)
10. Master NACK (son byte) + STOP
```

Sıcaklık okuma örneği (kavramsal):

```
START → Addr+W → komut → Sr → Addr+R → data… → STOP
```

---

## 9. Clock Stretching

Slave, henüz hazır değilse **SCL’yi LOW tutarak** master’ı bekletebilir. Buna **clock stretching** denir.

- Master, clock’u HIGH yapmak ister ama hat LOW kalır → slave işini bitirene kadar bekler.  
- Sensör ölçüm yaparken veya EEPROM yazarken görülebilir.  
- Driver/HAL tarafında timeout ile korunur; sonsuz beklememek gerekir.

---

## 10. Pull-up direnç neden gerekir?

I2C hatları **open-drain / open-collector** çalışır:

- Cihaz hattı yalnızca **LOW**’a çekebilir.  
- HIGH’ı üretmek için harici (veya dahili) **pull-up** gerekir.

| Konu | Not |
|------|-----|
| Tipik değer | ~2.2 kΩ – 10 kΩ (hız, hat kapasitesi, VDD’ye göre) |
| Pull-up yoksa | Hat LOW’da kalır / iletişim çöker |
| Çok güçlü pull-up | Slave LOW’a zor çeker; güç/EMI |
| Çok zayıf pull-up | Yükselme yavaş → yüksek hızda hata |

Kartında pull-up’lar genelde sensör breakout’ta veya ana kartta vardır; “bus ölü” ise önce **pull-up / kablo / ortak GND** kontrol et.

---

## 11. Hız modları (kısa)

| Mod | Hız |
|-----|-----|
| Standard | 100 kbit/s |
| Fast | 400 kbit/s |
| Fast Mode Plus | 1 Mbit/s |
| High-Speed | 3.4 Mbit/s |

Stajda çoğu sensör **100 veya 400 kHz** ile yeter.

---

## 12. Avantaj / dezavantaj

**Artı**

- Sadece 2 hat  
- Adres ile çoklu cihaz  
- Sensör dünyasında standart  

**Eksi**

- SPI’dan yavaş  
- Uzun kablo / parazit hassas  
- Pull-up ve bus kapasitesi yönetimi  
- Debugging bazen UART kadar “görünür” değil (logic analyzer / scanner şart)

---

## 13. Cube / HAL tarafında ne göreceksin?

Mentörün kullandığı isimlendirme STM32 Cube tarzıysa:

| Fonksiyon (örnek) | İş |
|-------------------|-----|
| `HAL_I2C_IsDeviceReady()` | Adrese ping → ACK var mı? |
| `HAL_I2C_Mem_Read()` | Register oku |
| `HAL_I2C_Mem_Write()` | Register yaz |
| `HAL_I2C_Master_Transmit/Receive()` | Ham byte gönder / al |

Platform farklı olsa da mantık aynı: **adres + R/W + ACK + byte akışı**.

---

## 14. WHO_AM_I nedir?

Birçok sensörde (LIS2DE12, MPU6050, ISM330…) sabit bir **kimlik register’ı** vardır.

- Datasheet’te adı: `WHO_AM_I`, `WHOAMI`, `Device ID`…  
- Okuyunca beklenen sabit değer gelir (ör. `0x33`).  
- Bus ve adres doğru mu diye **en hızlı doğrulama**.

Yarın SHT40’ta klasik WHO_AM_I olmayabilir; Sensirion’da serial number / status komutları vardır. Bugün datasheet görevinde bunu ayırt edeceksin.

---

## 15. Yarına köprü

| Bugün | Yarın (Salı) |
|-------|----------------|
| Bus’u anla, tara, ACK gör | SHT40’tan sıcaklık + nem oku |
| Datasheet’ten adres / register çıkar | Sensirion kütüphanesi + kendi HAL katmanın |
| Teori sorularına cevap ver | Tek odaklı ölçüm görevi |

---

## Özet checklist (kendine sor)

- [ ] I2C = SCL + SDA, senkron, adresli  
- [ ] START / STOP nasıl oluşuyor?  
- [ ] 7-bit adres → 8-bit frame (R/W)  
- [ ] ACK = SDA LOW  
- [ ] Pull-up neden var?  
- [ ] Clock stretching ne işe yarar?  
- [ ] Scanner `0x08`–`0x77` tarar  

Detaylı uygulama: [`02_Gorevler.md`](02_Gorevler.md)
