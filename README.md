# MakerClass Macropad 1 - KMK Firmware

KMK firmware pro MakerClass macropad s 6 tlačítky, rotačním enkodérem a RGB LED indikací.

## Co je KMK?

**KMK** je keyboard firmware napsaný v **CircuitPython** - alternativa k QMK/Vial s výhodami:

- ✅ **Live editing** - změny kódu se projeví okamžitě, žádná kompilace
- ✅ **Jednoduchý Python kód** - snadné úpravy a ladění
- ✅ **Cross-platform** - funguje všude kde běží CircuitPython
- ✅ **Serial console** - živý debug výstup
- ⚠️ **Bez GUI konfigurace** - vše se upravuje v kódu (na rozdíl od Vial)

## Hardware

- **Mikrokontrolér**: Raspberry Pi Pico (RP2040)
- **Tlačítka**: 6 hlavních + 1 encoder switch
- **Encoder**: Rotační enkodér s tlačítkem
- **RGB LED**: 1× WS2812 RGB LED pro indikaci vrstev

## Instalace

### 1. Nainstalovat CircuitPython

1. **Stáhnout CircuitPython** pro Raspberry Pi Pico:
   - https://circuitpython.org/board/raspberry_pi_pico/
   - Stáhnout nejnovější stable verzi (`.uf2` soubor)

2. **Nahrát CircuitPython**:
   - Odpojit Pico od USB
   - Držet tlačítko **BOOTSEL** na Pico
   - Připojit USB (stále držet BOOTSEL)
   - Pusťte BOOTSEL - objeví se disk **RPI-RP2**
   - Přetáhnout `.uf2` soubor na disk
   - Pico se restartuje a objeví se disk **CIRCUITPY**

### 2. Nainstalovat KMK firmware

1. **Stáhnout KMK**:
   ```bash
   git clone https://github.com/KMKfw/kmk_firmware.git
   ```

2. **Zkopírovat KMK na Pico**:
   - Zkopírovat celou složku `kmk/` na disk **CIRCUITPY**

3. **Zkopírovat soubory macropadu**:
   - Z domovské složky repozitářer nakopírovat na CIRCUITPY jednotku:
     - `kb.py`
     - `keymap_cz_auto.py`
     - `code.py`

### 3. Struktura souborů na CIRCUITPY

```
CIRCUITPY/
├── kmk/                    # KMK framework
├── kb.py                   # Hardware konfigurace
├── keymap_cz_auto.py       # České rozložení klávesnice
└── code.py                 # Hlavní firmware
```

**Důležité**: `code.py` je entry point - CircuitPython ho spustí automaticky!

### 4. Restart

- Odpojit a připojit USB
- Nebo zmáčknout **Ctrl+D** v serial console
- RGB LED by se měla rozsvítit **cyan barvou** (BASE vrstva)

## Vrstvy

Macropad má **6 vrstev** s barevnou RGB indikací:

### 0️⃣ BASE - Základní navigace
**🎨 Barva**: Cyan (azurová)

| Tlačítko | Funkce |
|----------|--------|
| 1 | Space |
| 2 | Šipka nahoru |
| 3 | Enter (HOLD = přepínání vrstev) |
| 4 | Šipka vlevo |
| 5 | Šipka dolů |
| 6 | Šipka vpravo |
| 7 (Encoder switch) | Mute |
| **Encoder** | Hlasitost +/- |

### 1️⃣ MEDIA - Ovládání médií
**🎨 Barva**: Green (zelená)

| Tlačítko | Funkce |
|----------|--------|
| 1 | Otevřít Media Player* |
| 2 | Media Stop |
| 3 | --- (HOLD = přepínání vrstev) |
| 4 | Předchozí skladba |
| 5 | Play/Pause |
| 6 | Další skladba |
| 7 (Encoder switch) | Mute |
| **Encoder** | Hlasitost +/- |

*Media Player makro: Win+R → `ms-media-player:` → Enter (funguje s CZ layoutem!)

