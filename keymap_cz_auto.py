# Czech (QWERTZ) Keymap for KMK - Automatic String Support
# Patches KC dictionary to automatically handle Czech layout in string macros
#
# Usage:
#   import keymap_cz_auto
#   M_URL = KC.MACRO('https://example.com')

from kmk.keys import KC

print('Czech layout: Auto string support enabled')

_KC_class = type(KC)
if not hasattr(_KC_class, '_original_getitem'):
    _original_getitem = _KC_class.__getitem__

# ASCII character mapping for CZ layout
_CZ_CHAR_MAP = {
    # Numbers (require Shift on CZ layout)
    '1': 'N1_SHIFT',
    '2': 'N2_SHIFT',
    '3': 'N3_SHIFT',
    '4': 'N4_SHIFT',
    '5': 'N5_SHIFT',
    '6': 'N6_SHIFT',
    '7': 'N7_SHIFT',
    '8': 'N8_SHIFT',
    '9': 'N9_SHIFT',
    '0': 'N0_SHIFT',

    # Special characters
    '!': 'QUOT_SHIFT',
    '%': 'MINS_SHIFT',
    '(': 'RBRC_SHIFT',
    ')': 'RBRC',
    '-': 'SLSH',
    '=': 'MINS',
    '_': 'SLSH_SHIFT',
    '/': 'LBRC_SHIFT',
    ':': 'DOT_SHIFT',
    ';': 'COMM',
    '?': 'COMM_SHIFT',
    '"': 'SCLN_SHIFT',

    # QWERTZ layout (Y and Z swapped)
    'y': 'Z',
    'z': 'Y',
    'Y': 'Z_SHIFT',
    'Z': 'Y_SHIFT',
}

# Shifted character mapping (base_key, needs_shift)
_CZ_SHIFT_MAP = {
    # Numbers
    'N1_SHIFT': ('N1', True),
    'N2_SHIFT': ('N2', True),
    'N3_SHIFT': ('N3', True),
    'N4_SHIFT': ('N4', True),
    'N5_SHIFT': ('N5', True),
    'N6_SHIFT': ('N6', True),
    'N7_SHIFT': ('N7', True),
    'N8_SHIFT': ('N8', True),
    'N9_SHIFT': ('N9', True),
    'N0_SHIFT': ('N0', True),
    # Special characters
    'QUOT_SHIFT': ('QUOT', True),
    'MINS_SHIFT': ('MINS', True),
    'RBRC_SHIFT': ('RBRC', True),
    'SLSH_SHIFT': ('SLSH', True),
    'LBRC_SHIFT': ('LBRC', True),
    'DOT_SHIFT': ('DOT', True),
    'COMM_SHIFT': ('COMM', True),
    'SCLN_SHIFT': ('SCLN', True),
    # QWERTZ
    'Z_SHIFT': ('Z', True),
    'Y_SHIFT': ('Y', True),
}

def _cz_getitem(cls, key):
    """Custom __getitem__ for Czech layout with automatic string remapping"""
    if not isinstance(key, str):
        return _original_getitem(cls, key)

    if len(key) == 1 and key in _CZ_CHAR_MAP:
        mapped = _CZ_CHAR_MAP[key]

        if mapped in _CZ_SHIFT_MAP:
            base_key, needs_shift = _CZ_SHIFT_MAP[mapped]
            base = _original_getitem(cls, base_key)
            if needs_shift:
                return KC.LSFT(base)
            return base

        return _original_getitem(cls, mapped)

    return _original_getitem(cls, key)

# Monkey-patch KC.__getitem__
_KC_class.__getitem__ = classmethod(_cz_getitem)

# CZ keycodes for explicit use (AltGr characters, etc.)

# CZ-specific characters on number row
KC.CZ_PLUS = KC.N1
KC.CZ_ECAR = KC.N2
KC.CZ_SCAR = KC.N3
KC.CZ_CCAR = KC.N4
KC.CZ_RCAR = KC.N5
KC.CZ_ZCAR = KC.N6
KC.CZ_YACU = KC.N7
KC.CZ_AACU = KC.N8
KC.CZ_IACU = KC.N9
KC.CZ_EACU = KC.N0

# Shifted numbers
KC.CZ_1 = KC.LSFT(KC.N1)
KC.CZ_2 = KC.LSFT(KC.N2)
KC.CZ_3 = KC.LSFT(KC.N3)
KC.CZ_4 = KC.LSFT(KC.N4)
KC.CZ_5 = KC.LSFT(KC.N5)
KC.CZ_6 = KC.LSFT(KC.N6)
KC.CZ_7 = KC.LSFT(KC.N7)
KC.CZ_8 = KC.LSFT(KC.N8)
KC.CZ_9 = KC.LSFT(KC.N9)
KC.CZ_0 = KC.LSFT(KC.N0)

# Basic special characters
KC.CZ_EQL = KC.MINS
KC.CZ_MINS = KC.SLSH
KC.CZ_COLN = KC.LSFT(KC.DOT)
KC.CZ_SLSH = KC.LSFT(KC.LBRC)
KC.CZ_UNDS = KC.LSFT(KC.SLSH)

# AltGr characters
KC.CZ_AT = KC.RALT(KC.V)
KC.CZ_HASH = KC.RALT(KC.X)
KC.CZ_DLR = KC.RALT(KC.SCLN)
KC.CZ_PERC = KC.LSFT(KC.MINS)
KC.CZ_CIRC = KC.RALT(KC.N3)
KC.CZ_AMPR = KC.RALT(KC.C)
KC.CZ_ASTR = KC.RALT(KC.SLSH)
KC.CZ_LPRN = KC.LSFT(KC.RBRC)
KC.CZ_RPRN = KC.RBRC
KC.CZ_LBRC = KC.RALT(KC.F)
KC.CZ_RBRC = KC.RALT(KC.G)
KC.CZ_LCBR = KC.RALT(KC.B)
KC.CZ_RCBR = KC.RALT(KC.N)
KC.CZ_BSLS = KC.RALT(KC.Q)
KC.CZ_PIPE = KC.RALT(KC.W)
KC.CZ_LABK = KC.RALT(KC.COMM)
KC.CZ_RABK = KC.RALT(KC.DOT)
KC.CZ_TILD = KC.RALT(KC.N1)
KC.CZ_GRV = KC.RALT(KC.N7)
KC.CZ_EURO = KC.RALT(KC.E)

# QWERTZ layout
KC.CZ_Z = KC.Y
KC.CZ_Y = KC.Z
