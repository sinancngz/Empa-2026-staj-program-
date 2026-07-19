# GPIO Anlatımı

**Gün 01 · Tiremo Cortex · ABOV A34G43x**

Bu not, mentörün tahtada / ekranda anlatırken kullanacağı iskelettir. Amaç: pin’in ne işe yaradığını, LED ve butonun nasıl kontrol edildiğini netleştirmek.

---

## 1. GPIO nedir?

Mikrodenetleyicinin ayaklarına (pin) **GPIO** denir: *General Purpose Input/Output* — genel amaçlı giriş/çıkış.

Her pin’i yazılımla iki temel moddan birine alırsın:

| Mod | Pin ne yapar? | Günlük hayattan örnek |
|-----|----------------|------------------------|
| **Output (çıkış)** | MCU pin’e 0 veya 1 **yazar** | LED yak / söndür |
| **Input (giriş)** | MCU pin’deki 0 veya 1’i **okur** | Butona basıldı mı? |

Önemli kural: Pin’i kullanmadan önce yönünü ayarla — çıkış mı, giriş mi? Yanlış yönde kullanırsan LED yanmaz veya buton okunmaz.

Tiremo Cortex’te bugün kullandığımız iki şey:

- **LED’ler** → çıkış (MCU sürer)
- **Kullanıcı butonu** → giriş (MCU okur)

---

## 2. Output — LED nasıl yanar?

### Adımlar

1. İlgili pin’i **output** yap  
2. Pin’e **HIGH (1)** veya **LOW (0)** yaz  
3. LED yanar veya söner  

### Active-high ve active-low

Kart şemasına göre LED’in polaritesi değişir:

| Tip | Pin HIGH iken | Pin LOW iken |
|-----|---------------|--------------|
| **Active-high** | LED **yanar** | LED söner |
| **Active-low** | LED söner | LED **yanar** |

Tiremo Cortex’te kullanıcı LED’leri çoğu zaman **active-low** olur: yani LED’i yakmak için pin’e **0** yazarsın. Bu yüzden “1 yazdım, neden yanmıyor?” diye şaşırma — önce polariteyi kontrol et.

### İlk pratik sıra

1. Tek LED’i sabit yak  
2. Aynı LED’i söndür  
3. Yanıp söndür (**blink**) — araya kısa bekleme (`delay`) koy  

Blink için bugün basit gecikme yeter. İleride aynı işi timer ile daha temiz yapacağız.

---

## 3. Input — Buton nasıl okunur?

### Adımlar

1. Pin’i **input** yap  
2. Pin değerini oku (`0` veya `1`)  
3. “Basılı” / “bırakılmış” kararını ver  

Buton aslında pin’i ya **GND**’ye ya da **VCC**’ye bağlayan bir anahtardır. Anahtar açıkken pin’in ne okuyacağı net olmalı — yoksa pin “havada” kalır.

---

## 4. Pull-up ve pull-down neden var?

Giriş pin’i hiçbir yere bağlı değilse gerilim **belirsiz**dir. Buna **floating (yüzen) pin** denir. Okuduğunda bazen 0, bazen 1 görürsün; kod rastgele davranır.

Çözüm: pin’i bilinen bir seviyeye **hafifçe çekmek** — pull direnci.

### Pull-up (yukarı çekme)

```
   VCC (3.3V)
    |
   [R]   ← pull-up direnci
    |
   PIN -------- BUTON -------- GND
```

| Buton durumu | Pin yaklaşık değeri |
|--------------|---------------------|
| Açık (basılmamış) | HIGH (1) |
| Basılı | LOW (0) — GND’ye kısa |

Bu düzen çok yaygındır. Yazılımda “basıldı” = pin **0** okundu diye düşünürsün (**active-low buton**).

### Pull-down (aşağı çekme)

```
   VCC -------- BUTON -------- PIN
                                |
                               [R]  ← pull-down
                                |
                               GND
```

| Buton durumu | Pin yaklaşık değeri |
|--------------|---------------------|
| Açık | LOW (0) |
| Basılı | HIGH (1) |

### Dahili vs harici

| Tür | Nerede? |
|-----|---------|
| **Dahili pull** | MCU içinde; kodda açılır (`pull-up enable` vb.) |
| **Harici pull** | Kart üzerinde fiziksel direnç |

Tiremo Cortex kullanıcı butonu için örnek koda / kart dokümanına bak: dahili pull-up var mı, basınca 0 mı 1 mi geliyor?

---

## 5. Debounce (kısa not)

Mekanik butona basınca kontak birkaç milisaniye zıplayabilir. Aynı basışta 0–1–0–1 görürsün; toggle yanlışlıkla iki kez çalışır.

Bugün için yeterli çözümler:

- Kısa bir yazılım gecikmesi  
- Ardışık birkaç okuma aynıysa “gerçek basış” say  

İleride timer ile daha düzgün debounce yapılacak.

---

## 6. Anlatım sonrası

Anlatım bitince kendi projenle görevlere geç: kolay → orta → zor.

| Seviye | Ne yapacaksın | Ne öğreniyorsun |
|--------|----------------|-----------------|
| **Kolay** | LED yak / söndür / blink | Output pin kontrolü |
| **Orta** | Buton oku → LED kontrol / toggle | Input + output birlikte |
| **Zor** | 3+ LED kayan ışık; butonla yön veya hız; kısa self-test | Birden fazla pin + basit sayaç |

Görev listesi: [`02_Gorevler.md`](02_Gorevler.md)
