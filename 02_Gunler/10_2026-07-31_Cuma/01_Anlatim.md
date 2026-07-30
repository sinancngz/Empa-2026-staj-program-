# Mikrofon Stream & Python Canlı Grafik

**Gün 10 · 31 Temmuz 2026 · Tiremo Cortex**

Bu not **teori + PC tarafı** notudur. Okuduktan sonra uygula: [`02_Gorevler.md`](02_Gorevler.md).  
Hazır script: [`kaynaklar/mic_plot.py`](kaynaklar/mic_plot.py)

### Bu notu nasıl kullanmalısın?

1. Dünkü raw okumanın neden “dalga” olmadığını anla.  
2. Nyquist + 1 kHz test fikrini öğren.  
3. UART satır formatını sabitle.  
4. Önce `--simulate`, sonra gerçek COM port ile grafiği çalıştır.

---

## 1. Dünden bugüne

| Dün (Perşembe) | Bugün (Cuma) |
|----------------|--------------|
| ADC’den mikrofon oku | Aynı hattı **hızlı** oku |
| 100–500 ms’de bir log | Sürekli örnek stream |
| Terminalde sayı | Python’da **zaman–genlik grafiği** |
| “Ses var / yok” hissi | **1 kHz sinüs** ile dalga doğrulama |

Dün zincir:

```
MIC → ADC → UART satırı
```

Bugün zincir:

```
1 kHz ton → MIC → ADC (sık örnek) → UART stream → Python plot
```

---

## 2. Neden grafik?

Tek satır:

```
MIC = 2200
```

Bu, o **anlık** örnektir. Sinüs dalgası zamanla `sin(2π·1000·t)` şeklinde salınır; tek nokta şekli göstermez.

Birçok noktayı sırayla çizersen:

```
genlik
  ^     /\      /\
  |    /  \    /  \
  |---/----\--/----\--→ zaman
           \/
```

ortaya çıkar. Bu, osiloskobun basit hali.

---

## 3. Örnekleme ve 1 kHz

### Nyquist (kısa)

Sinyal frekansı \(f\), örnekleme \(f_s\):

\[
f_s > 2f
\]

1 kHz için teorik minimum \(f_s > 2000\) Hz.

### Pratikte

| \(f_s\) | 1 kHz grafikte |
|---------|----------------|
| ~1 kHz | Bozuk / yanlış görünür (alias) |
| ~2–3 kHz | Tanınır ama köşeli |
| ~8–10 kHz+ | Daha düzgün sinüs |

Bugünkü kabul: telefonda 1 kHz çalınca **periyodik, sinüs benzeri** bir şey görmek.

### Bias hatırlatması

Sessizken çizgi ~2048 (örnek) civarındadır; sinüs bu orta çizginin üstünde/altında salınır. Sıfırda görmeyi beklersen şaşırırsın — bu normal.

---

## 4. UART formatı

Python’un işi kolay olsun diye **her satır = bir örnek**:

```
2048
2101
2155
...
```

veya:

```
MIC=2048
```

Kurallar:

- Baud rate MCU ↔ PC aynı (ör. 115200)  
- Satır sonu `\n`  
- Araya debug metni karıştırma (parse bozulur)  

Baud düşük + örnek çok hızlı → buffer taşar, grafik “takılır” veya atlar. Gerekirse örnek hızını düşür veya formatı kısalt.

---

## 5. Python tarafı (özet)

Kullanılan kütüphaneler:

| Paket | İş |
|-------|-----|
| `pyserial` | COM porttan satır oku |
| `matplotlib` | Canlı çizim |

Akış:

```
COM aç → satır oku → int parse → ring buffer’a ekle → grafiği güncelle
```

Örnek komutlar:

```bash
pip install -r requirements.txt
python mic_plot.py --simulate          # sahte 1 kHz
python mic_plot.py --port COM5         # gerçek kart
```

`--simulate` modu, kart hazır değilken script’in doğru çalıştığını gösterir: **tam 1 kHz sinüs** üretir.

---

## 6. 1 kHz test prosedürü

1. Firmware stream’i çalışıyor, Python bağlı.  
2. Sessiz baseline’ı kaydet (düz band).  
3. Telefonda 1000 Hz sinüs aç.  
4. Mikrofon yakınına getir.  
5. Grafikte düzenli salınım gör → ekran görüntüsü al.  
6. Tonu kes → tekrar sakin band.

Başarısız olursa checklist:

- [ ] COM port doğru mu?  
- [ ] Baud aynı mı?  
- [ ] Satırlar gerçekten sayı mı? (başka log var mı?)  
- [ ] Örnekleme çok yavaş mı?  
- [ ] Mikrofon doğru kanal mı? (dün doğrulandı mı?)

---

## 7. Mentöre anlatabileceğin 30 sn özet

> “Dün mikrofonu ADC ile okuduk. Bugün örnekleri UART’tan sürekli gönderip Python’da çiziyoruz. Telefonda 1 kHz sinüs çalınca grafikte bias etrafında periyodik dalga görüyoruz; bu da hattın sadece ‘sayı basmak’ değil, zaman domeninde sesi taşıdığını gösteriyor.”

---

## 8. Sonraki adım

1. Bu notu bitir.  
2. [`kaynaklar/mic_plot.py`](kaynaklar/mic_plot.py) → `--simulate`.  
3. Firmware stream’i ayarla.  
4. [`02_Gorevler.md`](02_Gorevler.md) checklist + teorik sorular.
