# Gün 01 — Anlatım Notları

**Tarih:** 2026-07-20 Pazartesi

---

## 1) Tiremo Cortex kartı (kısa)

- Empa Electronics geliştirme kartı
- ABOV A34G43x — ARM Cortex-M4F
- USB-C (CN6): besleme + debug + seri
- Kullanıcı LED’leri → **GPIO output**
- Kullanıcı butonu → **GPIO input**
- Bu stajda önce çevre birimleri tek tek; bugün sadece **GPIO**

Kart dökümanları: `kaynaklar/Tiremo.Cortex.pdf` · `kaynaklar/tiremo_cortex.pptx` · [`kaynaklar/Tiremo_Workshop_README.md`](kaynaklar/Tiremo_Workshop_README.md)

---

## 2) ABOV ortamı (kurulum)

Adım adım: [`kaynaklar/SetUp.md`](kaynaklar/SetUp.md)  
Proje açma / flash: [`kaynaklar/RunningCode.md`](kaynaklar/RunningCode.md)

| Araç | Ne işe yarar |
|------|----------------|
| eMStudio32 | IDE — yaz, derle, debug |
| MCUBrew32 | Pin / çevre birimi konfigürasyonu |
| aFlasher32 | HEX yükleme |
| Tera Term | Seri terminal (UART) |

Önerilen yollar: `C:\ABOV\eMStudio32`, `C:\ABOV\MCUBrew32`

---

## 3) GPIO — bugünün konusu

Tam döküman: [`GPIO_Anlatim.md`](GPIO_Anlatim.md)

Özet:

| Kavram | Anlam |
|--------|--------|
| **GPIO** | Genel amaçlı giriş/çıkış pini |
| **Output** | MCU pin’i sürer → LED yak/söndür |
| **Input** | Pin’i okur → buton basılı mı? |
| **Pull-up** | Dahili/harici direnç ile pin’i HIGH’a çeker |
| **Pull-down** | Pin’i LOW’a çeker |
| **Active-low LED** | Pin LOW iken LED yanar (kartta sık görülür) |

Anlatım sırası önerisi:

1. Output + LED  
2. Input + buton  
3. Pull-up / pull-down neden gerekli  
4. Kısa pratik → görevlere geç
