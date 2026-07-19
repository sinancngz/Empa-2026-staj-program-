# Gün 01 — GPIO Görevleri

**Herkes aynı görevleri yapar.**  
Sıra: Kolay → Orta → Zor. Bitirdikçe mentöre göster, tik atılsın.

Referans örnekler (repo): `Examples/GPIO/*` · `GPIO_LEDBlinky`

---

## Ortak hazırlık

- [ ] ABOV ortamı kurulu (eMStudio32 açılıyor)
- [ ] Kart USB-C ile bağlı
- [ ] En az bir örnek proje build + flash edildi

---

## Kolay

| # | Görev | Yapıldı |
|---|-------|---------|
| 1 | Bir LED’i sabit yak | ☐ |
| 2 | Aynı LED’i söndür | ☐ |
| 3 | LED’i yanıp söndür (blink) | ☐ |

**Beklenen:** Pin’in output olduğunu ve active-low / active-high farkını fark etmiş olmak.

---

## Orta

| # | Görev | Yapıldı |
|---|-------|---------|
| 1 | Kullanıcı butonunu oku (basılı / değil) | ☐ |
| 2 | Buton basılıyken LED yansın, bırakınca sönsün | ☐ |
| 3 | Buton her basışta LED’i aç/kapa (toggle) | ☐ |

**Beklenen:** Input + pull-up/pull-down bilgisini kullanmak. Gerekirse basit debounce.

---

## Zor

| # | Görev | Yapıldı |
|---|-------|---------|
| 1 | En az 3 LED’i sırayla yak (chase / kayan ışık) | ☐ |
| 2 | Butonla yön veya hız değiştir (ileri ↔ geri **veya** yavaş ↔ hızlı) | ☐ |
| 3 | Başlangıçta kısa self-test: tüm LED’ler bir kez yanıp sönsün | ☐ |

**Beklenen:** Birden fazla pin + basit state / sayaç ile kontrol.

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/gunluk_rapor.md   ← ne yaptın, takıldığın yer
└── proje/                  ← proje dosyaların
```

---

## Mentör tik listesi (özet)

| Stajyer | Kolay | Orta | Zor |
|---------|-------|------|-----|
| A — Yaşar Uçar | ☐ | ☐ | ☐ |
| B — Burak Uçar | ☐ | ☐ | ☐ |
| C — Başar Yıldırım | ☐ | ☐ | ☐ |
| D — Aykut İsmet Aslantaş | ☐ | ☐ | ☐ |
| E — Yavuz Selim Konaç | ☐ | ☐ | ☐ |
