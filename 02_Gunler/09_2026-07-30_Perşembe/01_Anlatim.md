# Mikrofon & ADC Okuma

**Gün 09 · 30 Temmuz 2026 · Tiremo Cortex**

Bu not **teori** notudur. Okuduktan sonra uygula: [`02_Gorevler.md`](02_Gorevler.md).

### Bu notu nasıl kullanmalısın?

1. Analog mikrofonun pil ADC’sinden farkını anla (AC sinyal + bias).  
2. Şema / datasheet’te mikrofon pin ve ADC kanalını bul.  
3. Raw → voltaj formülünü hatırla.  
4. Görevde UART’ta `MIC = …` değerlerini gör; sessiz / sesli farkı not et.

---

## 1. Bugün ne yapıyoruz?

Dün / önceki ADC günlerinde **pil gerilimi** gibi yavaş değişen (neredeyse DC) bir sinyali okuduk.

Bugün hedef: kart üzerindeki **analog MEMS mikrofon** çıkışını ADC ile okuyup terminalde görmek.

```
Ses (hava basıncı değişimi)
        │
        ▼
Analog MEMS mikrofon  →  elektrik sinyali (AC)
        │
        ▼
ADC kanalı            →  ham sayı (ör. 0…4095)
        │
        ▼
UART terminal         →  MIC = 2048
```

Referans örnek (varsa): `Examples/ADC/ADC_Microphone/`

> Pin, kanal, Vref ve bit sayısı için kesin bilgiyi **kart şeması + A34G43x datasheet**’ten doğrula.

---

## 2. Analog mikrofon nedir?

**MEMS mikrofon**, ses dalgasını (basınç değişimini) küçük bir kapasitif yapı ile **elektrik sinyaline** çevirir.

Tiremo Cortex’te mikrofon **analog çıkışlıdır**:

| Tip | Çıkış | ADC gerekir mi? |
|-----|--------|-----------------|
| Analog mikrofon | Sürekli gerilim | Evet |
| Dijital mikrofon (PDM / I2S) | Sayısal stream | Genelde hayır (özel arayüz) |

Bu yüzden mikrofon hattı bir **ADC giriş pinine** bağlanır.

---

## 3. Pil ADC’si ile mikrofon ADC’si farkı

| | Pil | Mikrofon |
|---|-----|----------|
| Sinyal karakteri | Yavaş / DC benzeri | Hızlı / AC (dalga) |
| Sessizken değer | Stabil voltaj | Genelde **orta seviye (bias)** civarı |
| Ses gelince | Değişmez | Ham değer **yukarı–aşağı salınır** |
| Okuma hızı ihtiyacı | Düşük (sn mertebesi) | Daha yüksek (ms / daha sık) |

### Bias (orta nokta) — kritik fikir

Analog mikrofon çıkışı çoğu kartta **0 V etrafında değil**, Vref’in ortasına yakın bir **DC ofset (bias)** üzerindedir.

Örnek (12 bit, Vref = 3.3 V):

```
Sessiz ortamda tipik ham değer ≈ 2048  →  ~1.65 V
```

Ses gelince değer bu orta noktanın **üstüne ve altına** salınır:

```
         3000  ·
              / \
  bias 2048 ·----·----·----  → zaman
              \ /
         1000  ·
```

Yani:

- Tek bir `MIC = 2100` satırı “ses seviyesi” demek değildir.  
- Ses, **zaman içinde salınımın büyüklüğü** ile anlaşılır.

Bu yüzden yarın (Cuma) değerleri Python’da **grafik** olarak izleyeceğiz; bugün önce hattı çalıştırıp raw okumayı öğreniyoruz.

---

## 4. ADC hatırlatması (mikrofon için)

### 4.1 Raw → voltaj

\[
V_{adc} = \text{raw} \times \frac{V_{ref}}{2^{n} - 1}
\]

12 bit, Vref = 3.3 V, raw = 2048:

\[
V \approx 2048 \times 3.3 / 4095 \approx 1.65\,V
\]

### 4.2 Kanal doğru mu?

Yanlış ADC kanalı seçersen:

- Sabit saçma değer görürsün, veya  
- Başka bir hattın (ör. pil) değerini okursun.

Araştırma sırası:

```
1. Şemada MIC / mikrofon net’ini bul
2. Hangi MCU pin’ine gittiğini yaz
3. Datasheet’te pin → ADC channel
4. Örnek kodda aynı kanalı kullan
5. Sessiz / sesli farkı terminalde doğrula
```

---

## 5. Örnekleme (sampling) — kısa

ADC bir anda sürekli sinyali “fotoğraflar”. Bu işleme **örnekleme** denir.

| Kavram | Anlam |
|--------|--------|
| Örnekleme frekansı \(f_s\) | Saniyede kaç örnek |
| Nyquist | \(f_s > 2 \cdot f_{sinyal}\) olmalı |
| Düşük \(f_s\) | Dalga bozulur, yanlış frekans görünür |

Bugün görevde genelde **100–500 ms’de bir** tek değer yazdırmak yeterli (kurulum doğrulama).

Yarın: dalga şeklini görmek için **çok daha sık** örnek gönderip Python’da çizeceğiz. Test için telefonda **1 kHz sinüs** dinletilecek.

---

## 6. UART çıktısı nasıl görünmeli?

Örnek format (görevle uyumlu):

```
MIC = 2034
MIC = 2050
MIC = 1987
MIC = 2201
```

Gözlem checklist:

| Ortam | Beklenen |
|-------|----------|
| Sessiz | Değerler dar bir bantta (bias civarı) |
| Konuşma / alkış | Salınım artar; min–max aralığı büyür |
| Yanlış kanal | Sesle hiç değişmez veya anlamsız sabit |

Bonus görevlerde:

- Seviye etiketi (`QUIET` / `NORMAL` / `LOUD`)  
- Peak / alarm  
- Bit status register (`mic_status`)

kullanılabilir — detay: [`02_Gorevler.md`](02_Gorevler.md).

---

## 7. Pratik ipuçları

1. **USB kablo / COM port** doğru mu? Baud rate mentör / örnek ile aynı mı?  
2. İlk ölçümde sessiz ortam baseline’ını yaz (ör. ortalama ~2040).  
3. Telefonda ses açıp mikrofona yaklaştır; değerlerin oynamasını izle.  
4. Raporuna: sessiz raw, sesli raw, voltaj hesabı, pin/kanal bilgisini ekle.  
5. Bit işlemleri gününden gelen alışkanlık: status bitlerini `|` / `&` ile yönet.

---

## 8. Yarın önizleme (Gün 10)

Bugün UART’ta tek tek sayılar görüyorsun.

Yarın:

- MCU’dan örnekleri daha hızlı stream et  
- Python (`pyserial` + `matplotlib`) ile canlı grafik  
- **1 kHz** test tonu → sinüs benzeri dalga

Bugünkü hattın çalışması yarının ön şartı.

---

## 9. Sonraki adım

1. Bu teoriyi bitir.  
2. Şema / datasheet’te mikrofon pin + ADC kanalını netleştir.  
3. [`02_Gorevler.md`](02_Gorevler.md) → ADC oku, UART yaz, sessiz/sesli karşılaştır.  
4. Teorik soruları rapora cevapla.
