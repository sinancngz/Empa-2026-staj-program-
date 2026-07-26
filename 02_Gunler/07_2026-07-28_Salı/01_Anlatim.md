# ADC & Pil Gerilimi Okuma

**Gün 07 · 28 Temmuz 2026 · Tiremo Cortex**

Bu notu okuyarak ADC’nin ne yaptığını, voltajı nasıl hesaplayacağını ve datasheet’ten pil kanalını nasıl bulacağını öğreneceksin. Sonra [`02_Gorevler.md`](02_Gorevler.md) ile uygula.

### Bu notu nasıl kullanmalısın?

1. **§1–4** oku → ADC nedir, çözünürlük, Vref, adım boyutu.  
2. **§5–6** oku → pil nasıl ölçülür, datasheet’te ne ararsın.  
3. Kart dökümanı + MCU datasheet + örnek projeyi aç (`Examples/ADC/ADC_Battery/`).  
4. Görevlere geç: kolay → orta → zor.  
5. Görev dosyasındaki **10 teorik soruyu** cevaplayıp rapora yaz.

### Gün sonu hedefleri

- Analog ile dijital farkını bir cümleyle anlatabilmek.  
- Ham ADC değerini **mV / V** cinsine çevirebilmek.  
- Datasheet / şemadan **pil hangi pin / kanal** üzerinden okunuyor bulabilmek.  
- Tiremo’da pil gerilimini periyodik okuyup UART’a yazabilmek.

---

## 1. ADC nedir?

**ADC** = *Analog to Digital Converter* (Analog–Dijital Dönüştürücü).

Gerçek dünyada pil gerilimi, sıcaklık, ses gibi büyüklükler **sürekli (analog)** değişir. Mikrodenetleyici ise sadece **0 ve 1** anlar. ADC, sürekli sinyali örnekleyip mikrodenetleyicinin işleyebileceği bir **sayıya** çevirir.

![Sürekli sinyal vs ayrık (örneklenmiş) sinyal](kaynaklar/resim1.png)

| Sinyal | Anlam |
|--------|--------|
| **Sürekli (analog)** | Her an sonsuz ara değer olabilir (ör. pil 3.71 V → 3.70 V…) |
| **Ayrık (dijital)** | Belirli anlarda alınmış “fotoğraflar” → 0, 1, 2, … 4095 gibi sayılar |

Kısaca: **Pil gerilimi analogdır → ADC onu sayıya çevirir → sen kodda bu sayıyla çalışırsın.**

> Not: Aşağıdaki örnek sayılar (12 bit, ~3.6 V aralık, kanal sayısı vb.) tipik bir MCU ADC’si içindir (örnek anlatımda STM32F4 tipi değerler kullanılmış olabilir). **Tiremo Cortex’te kesin değerleri her zaman A34G43x datasheet + kart şemasından doğrula.**

---

## 2. ADC’nin temel özellikleri

### 2.1 Çözünürlük (resolution)

Çözünürlük, ölçümü kaç parçaya böldüğünü söyler.

| Çözünürlük | Seviye sayısı | Anlam |
|------------|---------------|--------|
| 8 bit | \(2^8 = 256\) | Kaba ölçüm |
| 10 bit | \(2^{10} = 1024\) | Orta |
| 12 bit | \(2^{12} = 4096\) | Daha hassas |

12 bit → yaklaşık **0 … 4095** arası ham değer (çoğu ADC’de max = \(2^n - 1\)).

### 2.2 Gerilim aralığı ve Vref

ADC “sınırsız voltaj” ölçmez. Genelde **0 … Vref** arasını ölçer.

- Vref ≈ 3.3 V veya 3.6 V gibi bir referans olabilir (MCU / karta göre bak).  
- Vref’ten **yüksek** gerilim doğrudan ADC pinine verilmemeli → hem yanlış ölçüm hem hasar riski.  
- Pil hücresi bazen 4.2 V civarına çıkar → kartta çoğu zaman **gerilim bölücü** vardır. Bu yüzden ADC pininde gördüğün voltaj, pilin tamamı olmayabilir.

### 2.3 Kanal (channel)

ADC’nin birden fazla **analog giriş kanalı** vardır. Her kanal genelde bir MCU pinine veya dahili sinyale bağlıdır.

**Pil okurken kritik soru:**  
> “Batarya sense hattı hangi pin’e geliyor ve bu pin hangi ADC kanalı?”

Bunu tahminle değil, **şema + datasheet** ile bulursun (§6).

### 2.4 Hız vs çözünürlük

Genel kural: çözünürlük arttıkça dönüşüm genelde **daha uzun** sürer. Pil izleme için çok yüksek hız gerekmez; saniyede 1–10 örnek çoğu zaman yeter.

---

## 3. ADC çevrim (conversion) modları — ne işe yarar?

| Mod | Ne yapar? | Ne zaman kullanırsın? |
|-----|-----------|------------------------|
| **Tek çevrim (Single)** | Bir ölçüm alır, durur; tekrar tetiklenene kadar bekler | Butona basınca bir kez ölç |
| **Sürekli (Continuous)** | Bitince otomatik yeniden başlar | Periyodik pil izleme |
| **Tarama (Scan)** | Birden fazla kanalı sırayla ölçer | Pil + başka analog (bugün sadece pil) |
| **Süreksiz (Discontinuous)** | Tetik geldikçe grup içinden sırayla ölçer | Kontrollü / seyrek örnekleme |

