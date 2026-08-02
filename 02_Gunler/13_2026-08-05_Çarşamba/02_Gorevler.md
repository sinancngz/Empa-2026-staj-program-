# Gün 13 — Görevler (LIS2DE12 X Y Z)

Anlatım: [`01_Anlatim.md`](01_Anlatim.md)

**Ana hedef:** İvmeölçerden X, Y, Z verisini almak.  
Yan görevler zorunlu ama kısa; teori cevapları raporda.

---

## Ortak hazırlık

- [ ] I2C bus çalışıyor (Pazartesi scanner)  
- [ ] LIS2DE12 bağlı; scanner’da `0x18` veya `0x19`  
- [ ] UART debug açık  
- [ ] Datasheet / anlatım elinde  

---

## Ana görev — X Y Z oku

### İstenenler

1. `WHO_AM_I` oku → `0x33` doğrula, UART’a yaz.  
2. CTRL register ile sensörü ölçüme aç (ODR + X/Y/Z enable).  
3. `OUT_X`, `OUT_Y`, `OUT_Z` oku (**signed**).  
4. Değerleri periyodik UART log’unda bas (~5–10 Hz veya 100–200 ms).  
5. Kartı eğerek / sallayarak değerlerin **canlı değiştiğini** göster.

### Örnek çıktı

```
WHO_AM_I = 0x33
X=2   Y=-1   Z=64
X=3   Y=0    Z=63
X=40  Y=-2   Z=48
```

### Yapılacaklar

| # | Madde | Yapıldı |
|---|-------|---------|
| 1 | WHO_AM_I = `0x33` | ☐ |
| 2 | CTRL init (ODR + eksenler) | ☐ |
| 3 | X Y Z UART’ta | ☐ |
| 4 | `int8_t` / işaret doğru | ☐ |
| 5 | Eğince / sallayınca değişim (mentör demosu) | ☐ |

### Kabul

- [ ] Kimlik doğru  
- [ ] Düz dururken bir eksen diğerlerinden belirgin (yerçekimi)  
- [ ] Hareket → log değişiyor  
- [ ] Sabit sahte / hep sıfır yok  

---

## Yan görev 1 — Dominant eksen (orientation)

Anlık olarak **mutlak değeri en büyük** ekseni bul; UART’ta yön etiketle.

Örnek:

```
X=2   Y=-1   Z=64    |  UP (Z)
X=55  Y=3    Z=10    |  +X
```

İpucu: `|x|`, `|y|`, `|z|` karşılaştır; eşikte küçük gürültüyü yut (ör. |a| < 10 ise STILL).

| # | Madde | Yapıldı |
|---|-------|---------|
| 1 | Dominant eksen etiketi log’da | ☐ |
| 2 | Kartı çevirince etiket değişiyor | ☐ |

---

## Yan görev 2 — Basit hareket / sarsıntı

Durgun ortalama veya önceki örnekle fark al. Eşik aşılınca:

```
SHAKE
```

veya LED yak. Kısa **cooldown** ekle (sürekli spam olmasın).

| # | Madde | Yapıldı |
|---|-------|---------|
| 1 | Hareket / shake algısı çalışıyor | ☐ |
| 2 | Cooldown veya debounce var | ☐ |

---

## Teorik Sorular (Cevapları rapora yaz)

**1.** İvmeölçer ne ölçer? Kart düz ve sabitken neden bir eksen ≈ ±1 g civarında görünür?


**2.** LIS2DE12’nin tipik 7-bit I2C adresleri nelerdir? SA0 / SDO neden iki adres üretir?


**3.** `WHO_AM_I` register’ı ne işe yarar? Beklenen değer nedir?


**4.** Power-up sonrası sadece `OUT_X` okumak neden çoğu zaman yetmez? CTRL / ODR’nin rolü nedir?


**5.** `OUT_*` değerini `uint8_t` yerine `int8_t` olarak yorumlamak neden önemli?


**6.** Full-scale ±2 g ile ±16 g arasında pratikte ne fark eder?


**7.** Aynı I2C bus’ta SHT40 (`0x44`) ve LIS2DE12 (`0x18`) birlikte durabilir mi? Neden?


**8.** STATUS register’daki “data ready” biti olmasa sürekli okursan ne olur? (kısa düşün)


---

## Bonus (isteğe bağlı)

| # | Bonus | Yapıldı |
|---|-------|---------|
| 1 | Ham değeri mg veya g’ye çevir (datasheet sensitivity) | ☐ |
| 2 | `|a| = sqrt(x²+y²+z²)` büyüklüğünü logla | ☐ |

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/
│   └── gunluk_rapor.md    # teori + gözlem (düz / eğik örnek satırlar)
└── proje/
    └── (LIS2DE12 XYZ firmware)
```
