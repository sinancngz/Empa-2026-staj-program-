# Temel C ve Gömülü Programlama

Veri türleri, koşullar ve döngüler (kart kodunda)

Bu notu okuyarak Pazartesi–Çarşamba’da yazdığın kodların arkasındaki **C dilini** netleştireceksin. Amaç: sadece “çalışan örnek” değil, `if`, `while`, `for` ve veri türlerinin **neden** kullanıldığını görmek.

Önceki günler: GPIO → MCU / bellek → kesme. Bugün aynı konuları **C sözdizimi** ile okuyacaksın. Sonra [`02_Gorevler.md`](02_Gorevler.md) ile bol uygulama.

### Bu notu nasıl kullanmalısın?

1. **Sabah (yaklaşık 1 saat):** Aşağıdaki bölümleri sırayla oku; her bölümdeki kısa kod örneklerini not al.  
2. **Öğleden sonra:** Bilgisayarda [`02_Gorevler.md`](02_Gorevler.md) kolay görevden başla; takılırsan ilgili bölüme geri dön (ör. chase için “4. for”).  
3. **Kartta test:** Her `if` / `for` değişikliğinden sonra derle-yükle; büyük kodu tek seferde yazma.

### Öğrenme hedefleri (gün sonu)

- Bir değişkenin **türünü** seçebilmek (`bool`, `uint32_t`, `const`).  
- Buton ve LED kararını **`if` / `else`** ile yazabilmek.  
- Gömülü programın **`while(1)`** ile neden bitmediğini açıklayabilmek.  
- Birden fazla LED’i **`for`** ile dönebilmek.  
- Kesme kullanıyorsan **`volatile`** neden gerekli, bir cümleyle söyleyebilmek.

---

## Haftanın kodunda C nerede?

Daha önce kartta “LED yandı”, “buton okundu” dedin; bugün aynı işlerin **program dilindeki karşılığını** görüyorsun.

| Gün | Kartta ne yaptın? | C tarafında ne kullandın? |
|-----|-------------------|---------------------------|
| Pazartesi | LED yak/söndür, buton oku | `if`, değişken, `while(1)` |
| Salı | Debounce, kısa/uzun basış | `uint32_t`, `const`, karşılaştırma, state |
| Çarşamba | Kesme + flag | `volatile bool`, `if` flag kontrolü |

### Gömülü programın iskeleti

Neredeyse her kart projesi şu yapıdadır:

```c
int main(void)
{
    System_Init();   /* saat, temel ayar */
    Gpio_Init();     /* LED çıkış, buton giriş */

    while (1)       /* program buradan çıkmaz */
    {
        /* 1) Oku: buton, sensör, flag */
        /* 2) Karar ver: if / switch */
        /* 3) Yaz: LED, motor, UART */
    }
}
```

**PC programı** ile fark: Masaüstünde `main` biter, işletim sistemi devralır. **MCU’da** `while(1)` olmazsa `main` sona erer ve kart “boş” kalır — LED söner, buton dinlenmez. Bu yüzden gömülüde sonsuz döngü **normaldir**, hata değildir.

---

## 1. Veri türleri (kartta en çok bunlar)

Değişken = bellekte (RAM) bir kutu. **Tür**, kutunun boyutu ve ne tür değer tutacağını söyler. Yanlış tür seçersen taşma, yanlış karşılaştırma veya gereksiz bellek kullanırsın.

### Tam sayılar

| Tür | Kabaca aralık | Gömülüde tipik kullanım |
|-----|---------------|-------------------------|
| `int` | İşaretli tam sayı | Genel sayaç (mimariye göre 32 bit) |
| `unsigned int` | 0 ve pozitif | Bazen bit mask |
| `uint8_t` | 0…255 | Pin dizisi indeksi, küçük buffer |
| `uint16_t` | 0…65535 | Bazı süre değerleri |
| `uint32_t` | Çok geniş | `GetTickMs()`, basış süresi, gecikme |

`stdint.h` ile `uint8_t` / `uint32_t` kullanmak iyi alışkanlıktır: “bu değişken 8 bit” dersin; farklı derleyicilerde `int` boyutu değişse bile `uint32_t` tutarlı kalır.

**Salı debounce örneği — satır satır:**