Bugünün odağı: **tek kanal → pil**. Mod olarak örnek projede hangisi kullanılıyorsa onu anla; gerekirse tek/sürekli çevrimi tercih et.

---

## 4. Voltajı nasıl hesaplarsın? (en önemli formül)

Ham ADC değeri tek başına “volt” değildir. Voltaja çevirmek için:

![Adım boyutu formülü](kaynaklar/resim2.png)

\[
\text{Adım boyutu} = \frac{V_{ref}}{2^{n} - 1}
\]

Örnek (12 bit, Vref = 3.6 V):

![Örnek hesap](kaynaklar/resim3.png)

\[
\text{Adım} = \frac{3.6}{4095} \approx 0.88\,\text{mV}
\]

Kodda pratik çeviri:

\[
V_{adc} = \text{raw} \times \frac{V_{ref}}{2^{n} - 1}
\]

mV istersen:

\[
V_{mV} = \text{raw} \times \frac{V_{ref\_mV}}{2^{n} - 1}
\]

### Bölücü varsa (çok önemli)

Kartta pil → direnç bölücü → ADC pin ise:

\[
V_{pil} = V_{adc} \times k
\]

Burada \(k\) bölücü oranıdır (ör. 2 ise ADC’de gördüğün voltajın 2 katı pildir).  
\(k\)’yı **şemadaki dirençlerden** hesapla veya kart dökümanından oku. Uydurma.

### Mini örnek

- 12 bit, Vref = 3.3 V, raw = 2048, bölücü yok  
- \(V = 2048 \times 3.3 / 4095 \approx 1.65\,V\)

---

## 5. Bugünün uygulaması: sadece pil okuma

Bugün ADC ile **sadece batarya gerilimini** okuyacaksın.

Yapacağın şey (özet):

1. ADC’yi doğru kanal / pin ile başlat  
2. Dönüşüm al → `raw`  
3. Formülle **mV** hesapla  
4. UART’a yaz (ör. `BAT=3720 mV raw=2890`)  
5. İleride: LOW eşiği + LED uyarısı (görevlerde)

Referans örnek (repo): `Examples/ADC/ADC_Battery/`

---

## 6. Datasheet / şema okuma — ne araştıracaksın?

Mentör cevap vermeden önce şu checklist’i kendin doldur. Bulduklarını rapora yaz.

### A) Kart dökümanı / şema (`Tiremo.Cortex.pdf`, pin map, şema)

| Soru | Cevabın |
|------|---------|
| Pil sense net’inin adı ne? (VBAT, BAT_ADC, …) | |
| Bu net hangi MCU pin’ine gidiyor? (port + pin) | |
| Arada gerilim bölücü var mı? Direnç değerleri? | |
| Bölücü oranı \(k\) kaç? | |

### B) MCU datasheet (A34G43x — ADC bölümü)

| Soru | Cevabın |
|------|---------|
| Bu pin hangi **ADC kanalına** map’leniyor? | |
| ADC çözünürlüğü kaç bit? (yazılımda kaç bit seçilmiş?) | |
| Vref kaynağı ne? Tipik Vref kaç volt? | |
| Örnekleme süresi / clock ile ilgili kritik uyarı var mı? | |
| ADC pin’i max giriş voltajı nedir? | |

### C) Örnek kod (`ADC_Battery`)

| Soru | Cevabın |
|------|---------|
| Hangi kanal / pin define edilmiş? | |
| Ham değer nerede okunuyor? | |
| mV dönüşümü kodda var mı? Formül doğru mu? | |
| Ölçüm ne sıklıkla yapılıyor? | |

### Araştırma sırası (önerilen)

```
1. Kart şemasında BAT / VBAT hattını bul
2. Hangi pin’e gittiğini yaz
3. Datasheet’te o pin → ADC channel tablosunu bul
4. Örnek projedeki kanal ile karşılaştır (aynı mı?)
5. Vref ve bit sayısını netleştir
6. raw → mV formülünü kendi hesapla, kodla karşılaştır
```

Bunu yapmadan “çalıştı” deme. **Kanal yanlışsa ölçüm yanlış olur.**

---

## 7. Pratik ipuçları

- Ölçümü bir kez alıp bırakma; 1 Hz gibi periyodik log daha anlamlı.  
- Tek örnek gürültülü olabilir → ileride ortalama alırsın (bugün zor görev).  
- UART’ta hem `raw` hem `mV` yaz → hata ayıklama kolaylaşır.  
- LOW batarya eşiğini uydurma; hücre tipine göre makul bir mV seç (ör. Li-ion için kaba eşikler mentörle konuş).  
- Secret / credential yok; bu gün sadece ADC + pil.

---

## 8. Sonraki adım

1. Bu notu bitir.  
2. Datasheet checklist’ini doldur.  
3. [`02_Gorevler.md`](02_Gorevler.md) → kolaydan başla.  
4. [`02_Gorevler.md`](02_Gorevler.md) içindeki 10 teorik soruyu cevapla (rapora yaz).
