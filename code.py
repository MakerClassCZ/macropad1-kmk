import board
from kb import KMKKeyboard

from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.keys import KC, Key
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.macros import Macros, Press, Tap, Release, Delay

import keymap_cz_auto

print('MakerClass Macropad 1 (CZ Auto)')

keyboard = KMKKeyboard()

_BASE, _MEDIA, _MACROS, _TYPE, _UTILS, _LAYER_SWITCH = 0, 1, 2, 3, 4, 5

LAYER_COLORS = {
    _BASE: (128, 255, 128),
    _MEDIA: (85, 255, 128),
    _MACROS: (213, 255, 128),
    _TYPE: (43, 255, 128),
    _UTILS: (0, 255, 128),
    _LAYER_SWITCH: (0, 0, 160),
}

class LayerRGB(RGB):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_mode_active = False

    def on_layer_change(self, layer):
        if self.user_mode_active:
            return

        if self.animation_mode in (AnimationModes.STATIC, AnimationModes.STATIC_STANDBY):
            if layer in LAYER_COLORS:
                self.hue, self.sat, self.val = LAYER_COLORS[layer]
                self.set_hsv_fill(self.hue, self.sat, self.val)
                self.show()

rgb = LayerRGB(
    pixel_pin=board.GP11,
    num_pixels=1,
    val_limit=255,
    val_default=128,
    hue_default=128,
    sat_default=255,
    animation_mode=AnimationModes.STATIC,
    breathe_center=1.5,
    animation_speed=3,
)

class RGBLayers(Layers):
    def activate_layer(self, keyboard, layer, idx=None):
        super().activate_layer(keyboard, layer, idx)
        rgb.on_layer_change(layer)

    def deactivate_layer(self, keyboard, layer):
        super().deactivate_layer(keyboard, layer)
        if keyboard.active_layers:
            rgb.on_layer_change(keyboard.active_layers[0])

layers = RGBLayers()
encoder_handler = EncoderHandler()
macros = Macros()
media_keys = MediaKeys()

encoder_handler.pins = ((board.GP16, board.GP17, None),)
encoder_handler.divisor = 4

encoder_handler.map = (
    ((KC.VOLD, KC.VOLU, None),),
    ((KC.VOLD, KC.VOLU, None),),
    ((KC.VOLD, KC.VOLU, None),),
    ((KC.RGB_HUD, KC.RGB_HUI, None),),
    ((KC.RGB_VAD, KC.RGB_VAI, None),),
    ((KC.NO, KC.NO, None),),
)

keyboard.modules = [layers, encoder_handler, macros]
keyboard.extensions = [media_keys, rgb]

def win_run(*commands):
    return KC.MACRO(Press(KC.LGUI), Tap(KC.R), Release(KC.LGUI),
                    Delay(200), *commands, Tap(KC.ENTER))

M_MEDIAPLAYER_CZ = win_run('ms-media-player:', Delay(100))
M_NOTEPAD_CZ = win_run('notepad', Delay(100), Delay(300), 'Ahoj z MakerClass!')

# Emoji makra pro TYPE vrstvu
EMOJI_SMILE = KC.MACRO('😊')
EMOJI_THUMBS = KC.MACRO('👍')
EMOJI_STAR = KC.MACRO('⭐')
EMOJI_HEART = KC.MACRO('❤️')
EMOJI_PARTY = KC.MACRO('🎉')
EMOJI_FIRE = KC.MACRO('🔥')

RGB_MODES = [
    AnimationModes.STATIC,
    AnimationModes.BREATHING,
    AnimationModes.RAINBOW,
    AnimationModes.BREATHING_RAINBOW,
    AnimationModes.KNIGHT,
    AnimationModes.SWIRL,
]

def rgb_mode_next(key, keyboard, *args):
    # Find current mode index
    current_index = 0
    for i, mode in enumerate(RGB_MODES):
        if mode == rgb.animation_mode or int(mode) == int(rgb.animation_mode):
            current_index = i
            break

    next_index = (current_index + 1) % len(RGB_MODES)
    rgb.animation_mode = RGB_MODES[next_index]

    if RGB_MODES[next_index] == AnimationModes.STATIC:
        rgb.user_mode_active = False
        if keyboard.active_layers:
            rgb.on_layer_change(keyboard.active_layers[0])
    else:
        rgb.user_mode_active = True
        rgb.hue, rgb.sat, rgb.val = 128, 255, 128

RGB_MOD = Key(on_press=rgb_mode_next)

# fmt:off
keyboard.keymap = [
    # BASE
    [
        KC.SPC,  KC.UP,  KC.LT(_LAYER_SWITCH, KC.ENT),  KC.LEFT,  KC.DOWN,  KC.RGHT,  KC.MUTE
    ],

    # MEDIA
    [
        M_MEDIAPLAYER_CZ,  KC.MSTP,  KC.LT(_LAYER_SWITCH, KC.NO),  KC.MPRV,  KC.MPLY,  KC.MNXT,  KC.MUTE
    ],

    # MACROS
    [
        KC.LALT(KC.TAB),  KC.LCTL(KC.C),  KC.LT(_LAYER_SWITCH, KC.PSCR),  KC.LCTL(KC.D),  KC.LCTL(KC.V),  M_NOTEPAD_CZ,  KC.MUTE
    ],

    # TYPE
    [
        EMOJI_SMILE,  EMOJI_THUMBS,  KC.LT(_LAYER_SWITCH, EMOJI_STAR),  EMOJI_HEART,  EMOJI_PARTY,  EMOJI_FIRE,  KC.RGB_TOG
    ],

    # UTILS
    [
        RGB_MOD,  KC.RGB_HUI,  KC.LT(_LAYER_SWITCH, KC.NO),  KC.RGB_TOG,  KC.RELOAD,  KC.RGB_SPI,  KC.NO
    ],

    # LAYER_SWITCH
    [
        KC.TO(_BASE),  KC.TO(_MEDIA),  KC.NO,  KC.TO(_MACROS),  KC.TO(_TYPE),  KC.TO(_UTILS),  KC.NO
    ]
]
# fmt:on

if __name__ == '__main__':
    keyboard.go()
