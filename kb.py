import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.keypad import KeysScanner


class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        super().__init__()

        # Direct pin matrix - každé tlačítko má vlastní GPIO pin (bez diod)
        # Tlačítka mapování: SPACE, UP, ENTER, LEFT, DOWN, RIGHT, ENCODER_SW
        # GPIO piny:         GP19,  GP21, GP27,  GP20, GP22,  GP26,   GP15
        self.matrix = KeysScanner(
            pins=[
                board.GP19,  # Button 0: SPACE
                board.GP21,  # Button 1: UP
                board.GP27,  # Button 2: ENTER (s LT layer switch)
                board.GP20,  # Button 3: LEFT
                board.GP22,  # Button 4: DOWN
                board.GP26,  # Button 5: RIGHT
                board.GP15,  # Button 6: ENCODER_SW (MUTE)
            ],
            value_when_pressed=False,  # Pullup rezistory, LOW při stisku
            pull=True,  # Povolit pull-up
            interval=0.005,  # 5ms debounce
