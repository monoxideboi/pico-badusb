import usb_hid # type: ignore

import time

from adafruit_hid.keyboard import Keyboard # type: ignore
from adafruit_hid.keycode import Keycode # type: ignore

class Input:

    # hell
    keycodeMap = {
    'a': Keycode.A, 'b': Keycode.B, 'c': Keycode.C, 'd': Keycode.D, 'e': Keycode.E,
    'f': Keycode.F, 'g': Keycode.G, 'h': Keycode.H, 'i': Keycode.I, 'j': Keycode.J,
    'k': Keycode.K, 'l': Keycode.L, 'm': Keycode.M, 'n': Keycode.N, 'o': Keycode.O,
    'p': Keycode.P, 'q': Keycode.Q, 'r': Keycode.R, 's': Keycode.S, 't': Keycode.T,
    'u': Keycode.U, 'v': Keycode.V, 'w': Keycode.W, 'x': Keycode.X, 'y': Keycode.Y,
    'z': Keycode.Z, '1': Keycode.ONE, '2': Keycode.TWO, '3': Keycode.THREE,
    '4': Keycode.FOUR, '5': Keycode.FIVE, '6': Keycode.SIX, '7': Keycode.SEVEN,
    '8': Keycode.EIGHT, '9': Keycode.NINE, '0': Keycode.ZERO,
    ' ': Keycode.SPACE, '-': Keycode.MINUS, '=': Keycode.EQUALS,
    '[': Keycode.LEFT_BRACKET, ']': Keycode.RIGHT_BRACKET,
    '\\': Keycode.BACKSLASH, ';': Keycode.SEMICOLON, '\'': Keycode.QUOTE,
    '`': Keycode.GRAVE_ACCENT, ',': Keycode.COMMA, '.': Keycode.PERIOD,
    '/': Keycode.FORWARD_SLASH,
    '!': (Keycode.ONE, Keycode.SHIFT),  # SHIFT + 1
    '@': (Keycode.TWO, Keycode.SHIFT), # SHIFT + 2
    '#': (Keycode.THREE, Keycode.SHIFT), # SHIFT + 3
    '$': (Keycode.FOUR, Keycode.SHIFT), # SHIFT + 4
    '%': (Keycode.FIVE, Keycode.SHIFT), # SHIFT + 5
    '^': (Keycode.SIX, Keycode.SHIFT),  # SHIFT + 6
    '&': (Keycode.SEVEN, Keycode.SHIFT),  # SHIFT + 7
    '*': (Keycode.EIGHT, Keycode.SHIFT), # SHIFT + 8
    '(': (Keycode.NINE, Keycode.SHIFT),  # SHIFT + 9
    ')': (Keycode.ZERO, Keycode.SHIFT),  # SHIFT + 0
    '_': (Keycode.MINUS, Keycode.SHIFT), # SHIFT + MINUS
    '+': (Keycode.EQUALS, Keycode.SHIFT), # SHIFT + EQUALS
    '{': (Keycode.LEFT_BRACKET, Keycode.SHIFT),  # SHIFT + LEFT BRACKET
    '}': (Keycode.RIGHT_BRACKET, Keycode.SHIFT), # SHIFT + RIGHT BRACKET
    '|': (Keycode.BACKSLASH, Keycode.SHIFT), # SHIFT + BACKSLASH
    ':': (Keycode.SEMICOLON, Keycode.SHIFT), # SHIFT + SEMICOLON
    '"': (Keycode.QUOTE, Keycode.SHIFT), # SHIFT + QUOTE
    '<': (Keycode.COMMA, Keycode.SHIFT), # SHIFT + COMMA
    '>': (Keycode.PERIOD, Keycode.SHIFT), # SHIFT + PERIOD
    '?': (Keycode.FORWARD_SLASH, Keycode.SHIFT), # SHIFT + SLASH
    '~': (Keycode.GRAVE_ACCENT, Keycode.SHIFT),  # SHIFT + GRAVE ACCENT
    "UP": Keycode.UP_ARROW,
    "DOWN": Keycode.DOWN_ARROW,
    "LEFT": Keycode.LEFT_ARROW,
    "RIGHT": Keycode.RIGHT_ARROW,
    "PAGEUP": Keycode.PAGE_UP,
    "PAGEDOWN": Keycode.PAGE_DOWN,
    "HOME": Keycode.HOME,
    "END": Keycode.END,
    "INSERT": Keycode.INSERT,
    "DELETE": Keycode.DELETE,
    "BACKSPACE": Keycode.BACKSPACE,
    "TAB": Keycode.TAB,
    "SPACE": Keycode.SPACE,
    "ENTER": Keycode.ENTER,
    "ESCAPE": Keycode.ESCAPE,
    "PAUSE": Keycode.PAUSE,
    "PRINTSCREEN": Keycode.PRINT_SCREEN,
    "MENU": Keycode.APPLICATION,  # 'MENU' key is APPLICATION in Adafruit's library
    "F1": Keycode.F1,
    "F2": Keycode.F2,
    "F3": Keycode.F3,
    "F4": Keycode.F4,
    "F5": Keycode.F5,
    "F6": Keycode.F6,
    "F7": Keycode.F7,
    "F8": Keycode.F8,
    "F9": Keycode.F9,
    "F10": Keycode.F10,
    "F11": Keycode.F11,
    "F12": Keycode.F12,
    "SHIFT": Keycode.LEFT_SHIFT,
    "ALT": Keycode.LEFT_ALT,
    "ALTGR": Keycode.RIGHT_ALT,
    "CONTROL": Keycode.LEFT_CONTROL,
    "CTRL": Keycode.LEFT_CONTROL,  # Alias for CONTROL
    "GUI": Keycode.LEFT_GUI,
    "COMMAND": Keycode.LEFT_GUI,  # Alias for GUI
    "WINDOWS": Keycode.LEFT_GUI,  # Alias for GUI
    "CAPSLOCK": Keycode.CAPS_LOCK,
    "NUMLOCK": Keycode.KEYPAD_NUMLOCK,
    "SCROLLOCK": Keycode.SCROLL_LOCK,
}
    def pressKey(kbd, key):
        keycode = Input.keycodeMap.get(key)
        if type(keycode) == tuple:
            kbd.press(keycode[0], keycode[1])
        else:
            kbd.press(keycode)

    def inputKeycode(kbd, char, delay):
        print('char', char)
        isLower = True

        print (char.isupper())
        if char.isupper():
            isLower = False
            char = char.lower()

        print(char)
        keycode = Input.keycodeMap.get(char)
        print(keycode)

        isTuple = type(keycode) is tuple
        print(isTuple)
        if isTuple:
            kbd.send(keycode[0], keycode[1])
        elif isLower:
            kbd.send(keycode)
        else:
            kbd.send(keycode, Keycode.SHIFT)
        time.sleep(delay/1000)
        
        
        