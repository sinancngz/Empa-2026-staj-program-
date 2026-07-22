# Hafta 1 Özeti ve C ile Modüler Kod

Dizi, fonksiyon, enum ve mini proje iskeleti

Cuma günü yeni donanım konusu az; **haftanın parçalarını tek projede birleştirmek** çok. Bu not “ne yaptık, kodu nasıl düzenleriz, demo nasıl anlatılır” sorularını cevaplar. Asıl süre [`02_Gorevler.md`](02_Gorevler.md) görevlerinde.

---

## Hafta 1 — ne yaptık? (büyük resim)

Beş günde kart üzerinde şu yolu izledin:

| Gün | Donanım / kavram | C ile ne kullandık? | Kartta somut örnek |
|-----|------------------|---------------------|---------------------|
| Pazartesi | GPIO, LED, buton | `if`, `while(1)`, pin oku/yaz | LED toggle, basınca yan |
| Salı | MCU, RAM/Flash, debounce | `uint32_t`, `const`, state | Kısa/uzun basış ayrımı |
| Çarşamba | Kesme, NVIC, EXTI | `volatile`, ISR + flag | Buton kesmesi → main’de işle |
| Perşembe | Temel C pekiştirme | `for`, `switch`, fonksiyon | Chase, self-test iskeleti |

**Cuma hedefi:** Yukarıdakilerin hepsi **aynı firmware** içinde — okunaklı dosyalar, anlamlı isimler, 8–10 dakikalık demo.

### Cuma günü nasıl çalışılır?

1. **09:00–09:45:** Bu notu oku; özellikle “modüler dosya” ve “mini ürün parçaları” bölümlerini.  
2. **09:45–12:30:** Görevlerde önce **tek dosyada çalışan** `main`, sonra `led.c` / `button.c` ayır.  
3. **Öğleden sonra:** `enum` + `switch` ile mod/panel; GitHub `2026-07-24` klasörü.  
4. **Gün sonu:** Raporda hafta tablosu + “hangi `if`/`for` nerede” + repo linki.

En kolay yol: Perşembe chase/blink projeni **genişletmek**; sıfırdan yazmak zorunda değilsin.

---

## 1. Dizi — birden fazla LED / pin listesi

Tek tek `Gpio_Write(LED1,…)`, `Gpio_Write(LED2,…)` yazmak yerine pinleri **dizide** toplarsın.

```c
#define LED_COUNT 4

static const uint8_t led_pin[LED_COUNT] = {
    PIN_LED0, PIN_LED1, PIN_LED2, PIN_LED3
};

void Led_AllOff(void)
{
    for (int i = 0; i < LED_COUNT; i++) {
        Gpio_Write(led_pin[i], 0);
    }
}
```

**Neden dizi?**  
- Chase: `active_index` değişince tek `for` tüm LED’leri günceller.  
- Self-test: aynı döngü, sadece içine `DelayMs` eklersin.  
- Yeni LED eklemek: `LED_COUNT` ve diziye bir eleman — `for` döngüsünü değiştirmene gerek kalmaz.

**Bellek:**  
- `static const uint8_t led_pin[]` → pin numaraları değişmez → çoğu zaman **Flash**.  
- Çalışma anında değişen `chase_index`, `mode` → **RAM**.

---

## 2. `struct` — ilgili değişkenleri bir arada tutmak

Debounce için ayrı ayrı `bool stable`, `uint32_t last_change_ms` yerine tek paket:

```c
typedef struct {
    bool     stable;
    bool     last_raw;
    uint32_t last_change_ms;
    uint32_t down_ms;
} ButtonState_t;

static ButtonState_t btn = { 0 };   /* başlangıçta hepsi sıfır */
```

**Fayda:**  
- `Button_Update(&btn)` gibi tek fonksiyon tüm state’i günceller.  
- `main` içinde dağınık global değişken sayısı azalır.  
- Cuma orta/zor görevde `button.c` içinde `static ButtonState_t` tutmak yaygın bir düzendir.

İlk haftada struct şart değil; ama kod büyüyünce okunurluk için çok işe yarar.

---

## 3. `enum` — anlamlı mod ve olay isimleri

Sihirli sayılar (`mode = 0`, `mode = 1`) yerine isim:

```c
typedef enum {
    APP_IDLE,
    APP_CHASE,
    APP_ERROR
} AppMode_t;

static AppMode_t mode = APP_CHASE;
```

Derleyici `APP_CHASE`’i arka planda sayıya çevirir; sen kodda **isim** kullanırsın.

**`switch` ile kullanım:**

```c
switch (mode) {
case APP_IDLE:
    /* LED söndür veya bekle */
    break;
case APP_CHASE:
    Chase_Step();
    break;
case APP_ERROR:
    Led_BlinkFast();
    break;
default:
    mode = APP_CHASE;
    break;
}
```

Zor görevde “panel” hissi: kısa basış → mod değişir, uzun basış → hız değişir — hepsi `enum` + `switch` veya `if` ile.

---

## 4. Modüler dosya düzeni (öneri ve neden)

Tek `main.c` içinde 500 satır yazmak derlenir ama **bakım zor**. Hafta 1 sonunda şu ayrım yeterli:

