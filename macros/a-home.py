# Write your code here :-)
# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Home Desktop for Mac

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Home', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x33FFC0, 'Finder', [Keycode.COMMAND, 'n']),
        (0x03A826, 'Chrome', [Keycode.CONTROL, Keycode.OPTION, '2']),
        (0x000040, 'Zoom', [Keycode.CONTROL, Keycode.OPTION, '3']),
        # 2nd row ----------
        (0xFFC0CB, 'Code', [Keycode.CONTROL, Keycode.OPTION, '4']),
        (0x800080, 'Shell', [Keycode.CONTROL, Keycode.OPTION, '5']),
        (0x400000, 'Figma', [Keycode.CONTROL, Keycode.OPTION, '6']),
        # 3rd row ----------
        (0x00FF02, 'Spotify', [Keycode.CONTROL, Keycode.OPTION, '7']),
        (0xFFA500, 'Logic', [Keycode.CONTROL, Keycode.OPTION, '8']),
        (0x03A826, 'Stocks', [Keycode.CONTROL, Keycode.OPTION, '9']),
        # 4th row ----------
        (0x800080, 'Options', [Keycode.CONTROL, Keycode.OPTION, '[']),
        (0x000040, 'Mail', [Keycode.CONTROL, Keycode.OPTION, ']']),
        (0x00FF02, 'Messages', [Keycode.CONTROL, Keycode.OPTION, ';']),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, Keycode.OPTION, 'w'])
    ]
}
