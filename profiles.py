from config import PLATFORM
from adafruit_hid.keycode import Keycode

platform_keys = {
    "windows": Keycode.CONTROL,  # Windows uses CTRL for some hotkeys
    "linux": Keycode.CONTROL,  # Linux uses CTRL for some hotkeys
    "mac": Keycode.COMMAND  # MacOS uses CMD for some hotkeys
}

platform_key = platform_keys[PLATFORM]

profiles = {
    "mute": {
        'name': 'Mute',
        'color': (255, 0, 0)
    },
    "zoom": {
        'name': 'Zoom',
        'keycode': (Keycode.ALT, Keycode.A),
        'color': (0, 0, 205)
    },
    "teams": {
        'name': 'MS Teams',
        'keycode': (platform_key, Keycode.SHIFT, Keycode.M),
        'color': (120, 0, 255)
    },
    "meet": {
        'name': 'Google Meet',
        'keycode': (platform_key, Keycode.D),
        'color': (12, 132, 0)
    },
    "slack": {
        'name': 'Slack',
        'keycode': (Keycode.M),
        'color': (200, 80, 0)
    },
    "jitsi": {
        'name': 'Jitsi',
        'keycode': (Keycode.M),
        'color': (65, 200, 190)
    },
    "system": {
        'name': 'System hotkey',
        'keycode': (Keycode.GUI, Keycode.SHIFT, Keycode.A),  # Enable in host system
        'color': (255, 255, 255)
    }

}