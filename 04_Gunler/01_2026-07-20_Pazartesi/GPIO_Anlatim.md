# GPIO Anlatımı — Output, Input, LED, Buton, Pull-up / Pull-down

**Gün 01 · Tiremo Cortex · ABOV A34G43x**

---

## GPIO nedir?

**GPIO (General Purpose Input/Output)** — mikrodenetleyicinin pinlerini yazılımla **çıkış** veya **giriş** olarak kullanmanı sağlar.

| Mod | MCU ne yapar? | Örnek |
|-----|----------------|-------|
| **Output** | Pin’e 0 veya 1 yazar | LED yak / söndür |
| **Input** | Pin’deki seviyeyi okur | Buton basılı mı? |

Pin önce doğru **yöne** (direction) ayarlanmalı: çıkış mı, giriş mi?

---

## Output — LED sürme

### Mantık

1. Pin’i **output** yap  
2. HIGH veya LOW yaz  
3. LED yanar veya söner  

### Active-high vs active-low

| Tip | Pin HIGH | Pin LOW |
|-----|----------|---------|
| **Active-high** | LED yanar | LED söner |
| **Active-low** | LED söner | LED yanar |

Tiremo Cortex’te birçok kullanıcı LED’i **active-low** olabilir. Kart şemasına / örneğe bakmadan “HIGH = yanar” varsayma.

### Pratik ipuçları

- İlk test: tek LED, sabit yak → sabit söndür → blink  
- Blink için başta basit gecikme (`delay`) kabul; sonra timer’a geçilecek  
- Birden fazla LED varsa pin map’i not et  

---

## Input — Buton okuma

### Mantık

1. Pin’i **input** yap  
2. Pin değerini oku (0 / 1)  
3. Basılı / bırakılmış kararını ver  

### Buton nasıl bağlanır?

Buton, pin’i ya **GND**’ye ya da **VCC**’ye çeker. Diğer durumda pin “havada” kalmamalı → **pull** gerekir.

---

## Pull-up ve Pull-down

Pin girişken ve bağlı değilse gerilim **belirsiz** olur (floating). Rastgele 0/1 okunur. Bunu önlemek için pin’i bilinen bir seviyeye çekeriz.

### Pull-up

```
   VCC
    |
   [R]  ← pull-up direnci (dahili veya harici)
    |
   PIN ---- BUTON ---- GND
```

- Buton **açık:** pin ≈ HIGH  
- Buton **basılı:** pin ≈ LOW (GND’ye kısa)

Çok kullanılan düzen: **active-low buton** (basınca 0 okunur).

### Pull-down

```
   VCC ---- BUTON ---- PIN
                        |
                       [R]  ← pull-down
                        |
                       GND
```

- Buton **açık:** pin ≈ LOW  
- Buton **basılı:** pin ≈ HIGH  

### Dahili vs harici

| | |
|---|---|
| **Dahili pull** | MCU içinde; yazılımla açılır (`pull-up enable` vb.) |
| **Harici pull** | Kart üzerinde direnç; şemaya bak |

Tiremo Cortex kullanıcı butonu için kart dokümanına / örnek koda bak: dahili pull-up kullanılıyor mu, polarite ne?

---

## Debounce (kısa not)

Butona basınca mekanik kontak birkaç kez zıplar → kısa süre içinde 0–1–0–1 görülebilir.

Bugün için:

- Basit yazılım gecikmesi veya  
- “Birkaç okuma aynıysa kabul et”  

İleride timer ile daha düzgün debounce yapılacak.

---

## Bugün ne bekliyoruz?

| Seviye | Ne yapacaksın |
|--------|----------------|
| **Kolay** | LED yak-söndür / blink |
| **Orta** | Buton oku → LED kontrol |
| **Zor** | Birden fazla LED + butonla pattern |

Görev listesi: [`02_Gorevler.md`](02_Gorevler.md)

---

## Kontrol soruları (anlatım sonrası)

1. Output ile input farkı nedir?  
2. Active-low LED’de pin LOW iken ne olur?  
3. Pull-up neden gerekir?  
4. Floating pin ne demek?  
