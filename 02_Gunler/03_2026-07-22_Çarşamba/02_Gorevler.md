# Gün 03 — Görevler

Kesme (interrupt), NVIC ve harici kesme

Herkes aynı sırayı izler: **Kolay → Orta → Zor**. Bitince çalışmanı göster ve teslim et.

Önce anlatımı oku: [`01_Anlatim.md`](01_Anlatim.md)

Bugünkü pratik, önceki günlerle birleşir:

| Gün | Ne öğrenmiştin? | Bugün nerede kullanacaksın? |
|-----|-----------------|------------------------------|
| Pazartesi | GPIO: LED yaz, buton oku | LED çıkış, pin Input + pull |
| Salı | Debounce, kısa / uzun basış | Spam yok, süre ölçümü |
| Çarşamba | Kesme, ISR, NVIC | Butonu poll etme; kenarda ISR |

---

## Ortak hazırlık

Başlamadan şunlar hazır olsun:

- [ ] Kart USB-C ile bağlı, proje derleniyor
- [ ] [`01_Anlatim.md`](01_Anlatim.md) okundu
- [ ] En az **1 LED** (çıkış) ve **kullanıcı butonu** (giriş) tanımlı
- [ ] Pin config'te buton için:
  - **Pin Mode:** Input
  - **Pull:** şemana göre Pull-Up veya Pull-Down
  - **Interrupt Operation Mode:** Edge
  - **Interrupt Triggering Mode:** Pull-up ise genelde **Falling**, Pull-down ise **Rising**
- [ ] İlgili kesme NVIC'te açık (enable)

---

## Kolay

**Amaç:** Butonu artık döngüde sürekli okumayacaksın. Basılınca donanım seni uyandıracak; sen de bir LED'i aç/kapa yapacaksın.

| | |
|---|---|
| **Görev** | Harici kesme ile LED toggle |
| **Yapıldı** | ☐ |

### Ne yapacaksın? (adım adım)

1. Buton pinini yukarıdaki gibi **kesme** olacak şekilde ayarla.
2. `volatile bool button_flag = false;` gibi bir bayrak tanımla (**MCU RAM**).
3. **ISR** içinde (kesme fonksiyonu):
   - `button_flag = true;` yaz
   - Kesme bayrağını / pending'i **temizle** (yoksa ISR tekrar tekrar girer)
   - Uzun iş, `delay`, LED yakma **yapma** — ISR kısa kalsın
4. `main` / `while(1)` içinde:
   - `button_flag` true ise → `false` yap → LED'i **toggle** et
5. Döngüde `Gpio_Read(buton)` ile sürekli kontrol **etme** (polling yasak).

### Doğru çalışıyor mu?

- Butona her (temiz) basışta LED bir kez değişir.
- Basılı tutunca LED çılgınca yanıp sönmez (en azından kolay seviyede kenar doğruysa).
- Polling kullandığını söylersen görev tamam sayılmaz.

### Kısa hatırlatma

```
butona bas → kenar → NVIC → ISR (flag=1) → main flag görür → LED toggle
```

---

## Orta

**Amaç:** Salı'daki kısa / uzun basışı, bugün **kesme** ile birleştir. ISR sadece "bir şey oldu" der; süre ve LED işi `main`'de kalır.

| | |
|---|---|
| **Görev** | Kesme + debounce + kısa / uzun basış |
| **Yapıldı** | ☐ |

### Ne yapacaksın? (adım adım)

1. Kolaydaki gibi buton **harici kesme** ile gelsin (`volatile` flag veya kenar bilgisi).
2. **Debounce** ekle — tek basış birden fazla ISR / event üretmesin:
   - yazılım: son geçerli zamandan beri örn. **20 ms** geçmediyse yok say, **veya**
   - pin config'te **Debouncing Filter** aç