```
main.c          → init + while(1) + yüksek seviye akış
gpio_led.h/c    → Led_Init, Led_ChaseStep, Led_AllOff, Led_SelfTest
button.h/c      → Button_Init, Button_Update (veya flag okuma)
app.h/c         → App_Tick, mod, demo senaryoları (isteğe bağlı)
```

**`.h` dosyası:** Dışarıya açılan fonksiyon prototipleri (`#ifndef` guard ile).  
**`.c` dosyası:** Gerçek kod; `static` değişkenler sadece o dosyada görünür.

`main` kısa kalmalı — okuyan kiriş akışı görür:

```c
#include "gpio_led.h"
#include "button.h"
#include "app.h"

int main(void)
{
    System_Init();
    Led_Init();
    Button_Init();

    App_SelfTest();   /* açılış: for ile LED dene */

    while (1) {
        Button_PollOrProcessFlags();
        App_Tick();   /* chase, switch(mode), blink */
    }
}
```

**Derleme:** Tüm `.c` dosyaları projeye eklenir; linker hepsini bir `.elf` / `.hex` yapar. Bir fonksiyonu `led.c`’ye taşıdığında `main.c` sadece `gpio_led.h` include eder.

---

## 5. Hafta 1 mini ürün — mantıksal parçalar (demo iskeleti)

Cuma görevlerinin özü şu akıştır; hepsini **tek projede** birleştirirsin:

| Sıra | Ne olur? | Haftadan hangi C? |
|------|----------|-------------------|
| 1 | Açılış self-test | Pazartesi GPIO + Perşembe `for` |
| 2 | Normal mod: chase veya blink | `while(1)` + `for` + index |
| 3 | Buton: polling veya kesme | Salı debounce veya Çarşamba flag |
| 4 | Karar: kısa/uzun, mod değişimi | `if` / `else if` / `switch` |
| 5 | Çıktı: LED | GPIO |
| 6 | (İsteğe bağlı) UART bir satır | `printf` veya driver |

UART şart değilse görevde isteğe bağlı kalır; **GPIO + buton + düzenli C yapısı** zorunlu.

**Self-test örneği (demo 1. sahne):**

```c
void App_SelfTest(void)
{
    for (int i = 0; i < LED_COUNT; i++) {
        Gpio_Write(led_pin[i], 1);
        DelayMs(150);
        Gpio_Write(led_pin[i], 0);
    }
    DelayMs(300);
}
```

---

## 6. Kendin kontrol et (Cuma öncesi)

Aşağıdakiler projende var mı? Yoksa görev listesine dön.

- [ ] `while(1)` ana döngü var  
- [ ] En az bir yerde `for` (chase veya self-test)  
- [ ] En az bir yerde `if` / `else` (buton, flag veya mod)  
- [ ] Süre veya sayaç için `uint32_t` (veya uygun sabit genişlik)  
- [ ] Eşik değerleri `const`  
- [ ] Kesme kullanıyorsan paylaşılan değişken `volatile`  
- [ ] ISR kısa; LED/chase mantığı `main` veya `App_Tick` içinde  
- [ ] İsimler anlamlı (`led_on`, `press_count`, `APP_CHASE`)  
- [ ] En az iki `.c` dosyası (ör. `main` + `led` veya `button`)

---

## 7. Demo ve rapor (8–10 dakika)

Demo sırası net olursa jüri/mentör takip eder:

1. **Kart açılış** → self-test: LED’ler sırayla yanıp söner.  
2. **Normal mod** → chase veya yavaş blink görünür.  
3. **Buton** → kısa basış: toggle veya yön; uzun basış: hız veya farklı mod.  
4. **(Varsa)** UART’ta `OK` veya `mode=chase` gibi tek satır.

**Raporda yazman gerekenler (özet):**

- Hafta tablosu: hangi gün hangi özellik projede nerede.  
- Kod referansı: örnek bir `if` ve bir `for` satırı (dosya adı + ne işe yaradığı).  
- GitHub: `2026-07-24` klasörü linki veya repo yolu.  
- Çarşamba’daki 10 teori sorusu cevapları (görev dosyasında isteniyorsa) bu rapora eklenir.

---

## 8. Sık takılma noktaları (Cuma)

| Sorun | Olası neden | Çözüm |
|-------|-------------|--------|
| Chase durdu | `while` içinde uzun `delay` | Gecikmeyi kısalt; `App_Tick` her döngüde çağrılsın |
| Kesme çalışmıyor | `volatile` yok veya NVIC kapalı | Flag `volatile`; EXTI/NVIC init |
| Self-test sonra karanlık | `Led_AllOff` unutuldu | Self-test sonrası chase’e geç |
| Link hatası | `.c` projeye eklenmedi | IDE’de `led.c` / `button.c` build’e dahil |
| `switch` garip davranış | `break` eksik | Her `case` sonuna `break` |

---

## Sonraki adım

Bu notu okuduysan [`02_Gorevler.md`](02_Gorevler.md) ile doğrudan projene geç. Önce çalışan monolit, sonra dosya ayırma — adım adım ilerle.
