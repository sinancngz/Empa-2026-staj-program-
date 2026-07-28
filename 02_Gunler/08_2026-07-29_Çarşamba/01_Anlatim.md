# Bit İşlemleri Eğitimi

## 1. Giriş

Gömülü sistemlerde mikrodenetleyiciler (MCU) donanım kaynaklarını yönetmek için register adı verilen özel bellek alanlarını kullanır.

Register içerisindeki her bit farklı bir donanım ayarını temsil edebilir.

Örneğin bir GPIO register:

```
Bit7 Bit6 Bit5 Bit4 Bit3 Bit2 Bit1 Bit0

 0    0    1    0    0    0    0    1
```

Burada:

- Bit0 → Bir özellik aktif
- Bit5 → Başka bir özellik aktif

olabilir.

Bu yüzden gömülü yazılımda tek tek bitleri kontrol etmek çok önemlidir.

---

# 2. Sayı Sistemleri

## Decimal

Günlük hayatta kullandığımız sayı sistemi:

```
0 1 2 3 4 5 6 7 8 9
```

---

## Binary (İkilik Sistem)

Bilgisayarların kullandığı sayı sistemidir.

Sadece iki değer vardır:

```
0
1
```

Örnek:

```
Decimal: 5

Binary:

00000101
```

---

## Hexadecimal (16'lık Sistem)

Binary değerleri daha okunabilir yazmak için kullanılır.

Karakterler:

```
0-9
A-F
```

Örnek:

```
Binary:

11111111


Hex:

0xFF
```

---

# 3. Bit Kavramı

Bir bit iki farklı değer alabilir:

```
0 -> LOW
1 -> HIGH
```

8 bit:

```
Bit7 Bit6 Bit5 Bit4 Bit3 Bit2 Bit1 Bit0

 0    0    0    0    0    0    0    0
```

Bir byte toplam 8 bitten oluşur.

---

# 4. Bit Operatörleri

C dilinde kullanılan temel bit operatörleri:

| Operatör | Anlamı |
|---|---|
| & | AND |
| \| | OR |
| ^ | XOR |
| ~ | NOT |
| << | Left Shift |
| >> | Right Shift |

---

# 5. AND Operatörü (&)

İki bit de 1 ise sonuç 1 olur.

```
  1010
& 1100
------
  1000
```

Kullanım:

- Bit kontrol etmek
- Belirli bitleri okumak

Örnek:

```c
if(register & (1 << 3))
{
    // Bit3 aktif
}
```

---

# 6. OR Operatörü (|)

Bitlerden biri 1 ise sonuç 1 olur.

```
  1010
| 0100
------
  1110
```

Kullanım:

- Bit açmak (SET)

---

# 7. XOR Operatörü (^)

Bitler farklı ise sonuç 1 olur.

```
  1010
^ 1100
------
  0110
```

Kullanım:

- Toggle işlemleri

---

# 8. NOT Operatörü (~)

Bitleri tersine çevirir.

```
00001111

~

11110000
```

Genellikle bit temizleme işlemlerinde kullanılır.

---

# 9. Shift İşlemleri

## Left Shift (<<)

Bitleri sola kaydırır.

Örnek:

```c
1 << 3
```

Sonuç:

```
00000001

00001000
```

Yani:

```
1 << 3 = 8
```

---

## Right Shift (>>)

Bitleri sağa kaydırır.

Örnek:

```c
8 >> 2
```

Sonuç:

```
00001000

00000010
```

---

# 10. Bit Maskeleme

Belirli bir biti değiştirmek için maske kullanılır.

Örnek:

3. biti açmak:

Maske:

```
00001000
```

Kod:

```c
reg |= (1 << 3);
```

Sonuç:

```
00000000

OR

00001000

=

00001000
```

---

# 11. Bit SET İşlemi

Bir biti 1 yapmak.

Örnek:

```c
reg |= (1 << bit);
```

Örnek:

```c
reg |= (1 << 5);
```

Bit5 aktif edilir.

---

# 12. Bit CLEAR İşlemi

Bir biti 0 yapmak.

Örnek:

```c
reg &= ~(1 << bit);
```

Önce maske ters çevrilir:

```
00001000

~

11110111
```

Sonrasında AND yapılır.

---

# 13. Bit TOGGLE İşlemi

Bir biti tersine çevirmek.

```c
reg ^= (1 << bit);
```

Örnek:

```
0 -> 1

1 -> 0
```

LED kontrolünde sık kullanılır.

---

# 14. Bit READ İşlemi

Bir bitin durumunu okumak:

```c
if(reg & (1 << bit))
{
    // Bit 1
}
else
{
    // Bit 0
}
```

---

# 15. Register Örneği

Bir GPIO register düşünelim:

```
GPIO_ODR

Bit5 -> LED
```

LED'i yakmak:

```c
GPIO_ODR |= (1 << 5);
```

LED'i söndürmek:

```c
GPIO_ODR &= ~(1 << 5);
```

LED durumunu değiştirmek:

```c
GPIO_ODR ^= (1 << 5);
```

---

# 16. Bit Field Kavramı

Bazı registerlarda birden fazla bit beraber kullanılır.

Örnek:

```
CONTROL REGISTER


Bit7 Bit6 Bit5 Bit4 Bit3 Bit2 Bit1 Bit0

              MODE
```

MODE alanı:

```
00 -> Idle
01 -> RX
10 -> TX
11 -> ERROR
```

Kod:

```c
#define MODE_MASK 0x30

reg &= ~MODE_MASK;

reg |= (2 << 4);
```

---

# 17. Bit Macro Kullanımı

Daha okunabilir kod için:

```c
#define BIT(x) (1U << x)
```

Kullanım:

```c
GPIOA->ODR |= BIT(5);
```

---

# 18. Volatile Kullanımı

Donanım veya interrupt tarafından değiştirilen değişkenlerde kullanılır.

Örnek:

```c
volatile uint8_t button_flag;
```

Sebebi:

Compiler değişkeni optimize edip RAM okumasını engellememelidir.

---

# 19. Bit İşlemleri Nerelerde Kullanılır?

| Alan | Kullanım |
|-|-|
| GPIO | Pin kontrolü |
| UART | Status register |
| SPI | Konfigürasyon |
| I2C | Flag kontrolü |
| Timer | Ayarlar |
| ADC | Çözünürlük ayarı |
| Interrupt | Enable register |
| CAN | Frame ayarları |
| BLE | Feature flag |

---

# 20. Uygulama Örnekleri

## Örnek 1

Bir register üzerinde:

- Bit0 aç
- Bit3 aç
- Bit0 kapat
- Bit5 toggle yap


Çözüm:

```c
uint8_t reg = 0;

reg |= (1 << 0);

reg |= (1 << 3);

reg &= ~(1 << 0);

reg ^= (1 << 5);
```

---

## Örnek 2

GPIO fonksiyonları yazınız:

```c
void GPIO_Set(uint8_t pin);

void GPIO_Clear(uint8_t pin);

uint8_t GPIO_Read(uint8_t pin);
```

---

# Özet

Gömülü yazılımda bit işlemleri:

- Register kontrolü
- Donanım yönetimi
- GPIO işlemleri
- Haberleşme protokolleri
- Düşük güç uygulamaları

için temel bir konudur.

İyi bir embedded developer register seviyesinde düşünebilmelidir.