```c
uint32_t last_change_ms = 0;      /* RAM: son değişim anı, sürekli güncellenir */
const uint16_t DEBOUNCE_MS = 20;  /* Sabit: 20 ms eşiği, program boyunca değişmez */
```

- `last_change_ms` → her buton sıçramasında yeniden yazılır → **RAM**.  
- `DEBOUNCE_MS` → kod içinde hep 20 → **`const`** → genelde Flash’ta saklanır (Salı notundaki MCU bellek ayrımı).

### Mantıksal: `bool`

Sadece iki durum: doğru / yanlış.

```c
bool led_on = false;    /* LED şu an yanıyor mu? */
bool stable = false;    /* debounce sonrası stabil mi? */

if (led_on) {
    Gpio_Write(LED1, 1);   /* örnek: active-high */
} else {
    Gpio_Write(LED1, 0);
}
```

Kartta “basılı mı?”, “flag geldi mi?”, “mod hızlı mı?” gibi soruların cevabı çoğu zaman `bool` veya `0/1` karşılaştırmasıdır.

### `const` — değişmeyecek değer

Programcı “bunu çalışırken değiştirmeyeceğim” der.

```c
const uint32_t LONG_PRESS_MS = 1000;
const uint32_t BLINK_SLOW_MS = 500;
const uint32_t BLINK_FAST_MS = 200;

uint32_t now = GetTickMs();

if ((now - down_ms) >= LONG_PRESS_MS) {
    /* 1 saniyeden uzun basıldı */
}
```

**Neden `const`?**  
- Yanlışlıkla `LONG_PRESS_MS = 500` yazamazsın (derleyici uyarır).  
- Okuyan kişi “bu eşik sabit” diye anlar.  
- MCU’da çoğu zaman program belleğinde (Flash) durur.

### `volatile` — kesmede paylaşılan değişken

Normal değişken: sadece `main` okur/yazar.  
**Kesme:** ISR (kesme fonksiyonu) yazar, `main` okur — **aynı değişken, iki farklı zaman**.

```c
volatile bool button_flag = false;

void BTN_IRQHandler(void)
{
    button_flag = true;   /* kesme anında */
}

int main(void)
{
    while (1) {
        if (button_flag) {    /* normal döngüde */
            button_flag = false;
            /* LED toggle vb. */
        }
    }
}
```

**`volatile` olmazsa ne olur?**  
Derleyici optimizasyonu: “`button_flag` döngüde değişmiyor” sanıp register’da tutabilir veya okumayı kaldırabilir. ISR yazsa bile `main` **görmeyebilir**. Kesme kullanıyorsan paylaşılan flag’ler **mutlaka** `volatile` olmalı.

**Not:** `volatile` debounce yerine geçmez; sadece “bu değişken dışarıdan da değişir” der.

---

## 2. `if` / `else` — karar vermek

Programın “şu durumda şunu yap” kısmıdır. Kartta neredeyse her kullanıcı etkileşimi `if` ile işlenir.

### Tek dal — sadece koşul doğruysa

```c
if (Gpio_Read(BTN) == 0) {   /* active-low: basılı = 0 */
    Gpio_Write(LED1, 1);
}
```

Koşul yanlışsa bu blok **hiç çalışmaz**, program bir sonraki satıra geçer.

### İki dal — ya bu ya şu

```c
if (button_flag) {
    button_flag = false;
    led_on = !led_on;
} else {
    /* flag yok; chase veya blink devam */
}
```

### `else if` — birden fazla durum (Salı kısa/uzun)

```c
if (press_duration_ms < 1000) {
    Led_Toggle(LED1);           /* kısa basış */
} else if (press_duration_ms >= 1000) {
    Led_FlashAll();             /* uzun basış */
} else {
    /* süre henüz belli değil */
}
```

Sıra önemli: önce kısa koşul, sonra uzun. İlk doğru olan blok çalışır, geri kalanı atlanır.

### Karşılaştırma ve mantık

| Operatör | Anlam | Kart örneği |
|----------|--------|-------------|
| `==` | eşit mi | `if (raw == 0)` basılı |
| `!=` | farklı mı | `if (mode != MODE_PAUSE)` |
| `<` `>` `<=` `>=` | büyük/küçük | süre eşiği |
| `!` | değil | `if (!led_on)` |
| `&&` | ve | `if (flag && stable)` |
| `\|\|` | veya | `if (short \|\| long)` |

