# Gün 12 — Kaynaklar

| Kaynak | Ne için? |
|--------|----------|
| [Sensirion embedded-i2c-sht4x](https://github.com/Sensirion/embedded-i2c-sht4x) | Resmi SHT4x driver |
| SHT40 datasheet (Sensirion) | Komutlar, timing, formüller |
| Dünkü I2C Scanner projesi | Adres doğrulama |

### HAL uyarlama notu

Kütüphanedeki `sensirion_i2c_hal.c` (isim sürümden sürüme değişebilir) içindeki:

- bus init  
- sleep  
- i2c write / read  

fonksiyonlarını kartının I2C API’sine bağla. Sensör API dosyalarını (`sht4x.c`) gereksiz yere değiştirme.
