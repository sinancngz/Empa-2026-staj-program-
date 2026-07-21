# Gün 02 — Görevler (MCU · buton · debounce · event)

**Herkes aynı görevleri yapar.**  
Sıra: Kolay → Orta → Zor. Bitince çalışmanı göster / teslim et.

Dün: LED + buton.  
Bugün: **debounce**, **kısa / uzun basış**, **event** — karttaki **MCU** üzerinde.

Anlatım: [`01_Anlatim.md`](01_Anlatim.md) · Referans: `Examples/GPIO/*`

---

## Ortak hazırlık

- [ ] eMStudio32 / proje açılıyor, kart USB-C ile bağlı
- [ ] Dünkü proje veya bugün için yeni proje hazır
- [ ] MPU / MCU notunu okudun ([`01_Anlatim.md`](01_Anlatim.md))
- [ ] LED çıkış, buton giriş (pull) çalışıyor

---

## Kolay

| Görev | Yapıldı |
|-------|---------|
| Debounce’lu buton: her **gerçek** basışta LED bir kez toggle — basılı tutunca spam / titreşim olmasın | ☐ |

**Beklenen:** ~20 ms debounce (gecikme veya ardışık okuma). State değişkenleri (**MCU RAM**): örn. `last_raw`, `stable`, `last_change_ms`.

---

## Orta

| Görev | Yapıldı |
|-------|---------|
| Kısa ve uzun basışı ayır (eşik örn. **1 sn**): kısa → LED toggle; uzun → farklı LED pattern veya tüm LED flash | ☐ |

**Beklenen:** Süre tick / clock ile; debounce hâlâ açık. Eşik `const`, süre sayacı RAM’de.

---

## Zor

| Görev | Yapıldı |
|-------|---------|
| `Press` / `Release` / `Long` event üret (`enum` + state); en az 2 LED’i event’lere bağla; `button.h` + `button.c`/`.cpp` ayır. Bitince kendi **GitHub** repona bugünün tarihiyle yükle | ☐ |

**Beklenen:** `main` sadece init + döngü + event’e tepki. Kartta göster; repo linkini rapora yaz.

### GitHub teslimi (zor)

1. Pazartesi kurduğun **kendi** GitHub staj reponu kullan (yoksa bugün oluştur).  
2. Bugünün zor görevini **günün tarihiyle** yükle:

```
YYYY-MM-DD/
└── ...
```

Bugün: **`2026-07-21`**

3. README’de debounce / eşik (ms) ve kısa not; repo URL’sini günlük rapora ekle.

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/gunluk_rapor.md    ← GitHub repo URL’si
└── proje/
```

Ayrıca: zor görev → kendi GitHub repon (`2026-07-21/`).

Raporda 2–3 cümle: debounce nasıl, kısa/uzun eşik kaç ms, “state RAM’de / kod Flash’ta” kendi örneğinle.