**Çok yapılan hata:** `if (x = 1)` → bu **atama**dır, karşılaştırma değil. `x` hep 1 olur ve `if` her zaman doğru sanılır. Karşılaştırma için **`==`** kullan.

### Active-low / active-high (GPIO ile bağlantı)

```c
/* Pull-up buton, basınca 0 */
if (Gpio_Read(BTN) == 0) {
    /* basılı */
}

/* Pull-down buton, basınca 1 */
if (Gpio_Read(BTN) == 1) {
    /* basılı */
}
```

`if` koşulunu yazmadan önce kartında basınca pin **0 mı 1 mi** olduğunu bil.

---

## 3. `while` — koşul doğru olduğu sürece tekrar

### Sonsuz döngü — gömülü kalp

```c
while (1)
{
    if (button_flag) { /* ... */ }
    Chase_Update();
    DelayMs(100);
}
```

`1` her zaman doğrudur → döngü **hiç bitmez**. Tüm uygulama bu döngünün içinde döner.

### Süre dolana kadar bekle (tick ile)

```c
uint32_t t0 = GetTickMs();
while ((GetTickMs() - t0) < 500) {
    /* boş veya çok kısa iş; 500 ms geçene kadar buradasın */
}
/* 500 ms sonra buraya gelirsin */
```

**Dikkat:** Bu döngüde 500 ms boyunca **başka iş yapılmaz** (chase durur). Öğrenme için iyidir; ileride timer interrupt ile “arka planda zaman” daha iyi olur. Perşembe görevlerinde kısa gecikmeler için yeterli.

### `while` ile `for` farkı (kısa)

| | `while` | `for` |
|---|---------|--------|
| Ne zaman? | “Koşul sağlanana kadar” / sonsuz | “N kere” / dizide index |
| Örnek | `while(1)`, bekleme | LED chase, self-test |

---

## 4. `for` — sayılı tekrar ve diziler

`for (başlangıç; koşul; artış)` — en çok **dizi indeksi** ve **sabit sayıda tekrar** için.

### Chase — her LED’i tek tek kontrol

```c
#define LED_COUNT 3
static const uint8_t led_pin[LED_COUNT] = { PIN_LED0, PIN_LED1, PIN_LED2 };
uint8_t active_index = 1;   /* ortadaki LED yansın */

for (int i = 0; i < LED_COUNT; i++) {
    if (i == active_index) {
        Gpio_Write(led_pin[i], 1);
    } else {
        Gpio_Write(led_pin[i], 0);
    }
}
```

**Ne oldu?**  
- `i` 0, 1, 2 diye döner.  
- Sadece `active_index` olan pin yanar.  
- Chase’de her adımda `active_index` değişir; `for` her adımda tüm pinleri günceller.

### Self-test (açılışta bir kez)

```c
for (int i = 0; i < LED_COUNT; i++) {
    Gpio_Write(led_pin[i], 1);
    DelayMs(200);
    Gpio_Write(led_pin[i], 0);
}
```

Cuma zor görevinde demo’nun ilk sahnesi genelde budur.

### `i++` ve index sınırları

- `i++` → i’yi 1 artır.  
- Koşul `i < LED_COUNT` → `i` 0…(N-1); diziyi taşmazsın.  
- `i <= LED_COUNT` yazarsan **bir fazla** erişim → hata.

### Mod ile döngüsel index (chase sınırı)

```c
chase_index = (chase_index + 1) % LED_COUNT;
```

`% LED_COUNT` → index LED sayısını aşınca başa döner (0,1,2,0,1,…).

### Üçlü operatör `? :` (isteğe bağlı, chase’de sık)

```c
Gpio_Write(led_pin[i], (i == active_index) ? 1 : 0);
```

“Eğer i aktif index ise 1, değilse 0” — kısa `if/else` aynı satırda.

---

## 5. `switch` — çoklu seçenek (event / mod)

`if / else if` zinciri uzayınca `switch` okunaklı olur. Özellikle **enum** ile:

```c
typedef enum {
    EVT_NONE,
    EVT_PRESS,
    EVT_LONG
} ButtonEvent_t;

ButtonEvent_t e = Button_Update();

switch (e) {
case EVT_PRESS:
    Led_Toggle(LED1);
    break;          /* switch'ten çık; yoksa aşağıdaki case'ler de çalışır! */
case EVT_LONG:
    Led_PatternFast();
    break;
default:
    break;          /* EVT_NONE veya tanımsız */
}
```

