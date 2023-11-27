# Write your code here :-)
# Write your code here :-)
# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Chrome Tools for Mac

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Chrome Tools', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x00FF02, 'New W', [Keycode.COMMAND, 'n']),
        (0x800080, 'Incog', [Keycode.COMMAND, Keycode.SHIFT, 'n']),
        (0x400000, 'Zoom +', [Keycode.COMMAND, '+']),
        # 2nd row ----------
        (0x00FF02, 'New T', [Keycode.COMMAND, 't']),
        (0x800080, 'Redo T', [Keycode.COMMAND, Keycode.SHIFT, 't']),
        (0x400000, 'Zoom -', [Keycode.COMMAND, '-']),
        # 3rd row ----------
        (0x000040, '< Back', [Keycode.COMMAND, '[']),
        (0x000040, 'Fwd >', [Keycode.COMMAND, ']']),
        (0x03A826, 'Refresh', [Keycode.COMMAND, Keycode.SHIFT, 'r']),
        # 4th row ----------
        (0x00FF02, 'Copy', [Keycode.COMMAND, 'c']),
        (0x800000, 'Paste', [Keycode.COMMAND, 'v']),
        (0x800080, 'FPaste', [Keycode.COMMAND, Keycode.SHIFT, 'v']),
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'w']) # Close window/tab
    ]
}
