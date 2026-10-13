# volume_controller.py

import pyautogui

# Virtual volume value for HUD display
volume_level = 50


def volume_up():

    global volume_level

    pyautogui.press(
        "volumeup"
    )

    volume_level = min(
        volume_level + 2,
        100
    )


def volume_down():

    global volume_level

    pyautogui.press(
        "volumedown"
    )

    volume_level = max(
        volume_level - 2,
        0
    )


def get_volume():

    return volume_level