### 2️⃣ MACROS - Makra a zkratky
**🎨 Barva**: Magenta (fialová)

| Tlačítko | Funkce |
|----------|--------|
| 1 | Alt+Tab |
| 2 | Ctrl+C (kopírovat) |
| 3 | Print Screen (HOLD = přepínání vrstev) |
| 4 | Ctrl+D |
| 5 | Ctrl+V (vložit) |
| 6 | Notepad makro** |
| 7 (Encoder switch) | Mute |
| **Encoder** | Hlasitost +/- |

**Notepad makro: Win+R → notepad → "Ahoj z MakerClass!" (funguje s CZ layoutem!)

### 3️⃣ TYPE - Psaní textu
**🎨 Barva**: Yellow (žlutá)

| Tlačítko | Funkce |
|----------|--------|
| 1 | M |
| 2 | A |
| 3 | K (HOLD = přepínání vrstev) |
| 4 | E |
| 5 | R |
| 6 | S |
| 7 (Encoder switch) | RGB Toggle |
| **Encoder** | RGB Hue (změna barvy) |

Slovo: **MAKERS** (M-A-K-E-R-S)

### 4️⃣ UTILS - Nastavení
**🎨 Barva**: Red (červená)

| Tlačítko | Funkce |
|----------|--------|
| 1 | RGB Mode (přepínání efektů) |
| 2 | RGB Hue Increase (změna barvy) |
| 3 | --- (HOLD = přepínání vrstev) |
| 4 | RGB Toggle (zap/vyp RGB) |
| 5 | Reload (restart firmware) |
| 6 | RGB Animation Increase (rychlost animace) |
| 7 (Encoder switch) | --- |
| **Encoder** | RGB Brightness (jas) |

### 5️⃣ LAYER_SWITCH - Přepínání vrstev
**🎨 Barva**: White (bílá)

| Tlačítko | Funkce |
|----------|--------|
| 1 | Přepnout na BASE |
| 2 | Přepnout na MEDIA |
| 3 | --- |
| 4 | Přepnout na MACROS |
| 5 | Přepnout na TYPE |
| 6 | Přepnout na UTILS |

## Přepínání vrstev

1. **Držte tlačítko 3** (na jakékoli vrstvě)
2. **Zobrazí se vrstva LAYER_SWITCH** (bílá LED)
3. **Zmáčkněte tlačítko** pro přepnutí:
   - Tlačítko 1 → BASE (Cyan)
   - Tlačítko 2 → MEDIA (Green)
   - Tlačítko 4 → MACROS (Magenta)
   - Tlačítko 5 → TYPE (Yellow)
   - Tlačítko 6 → UTILS (Red)
4. **Pusťte tlačítko 3**

RGB LED se změní na barvu aktivní vrstvy.

## RGB Efekty

### Dostupné módy

Zmáčkněte **RGB_MOD** (UTILS vrstva, tlačítko 1) pro cyklování:

1. **STATIC** - Layer indication (barvy podle vrstvy) ✨ výchozí
2. **BREATHING** - Dýchání (pulzující jas)
3. **RAINBOW** - Duha (plynulá změna barev)
4. **BREATHING_RAINBOW** - Kombinace dýchání + duha
5. **KNIGHT**
6. **SWIRL**

### Parametry RGB

- **Rychlost animace**: 3× rychlejší než výchozí (lze změnit v `code.py`)
- **Výchozí jas**: 128/255 (50%)
- **Breathing rozsah**: 1.5× (výraznější efekt)

### Ovládání RGB

- **RGB_MOD** (UTILS/1) - Přepíná mezi módy
- **RGB_TOG** (UTILS/4, TYPE/7) - Zapnout/vypnout RGB
- **RGB_HUI** (UTILS/2) - Změna barvy (hue)
- **RGB_ANI** (UTILS/6) - Změna rychlosti animace
- **Encoder na TYPE vrstvě** - RGB Hue (změna barvy)
- **Encoder na UTILS vrstvě** - RGB Brightness (jas)

