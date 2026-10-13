# brightness_controller.py

import screen_brightness_control as sbc

try:

    brightness_level = sbc.get_brightness()[0]

except:

    brightness_level = 50


def brightness_up():

    global brightness_level

    brightness_level = min(
        brightness_level + 2,
        100
    )

    try:

        sbc.set_brightness(
            brightness_level
        )

    except:

        pass


def brightness_down():

    global brightness_level

    brightness_level = max(
        brightness_level - 2,
        0
    )

    try:

        sbc.set_brightness(
            brightness_level
        )

    except:

        pass


def get_brightness():

    return brightness_level