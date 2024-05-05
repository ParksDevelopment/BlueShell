print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
encoder_handler = EncoderHandler()
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.LED import LED
from kmk.extensions.led import AnimationModes
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys


keyboard = KMKKeyboard()
led = LED(led_pin=[board.GP25],
    brightness=100,
    brightness_step=5,
    brightness_limit=100,
)
keyboard.extensions.append(led)
keyboard.extensions.append(MediaKeys())
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.modules = [encoder_handler]
keyboard.modules.append(Layers())
keyboard.modules.append(MouseKeys())

keyboard.col_pins = (board.GP0,board.GP1,board.GP2,board.GP3,board.GP4,board.GP5,board.GP6,board.GP7,board.GP8,board.GP9,board.GP10,board.GP11,board.GP12,board.GP13,board.GP14,board.GP15,board.GP16,)
keyboard.row_pins = (board.GP17,board.GP18,board.GP19,board.GP20,board.GP21,board.GP22,)

encoder_handler.pins = ((board.GP23, board.GP24, None,),)

keyboard.keymap = [
    [
    KC.ESCAPE,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,KC.F6,KC.F7,KC.F8,KC.F9,KC.F10,KC.F11,KC.F12,KC.NO,KC.NO,KC.NO,KC.NO,
    KC.GRAVE,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,KC.N0,KC.MINUS,KC.EQUAL,KC.BKDL,KC.INSERT,KC.HOME,KC.PGUP,
    KC.TAB,KC.Q,KC.W,KC.E,KC.R,KC.T,KC.Y,KC.U,KC.I,KC.O,KC.P,KC.LBRACKET,KC.RBRACKET,KC.BSLASH,KC.DELETE,KC.END,KC.PGDOWN,
    KC.CAPSLOCK,KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,KC.SCOLON,KC.QUOTE,KC.ENTER,KC.NO,KC.NO,KC.NO,KC.NO,
    KC.LSHIFT,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.N,KC.M,KC.COMMA,KC.DOT,KC.SLASH,KC.RSHIFT,KC.UP,KC.NO,KC.NO,KC.NO,KC.NO,
    KC.LCTRL,KC.LGUI,KC.LALT,KC.SPACE,KC.RALT,KC.MO(1),KC.APPLICATION,KC.RCTRL,KC.LEFT,KC.DOWN,KC.RIGHT,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.MUTE,
    ],
    [
    KC.ESCAPE,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,KC.F6,KC.F7,KC.F8,KC.F9,KC.F10,KC.F11,KC.F12,KC.NO,KC.NO,KC.NO,KC.NO,
    KC.GRAVE,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,KC.N0,KC.MINUS,KC.EQUAL,KC.BKDL,KC.INSERT,KC.HOME,KC.PGUP,
    KC.TAB,KC.Q,KC.W,KC.E,KC.R,KC.T,KC.Y,KC.U,KC.I,KC.O,KC.P,KC.LBRACKET,KC.RBRACKET,KC.BSLASH,KC.DELETE,KC.END,KC.PGDOWN,
    KC.CAPSLOCK,KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,KC.SCOLON,KC.QUOTE,KC.ENTER,KC.NO,KC.NO,KC.NO,KC.NO,
    KC.LSHIFT,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.N,KC.M,KC.MB_LMB,KC.MB_RMB,KC.SLASH,KC.RSHIFT,KC.MS_UP,KC.NO,KC.NO,KC.NO,KC.NO,
    KC.LCTRL,KC.LGUI,KC.LALT,KC.SPACE,KC.RALT,KC.MO(1),KC.APPLICATION,KC.RCTRL,KC.MS_LEFT,KC.MS_DOWN,KC.MS_RIGHT,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.LED_SET(50),
    ]
]

encoder_handler.map = [ ((KC.VOLU, KC.VOLD, KC.NO),),
                        ((KC.LED_INC(), KC.LED_DEC(), KC.NO),),
]

if __name__ == '__main__':
    keyboard.go()