**Poznámka**: Layer indication (barvy vrstev) funguje pouze v **STATIC** módu!

## České rozložení klávesnice

Firmware obsahuje **automatickou podporu českého QWERTZ layoutu** (vygenerovanou pomocí AI)!

Znaky vyžadující AltGr (pravý Alt) musí být explicitní:

```python
# ❌ Nefunguje
KC.MACRO('email@example.com')

# ✅ Funguje
KC.MACRO('email', Tap(KC.CZ_AT), 'example.com')
```

## Vlastní makra

### Jak vytvořit makro

Editujte `code.py` (sekce "Makra"):

```python
# Jednoduché makro
M_HELLO = KC.MACRO('Hello World!')

# Makro s klávesami
M_COPY_PASTE = KC.MACRO(
    Press(KC.LCTL), Tap(KC.C), Release(KC.LCTL),
    Delay(100),
    Press(KC.LCTL), Tap(KC.V), Release(KC.LCTL)
)

# Win+R helper
M_CALC = win_run('calc')

# Email/URL makro
M_EMAIL = KC.MACRO('email', Tap(KC.CZ_AT), 'example.com')
```

### Přidat do keymap

```python
keyboard.keymap = [
    # ...
    [
        M_HELLO,  M_COPY_PASTE,  M_CALC,  # ...
    ],
]
```

### Uložit a testovat

1. Uložit `code.py`
2. Pico se automaticky restartuje (auto-reload)
3. Makro je okamžitě funkční!

### Změna TYPE vrstvy

Chcete místo MAKERS něco jiného? Editujte `code.py`:

```python
# TYPE vrstva (řádek ~140)
[
    KC.M,  KC.A,  KC.LT(_LAYER_SWITCH, KC.K),  KC.E,  KC.R,  KC.S,  KC.RGB_TOG
],
```

Můžete použít například:
- Jiné písmena/znaky
- Často používané zkratky
- Navigační klávesy (KC.HOME, KC.END, KC.PGUP, KC.PGDN)

## Live Editing

**Největší výhoda KMK**: Změny se projeví okamžitě!

1. Připojit Pico jako USB disk (**CIRCUITPY**)
2. Editovat `code.py` v textovém editoru
3. **Uložit** - Pico se automaticky restartuje
4. Změny jsou aktivní za ~1 sekundu!

**Tipy:**
- Použít VS Code s Python extension
- Sledovat serial console pro debug výpisy
- Backup `code.py` před velkými změnami

## Serial Console (Debug)

Sledujte živý debug výstup:

### Linux/Mac
```bash
screen /dev/ttyACM0 115200
```

### Windows
- **PuTTY** nebo **Tera Term**, 115200 baud
- Port: hledejte "CircuitPython CDC"

## Porovnání KMK vs QMK/Vial

| Vlastnost | KMK | QMK/Vial |
|-----------|-----|----------|
| **Programování** | Python | C |
| **Kompilace** | ❌ Není potřeba | ✅ Nutná |
| **Live editing** | ✅ Okamžité změny | ❌ Musí překompilovat |
| **GUI konfigurace** | ❌ Pouze kód | ✅ Vial web app |
| **Debug** | ✅ Serial console | ⚠️ QMK Console |
| **Velikost firmware** | ~1.5 MB | ~30 KB |
| **Rychlost odezvy** | Dobrá | Vynikající |
| **Učící křivka** | Nízká (Python) | Střední (C) |
| **Vlastní makra** | Velmi snadné | Složitější |

**Doporučení**:
- **KMK** - pokud chcete experimentovat, rychle měnit konfiguraci, učit se
- **QMK/Vial** - pokud chcete stabilní, rychlé firmware s GUI konfigurací

## Odkazy

- **KMK dokumentace**: http://kmkfw.io/
- **CircuitPython**: https://circuitpython.org/
- **QMK/Vial verze**: https://github.com/MakerClassCZ/macropad1-vial-qmk

## Autor

MakerClass (@makerclass)
Licence: GPL-3.0
