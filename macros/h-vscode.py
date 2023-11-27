# Write your code here :-)
# MACROPAD Hotkeys example: VSCODE for Mac

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'VSCode', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x00FF02, 'New File', [Keycode.COMMAND, Keycode.CONTROL, Keycode.OPTION, 'n']),
        (0x000000, '', []),
        (0x00FF02, 'Comment +', [Keycode.COMMAND, '/']),
        # 2nd row ----------
        (0x800080, 'Terminal', [Keycode.CONTROL, '`']),
        (0x000000, '', []),
        (0x800080, 'Server', [Keycode.CONTROL, Keycode.ALT, 'l']),
        # 3rd row ----------
        (0x03A826, 'CMD PLT', [Keycode.COMMAND, Keycode.SHIFT, 'p']),
        (0x000000, '', []),
        (0x03A826, 'File Search', [Keycode.COMMAND, Keycode.SHIFT, 'f']),
        # 4th row ----------
        (0x400000, 'Sidebar', [Keycode.COMMAND, 'b']),
        (0x000000, '', []),
        (0x400000, 'DEL Line', [Keycode.COMMAND, Keycode.SHIFT, 'k']),
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'w']) # Close window/tab
    ]
}