3. Basılı tutma süresini ölç (`GetTickMs` / timer / bildiğin tick):
   - **Kısa basış** (örn. bırakınca süre < 1 sn) → **LED1** toggle
   - **Uzun basış** (örn. ≥ **1 sn**) → **LED2** kısa flash veya farklı pattern
4. Süre ölçümü ve LED animasyonu **ISR içinde olmasın**; `main` döngüsünde olsun.

### Doğru çalışıyor mu?

- Hızlı çift yanma / spam yok (debounce işliyor).
- Kısa basış ile uzun basış **farklı** LED davranışı üretiyor.
- ISR'da sadece flag / zaman damgası gibi hafif iş var.

### Salı ile fark

Salı'da butonu döngüde okuyordun. Bugün olay **EXTI / kesme** ile geliyor; kısa–uzun mantığı aynı, kaynak değişti.

---

## Zor

**Amaç:** Üç günün özetini tek projede topla: kayan ışık (Pazartesi) + debounce'lu event (Salı) + kesmeyle kontrol (Çarşamba). Sonra GitHub'a yükle.

| | |
|---|---|
| **Görev** | Kayan ışık + kesmeli kontrol + GitHub |
| **Yapıldı** | ☐ |

### Ne yapacaksın? (adım adım)

1. En az **3 LED** ile kayan ışık (chase): LED'ler sırayla aksın.
2. Ana döngü chase'i sürekli çalıştırsın.
3. Buton **kesme** ile gelsin; debounce'lu **tek event** üretsin (spam yok).
4. Event'e göre:
   - chase **yönünü** değiştir (ileri ↔ geri), **veya**
   - chase **hızını** değiştir (yavaş ↔ hızlı)
5. İstersen kodu böl: `button.h` / `button.c` (veya `.cpp`) ve LED tarafı ayrı dosya; `main` init + döngü + event'e tepki.
6. Bitince kendi GitHub repona yükle (aşağıya bak).

### Doğru çalışıyor mu?

- Chase kendi başına akıyor.
- Butona basınca yön veya hız net değişiyor.
- ISR sadece sinyal; LED sırası `main`'de güncelleniyor.
- Repo linki raporda var.

### GitHub teslimi

1. Kendi staj reponu kullan (yoksa oluştur).
2. Bugünün klasörüne koy:

```
2026-07-22/
└── ...    (kaynak kod / proje)
```

3. Kısa README: ne yaptın, kenar Rising mi Falling mi, debounce nasıl.
4. Repo URL'sini `gunluk_rapor.md` içine yaz.

---

## Rapora eklenecek — teorik sorular

`gunluk_rapor.md` içinde **kendi cümlelerinle** cevapla (ders notunu kopyalama). Her soruya 2–5 cümle yeter.

### Pazartesi'den

1. GPIO'da **Input** ile **Output** farkı nedir? LED ve buton hangisine girer?
2. **Pull-up** ne işe yarar? Pull kapalı (floating) pin neden sorun çıkarır?

### Salı'dan

3. **MPU** ile **MCU** farkını bir örnekle anlat (kartındaki çip hangisi?).
4. `bool led_on` ve `void Led_Toggle()` bellekte kabaca nerede durur (RAM / Flash)? Neden?
5. Debounce olmadan butonla toggle neden "çift basış" gibi görünür?

### Çarşamba'dan

6. **Polling** ile **kesme** farkı nedir? Bugünkü kolay görevde hangisini kullandın?
7. **ISR** nedir? İçinde neden uzun `delay` veya ağır iş istenmez?
8. **NVIC** ne işe yarar? "Öncelik" ve "nested"i bir cümleyle açıkla.
9. Pull-up butonda basışı yakalamak için genelde **Rising** mi **Falling** mi? Neden?
10. `volatile bool button_flag` neden `volatile`?

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/gunluk_rapor.md    ← teori cevapları + GitHub URL
└── proje/
```

Zor görev ayrıca: GitHub → `2026-07-22/`.
