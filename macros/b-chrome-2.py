# Write your code here :-)
# Write your code here :-)
# Write your code here :-)
# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Chrome web browser for Mac

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Chrome Pages', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x00FF02, 'Tab', [Keycode.COMMAND, 't']),
        (0xFFA500, 'Reddit', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                            'https://www.reddit.com\n']),
        (0x400000, 'Youtube', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                            'https://www.youtube.com\n']),
        # 2nd row ----------
        (0x000040, 'Outlook', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                            'https://outlook.office365.com/mail\n']),
        (0x03A826, 'OCal', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                            'https://outlook.office365.com/calendar/view/week\n']),
        (0x000040, 'Canva', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                            'https://www.canva.com\n']),                     # Scroll down
        # 3rd row ----------
        (0x800000, 'Drive', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                            'https://drive.google.com/drive/u/0/my-drive\n']),
        (0x00FF02, 'GCal', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                            'https://calendar.google.com/calendar/u/0/r\n']),
        (0x800080, 'Gmail', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                            'https://mail.google.com/mail/u/0/#inbox\n']),
        # 4th row ----------
        (0x00FF02, 'GPT', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                           'https://chat.openai.com\n']),   # Adafruit in new window
        (0x800080, 'GHUB', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                            'https://github.com/arnadeglenn\n']),   # Digi-Key in new window
        (0xFFA500, 'Odin', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                             'https://www.theodinproject.com\n']), # Hack-a-Day in new win
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'w']) # Close window/tab
    ]
}
