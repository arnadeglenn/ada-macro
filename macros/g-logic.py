# Write your code here :-)
# Write your code here :-)
# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Chrome Tools for Mac

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Logic', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x03A826, 'Split', [Keycode.COMMAND, 't']),
        (0x03A826, 'Join', ['j']),
        (0x03A826, 'KB MIDI', [Keycode.COMMAND, 'k']),
        # 2nd row ----------
        (0x03A826, 'Mixer', ['x']),
        (0x03A826, 'EQ', ['b']),
        (0x03A826, 'Editor', ['e']),
        # 3rd row ----------
        (0x400000, 'Record', ['r']),
        (0x03A826, 'Automate', ['a']),
        (0x400000, 'Stack', [Keycode.COMMAND, Keycode.SHIFT, 'd']),
        # 4th row ----------
        (0x00FF02, 'N-Audio', [Keycode.COMMAND, Keycode.OPTION, 'a']),
        (0x03A826, 'Bounce', [Keycode.COMMAND, 'b']),
        (0x00FF02, 'N-Instr', [Keycode.COMMAND, Keycode.OPTION, 's']),
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'w']) # Close window/tab
    ]
}
