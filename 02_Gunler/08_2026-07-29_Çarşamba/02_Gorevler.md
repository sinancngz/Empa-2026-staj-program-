# Gün 08 — Görevler (Bit İşlemleri ve Register Kontrolü)

Anlatım: [`01_Anlatim.md`](01_Anlatim.md)

---

## Görev

Bit işlemlerini kullanarak bir register üzerinde belirli bitleri kontrol et.

Amaç:

- Binary ve hexadecimal mantığını anlamak
- Bit açma (SET)
- Bit kapatma (CLEAR)
- Bit değiştirme (TOGGLE)
- Bit okuma (READ)
- Maskeleme mantığını öğrenmek

Gerçek donanım register mantığını simüle eden bir uygulama hazırlanacaktır.

---

## Görev Senaryosu

Aşağıdaki 8 bitlik bir kontrol register'ımız olduğunu düşünelim:

```c
uint8_t control_register = 0x00;
```

Register yapısı:

```
Bit7 Bit6 Bit5 Bit4 Bit3 Bit2 Bit1 Bit0

 |    |    |    |    |    |    |    |
 |    |    |    |    |    |    |---- ENABLE
 |    |    |    |    |    |--------- ERROR
 |    |    |    |    |-------------- MODE0
 |    |    |    |------------------- MODE1
 |    |    |------------------------ DATA_READY
 |    |----------------------------- RESERVED
 |---------------------------------- RESERVED
```

Aşağıdaki işlemler yapılacaktır:

1. ENABLE bitini aktif et
2. ERROR bitini temizle
3. MODE bitlerini kullanarak çalışma modunu değiştir
4. DATA_READY bitini toggle et
5. Register'ın güncel durumunu terminale hexadecimal olarak yazdır

---

## Yapılacaklar

| # | Madde | Yapıldı |
|---|-------|---------|
| 1 | Binary, decimal ve hexadecimal sayı sistemlerini incele | ☐ |
| 2 | Bit SET işlemini uygula | ☐ |
| 3 | Bit CLEAR işlemini uygula | ☐ |
| 4 | Bit TOGGLE işlemini uygula | ☐ |
| 5 | Bit READ işlemi ile durum kontrolü yap | ☐ |
| 6 | Maskeleme kullanarak birden fazla biti değiştir | ☐ |
| 7 | İşlemlerin sonucunu terminalde göster | ☐ |
| 8 | Teorik soruları rapora cevapla | ☐ |

---

## Beklenen Çıktı

Terminal örneği:

```
Initial Register = 0x00

ENABLE SET
Register = 0x01

MODE = TX
Register = 0x09

DATA_READY TOGGLE
Register = 0x19
```

---

# Teknik Gereksinimler

## Kullanılması gereken işlemler

### Bit SET

Bir biti 1 yapmak için:

```c
reg |= (1 << bit);
```


---

### Bit CLEAR

Bir biti 0 yapmak için:

```c
reg &= ~(1 << bit);
```


---

### Bit TOGGLE

Bir biti terslemek için:

```c
reg ^= (1 << bit);
```


---

### Bit READ

Bir biti kontrol etmek için:

```c
if(reg & (1 << bit))
{
    // Bit aktif
}
```

---

# Bonus Görev

Aşağıdaki fonksiyonları yazınız:

```c
void bit_set(uint8_t *reg, uint8_t bit);

void bit_clear(uint8_t *reg, uint8_t bit);

void bit_toggle(uint8_t *reg, uint8_t bit);

uint8_t bit_read(uint8_t reg, uint8_t bit);
```

Örnek kullanım:

```c
uint8_t status = 0;

bit_set(&status, 3);

bit_toggle(&status, 1);

if(bit_read(status,3))
{
    printf("Bit aktif");
}
```

---

# Teorik Sorular (Cevapları rapora yaz)

**1.** Bit nedir? Byte ile arasındaki fark nedir?


**2.** Binary sayı sistemi neden mikrodenetleyicilerde önemlidir?


**3.** Aşağıdaki işlemin sonucu nedir?

```c
uint8_t value = 0x00;

value |= (1 << 3);
```

Sonucu hexadecimal ve binary olarak göster.


**4.** Aşağıdaki kod ne yapar?

```c
value &= ~(1 << 5);
```


**5.** Aşağıdaki işlemin sonucu nedir?

```c
uint8_t value = 0x08;

value ^= (1 << 3);
```

Açıklayınız.


**6.** Maskeleme (bit masking) nedir? Neden kullanılır?


**7.** Bir register içerisindeki sadece 4. biti değiştirmek istiyorsunuz. Diğer bitlerin değişmemesi için hangi yöntem kullanılır?


**8.** Aşağıdaki değerin decimal karşılığını bulun:

```
0b10101010
```


**9.** STM32 gibi mikrodenetleyicilerde GPIO kontrolünde neden bit işlemleri kullanılır?


**10.** Aşağıdaki kodun amacı nedir?

```c
#define LED_PIN 5

GPIOA->ODR |= (1 << LED_PIN);
```

Açıklayınız.

---

# Kabul

Mentöre gösterirken:

- Register değerleri doğru değişmeli
- SET / CLEAR / TOGGLE işlemleri çalışmalı
- Terminal çıktısında register durumu hexadecimal görünmeli
- Kod içerisinde bit mask kullanımı bulunmalı

---

# Teslim

```
teslimler/Stajyer_X/

├── rapor/
│   └── gunluk_rapor.md
└── proje/
```