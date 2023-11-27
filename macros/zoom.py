# MACROPAD Hotkeys: Zoom for Mac

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    "name": "Zoom",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        # audio toggle
        (0x004000, "Mute", [Keycode.SHIFT, Keycode.COMMAND, "a"]),
        (0x400000, "Camera", [Keycode.SHIFT, Keycode.COMMAND, "v"]),
        (0x004000, "Share", [Keycode.SHIFT, Keycode.COMMAND, "s"]),  # video toggle
        # 2nd row ----------
        (0x202000, "Users", [Keycode.COMMAND, "u"]),
        (0x004000, "Chat", [Keycode.SHIFT, Keycode.COMMAND, "h"]),
        (0x202000, "Hand", [Keycode.ALT, "y"]),
        # 3rd row ----------
        # view toggle (gallery/speaker)
        (0x03A826, "Link", [Keycode.SHIFT, Keycode.COMMAND, "i"]),
        (0x400000, "Record", [Keycode.SHIFT, Keycode.COMMAND, "r"]),
        (0x03A826, "Gallery", [Keycode.SHIFT, Keycode.COMMAND, "w"]),  # participants toggle
        # 4th row ----------
        (0x202000, "MinMax", [Keycode.COMMAND, "m"]),
        (0x004000, "Full", [Keycode.SHIFT, Keycode.COMMAND, "f"]),  # raise/lower hand
        (0x400000, "Leave", [Keycode.COMMAND, "w"]),
        # Encoder button ---
        (0x000000, "", [Keycode.COMMAND, "w"]),  # close window
    ],
}
