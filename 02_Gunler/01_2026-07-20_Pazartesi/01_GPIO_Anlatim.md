# GPIO — Giriş / Çıkış, LED ve Buton

Tiremo Cortex · ABOV A34G43x

Bu notu okuyarak pin’in ne işe yaradığını, LED ve butonun nasıl kontrol edildiğini öğreneceksin. Sonra [`02_Gorevler.md`](02_Gorevler.md) ile uygula.

### Bu notu nasıl kullanmalısın?

1. Önce **§1–4** oku (GPIO, LED, buton, pull) — kart şemasıyla eşleştir.  
2. Bilgisayarda örnek projeyi aç; `Gpio_Init`, `Gpio_Write`, `Gpio_Read` benzeri fonksiyonları bul.  
3. [`02_Gorevler.md`](02_Gorevler.md) **kolay** görevle başla: tek LED yak → söndür → blink.  
4. **Orta** görevde buton okumayı ekle; basınca 0 mı 1 mi geldiğini not et.

### Gün sonu hedefleri

- Bir pini **çıkış** yapıp LED’i yakıp söndürebilmek.  
- Bir pini **giriş** yapıp butonun basılı/bırakılmış olduğunu okuyabilmek.  
- **Pull-up** ile “basılı = 0” mantığını açıklayabilmek.  
- `while(1)` içinde blink veya buton kontrolü yazabilmek.

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

### Yazılımda tipik sıra (çıkış)

Donanım sürücüsü projeye göre değişir; mantık hep aynıdır:

1. **Init:** Pin modu = çıkış, gerekirse hız / varsayılan seviye.  
2. **Yaz:** `Gpio_Write(LED_PIN, 1)` veya `0` (active-low ise “yan” için 0).  
3. **Blink:** Yan → `DelayMs(300)` → söndür → `DelayMs(300)` → tekrar — hepsi `while(1)` içinde.

```c
while (1) {
    Gpio_Write(LED1, 0);   /* örnek: active-low, 0 = yan */
    DelayMs(400);
    Gpio_Write(LED1, 1);   /* söndür */
    DelayMs(400);
}
```

LED yanmıyorsa önce **polarite** (active-high/low), sonra **doğru pin** ve **init çağrıldı mı** kontrol et.

---

## 3. Input — Buton nasıl okunur?

### Adımlar

1. Pin’i **input** yap  
2. Pin değerini oku (`0` veya `1`)  
3. “Basılı” / “bırakılmış” kararını ver  

Buton aslında pin’i ya **GND**’ye ya da **VCC**’ye bağlayan bir anahtardır. Anahtar açıkken pin’in ne okuyacağı net olmalı — yoksa pin “havada” kalır.

### Yazılımda tipik sıra (giriş)

```c
Gpio_Init();   /* buton pini: input + pull-up açık (kartına göre) */

while (1) {
    if (Gpio_Read(BTN) == 0) {   /* pull-up: basılı = 0 */
        Gpio_Write(LED1, 0);     /* LED yak (active-low örnek) */
    } else {
        Gpio_Write(LED1, 1);
    }
}
```

**Polling:** Butonu her döngü turunda okursun. Basit ve bugün için yeterli. Çarşamba günü aynı butonu **kesme** ile de okuyacaksın; GPIO giriş ayarı yine aynı kalır.

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

Mekanik butona basınca kontak birkaç milisaniye **zıplayabilir** (bounce). Aynı fiziksel basışta yazılım şunu görebilir:

```
1 → 0 → 1 → 0 → 0   (milisaniyeler içinde)
```

`if` içinde her 0–1 geçişinde LED toggle yazdıysan, **tek basışta iki kez** toggle olur.

Bugün için yeterli çözümler:

- Basıştan sonra **kısa gecikme** (öğrenme amaçlı; chase’i yavaşlatır).  
- **Ardışık okumalar** aynı değeri gösterene kadar bekle — Salı günü bunu `uint32_t` ve tick ile düzgün yapacaksın.

GPIO gününde buton “garip” davranıyorsa debounce’u Salı’ya bırakıp önce **doğru pull ve okuma** ile devam etmek de olur.

---

## 6. Sık hatalar (ilk gün)

| Belirti | Olası neden | Ne yap? |
|---------|-------------|---------|
| LED hiç yanmıyor | Yanlış pin veya active-low | 0/1 ters dene; şemaya bak |
| Buton rastgele | Floating pin, pull kapalı | Pull-up aç |
| Toggle çift çalışıyor | Bounce | Salı debounce veya kısa bekleme |
| Program “duruyor” | `main` sonunda döngü yok | `while(1)` ekle |

---

## 7. Bundan sonra

Bu konuyu bitirince kendi projenle görevlere geç: kolay → orta → zor.

| Seviye | Ne yapacaksın | Ne öğreniyorsun |
|--------|----------------|-----------------|
| **Kolay** | LED yak / söndür / blink | Output pin kontrolü |
| **Orta** | Buton oku → LED kontrol / toggle | Input + output birlikte |
| **Zor** | 3+ LED kayan ışık; butonla yön veya hız; kısa self-test | Birden fazla pin + basit sayaç |

Görev listesi: [`02_Gorevler.md`](02_Gorevler.md)
