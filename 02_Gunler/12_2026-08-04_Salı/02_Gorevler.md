# Gün 12 — Görevler (SHT40 Sıcaklık & Nem)

Anlatım: [`01_Anlatim.md`](01_Anlatim.md)

Bugün **tek görev** var. Kolay / orta / zor yok — odaklı bitir.

---

## Ortak hazırlık

- [ ] Dünkü I2C Scanner’da SHT40 adresi görünüyor (`0x44` tipik)  
- [ ] UART debug çalışıyor  
- [ ] Sensirion SHT4x gömülü kütüphanesi indirildi / mentör verdi  
- [ ] Anlatım okundu  

---

## Görev — SHT40 ile sıcaklık ve nem ölç

### Amaç

SHT40’tan periyodik olarak **sıcaklık (°C)** ve **bağıl nem (%RH)** oku; UART’a yaz.

### Nasıl?

1. Sensirion’un resmi **embedded I2C SHT4x** kütüphanesini bul (ör. GitHub: `Sensirion/embedded-i2c-sht4x`).  
2. Projeye ekle (`sht4x` + `sensirion_i2c` kaynakları).  
3. **`sensirion_i2c_hal`** (veya eşdeğeri) dosyasında platform HAL’ini **kendi I2C sürücüne** bağla:
   - init  
   - sleep (µs / ms)  
   - master transmit  
   - master receive  
4. Yüksek hassasiyet (veya datasheet’teki uygun) ölçüm API’sini çağır.  
5. Başarıda T + RH yaz; hatada net `ERR:SHT` log’u ver.

### Örnek çıktı

```
T=23.41 C   RH=47.2 %
T=23.38 C   RH=47.3 %
T=23.40 C   RH=47.1 %
```

Hata örneği:

```
ERR:SHT (-1)
```

### Yapılacaklar

| # | Madde | Yapıldı |
|---|-------|---------|
| 1 | Kütüphane projeye eklendi, derleniyor | ☐ |
| 2 | HAL init / sleep / TX / RX dolduruldu (stub yok) | ☐ |
| 3 | Scanner ile `0x44` (veya kartın adresi) doğrulandı | ☐ |
| 4 | `measure` başarılı; T ve RH UART’ta | ☐ |
| 5 | ~1 Hz civarı periyodik log | ☐ |
| 6 | Hata yolu test edildi (kablo çek / yanlış init → ERR log) | ☐ |
| 7 | Mentöre canlı demo | ☐ |

### Kabul kriterleri

- [ ] Değerler makul aralıkta (oda: kabaca 15–35 °C, nem 20–80 % — ortama göre)  
- [ ] Nefes / el yaklaşınca nem veya sıcaklık **değişiyor** (sabit sahte sayı değil)  
- [ ] CRC / I2C hatası yutulmuyor; log’da görünüyor  
- [ ] HAL gerçekten platform API çağırıyor (boş `return 0` yok)  

---

## Teorik Sorular (Cevapları rapora yaz)

**1.** SHT40’ın tipik 7-bit I2C adresi nedir? Write frame’de bus’a giden ilk byte kabaca ne olur?


**2.** SHT40’ta klasik WHO_AM_I register yerine ne kullanılır? Dünkü LIS/MPU yaklaşımından farkı nedir?


**3.** Bir ölçüm cevabında gelen 6 byte’ın sırası nedir? CRC neden vardır?


**4.** Ölçüm komutundan hemen sonra beklemeden okursan ne olur? Sleep / delay’in rolü nedir?


**5.** Sensirion kütüphanesinde neden tüm projeyi baştan yazmak yerine sadece HAL katmanını değiştiriyoruz?


**6.** `HAL_I2C_IsDeviceReady()` başarılı ama `sht4x_measure` sürekli hata veriyorsa ilk bakacağın 3 şey nedir?


**7.** Ham tick ile °C / %RH arasındaki ilişkiyi kim tanımlar (datasheet mi, senin uydurman mı)?


**8.** Pull-up olmasa dün scanner ve bugün SHT40 ölçümü neden ikisi birden bozulur?

---

## Bonus (zorunlu değil)

| # | Bonus | Yapıldı |
|---|-------|---------|
| 1 | Sıcaklık eşiği aşılınca LED yak | ☐ |
| 2 | °C / °F birim seçimi (buton veya komut) | ☐ |
| 3 | Ardışık 3 hatada “sensor offline” durumu | ☐ |

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/
│   └── gunluk_rapor.md    # teori cevapları + gözlem (T/RH örneği)
└── proje/
    └── (SHT40 + uyarlanmış HAL)
```
