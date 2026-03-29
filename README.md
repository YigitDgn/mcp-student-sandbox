# Mystery Modülü - İkinci Dereceden Denklem Çözücü

## Genel Bakış

Bu modül, `ax² + bx + c = 0` formundaki ikinci dereceden denklemleri çözmek için bir fonksiyon sağlar.

## Fonksiyon

### `fn_x(a, b, c)`

İkinci dereceden denklemi ikinci dereceden formül kullanarak çözer.

**Parametreler:**
- `a`: x² katsayısı (0 olamaz)
- `b`: x katsayısı
- `c`: Sabit terim

**Dönüş Değeri:**
- Diskriminant ≥ 0 ise iki kök tuple'ı `(kök1, kök2)`
- Diskriminant < 0 ise `None` (reel çözüm yok)

**Formül:**
```
x = (-b ± √(b² - 4ac)) / 2a
```

## Kullanım Örnekleri

```python
from mystery_module import fn_x

# Örnek 1: İki reel kök
roots = fn_x(1, -5, 6)
print(roots)  # Çıktı: (3.0, 2.0)

# Örnek 2: Reel çözüm yok
roots = fn_x(1, 0, 1)
print(roots)  # Çıktı: None

# Örnek 3: Tekrarlanan kök
roots = fn_x(1, -2, 1)
print(roots)  # Çıktı: (1.0, 1.0)
```

## Uygulama Detayları

- Karekök hesaplaması için Python'un `math.sqrt()` fonksiyonunu kullanır
- Diskriminant negatif olduğunda `None` döndürür (karmaşık kökler)
- Her iki kökü tek bir işlemde verimli bir şekilde hesaplar

## Gereksinimler

- Python 3.x
- Dış bağımlılık yok