**`break` unutulursa:** C bir sonraki `case`’e “düşer” (fall-through). Bazen bilerek kullanılır; başlangıçta her `case` sonuna `break` koy.

Cuma zor görevinde **uygulama modu** (`MODE_CHASE`, `MODE_PAUSE`…) için `switch` kullanacaksın.

---

## 6. Fonksiyon — kodu bölmek ve okumak

Uzun `main` yerine parçalara ayırırsın.

```c
/* led.h veya main üstü — prototip */
void Led_Init(void);
void Led_Toggle(int index);
bool Button_ReadDebounced(void);

int main(void)
{
    Led_Init();
    Button_Init();

    while (1) {
        if (Button_ReadDebounced()) {
            Led_Toggle(0);
        }
    }
}

/* led.c — gövde */
void Led_Toggle(int index)
{
    /* pin oku/yaz */
}
```

| Kavram | Açıklama |
|--------|----------|
| **Prototip** | “Bu fonksiyon var, imzası şöyle” — derleyici için |
| **Gövde** | `{ ... }` içindeki gerçek kod — Flash’ta |
| **`void`** | Parametre yok veya dönüş yok |
| **`bool` dönüş** | true/false (debounce sonucu vb.) |

`main` okuyan biri akışı görür; detay `led.c` / `button.c` içinde kalır.

---

## 7. Üç gün + C — birleşik örnek (okuma rehberi)

Aşağıdaki kodu **satır satır** main ile ilişkilendir:

```c
volatile bool button_flag = false;   /* Çarşamba: ISR ile paylaşım */

void BTN_IRQHandler(void)
{
    button_flag = true;              /* Sadece işaretle; LED burada yakılmaz */
    /* clear pending */
}

int main(void)
{
    System_Init();
    Gpio_Init();
    Exti_Button_Init();

    uint32_t chase_index = 0;        /* Salı/Perşembe: state RAM'de */
    const uint32_t CHASE_DELAY_MS = 150;

    while (1)                        /* Gömülü: sonsuz döngü */
    {
        if (button_flag) {             /* Çarşamba: kesme sonrası karar */
            button_flag = false;
            chase_index = (chase_index + 1) % LED_COUNT;
        }

        for (int i = 0; i < LED_COUNT; i++) {   /* Perşembe: chase */
            Gpio_Write(led_pin[i], (i == chase_index) ? 1 : 0);
        }

        /* CHASE_DELAY_MS kadar bekle (tick/delay) */
    }
}
```

| Satır grubu | Haftadan |
|-------------|---------|
| `volatile` + ISR | Çarşamba |
| `if (button_flag)` | Çarşamba + `if` |
| `for` + `led_pin[i]` | Perşembe + Pazartesi GPIO |
| `const` gecikme | Salı/Perşembe |
| `while(1)` | Pazartesi |

---

## 8. Sık hatalar ve ne yapmalısın?

| Hata | Belirti | Ne yap? |
|------|---------|---------|
| `if (x = 1)` | Her zaman “doğru” gibi | `==` kullan |
| `while(1)` içinde çok uzun bekleme | Chase/kesme gecikir | Gecikmeyi kısalt; ağır işi böl |
| ISR’da `delay` / `printf` | Takılma, garip davranış | ISR’da sadece flag |
| Dizi taşması `i <= COUNT` | Rastgele LED | `i < COUNT` |
| Flag’de `volatile` yok | Kesme “çalışmıyor” | `volatile bool` |
| Yanlış active-low/high | Buton ters | Şemaya göre `== 0` veya `== 1` |

---

## 9. Perşembe görevleri ile eşleştirme

| Görev | Bu nottan hangi bölüm? |
|-------|-------------------------|
| Kolay blink + buton | §2 `if`, §3 `while(1)`, §1 `const` |
| Orta chase | §4 `for`, dizi, §2 yön `if` |
| Zor self-test + modül | §4 self-test, §6 fonksiyon, §1 `volatile` |

---

## Sonraki adım

Notu okuduysan [`02_Gorevler.md`](02_Gorevler.md) kolay görevle başla. Takılırsan ilgili bölüme dön; küçük adımla derle-yükle-test et.
