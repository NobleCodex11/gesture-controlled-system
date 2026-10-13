import tkinter as tk
import threading

privacy_mode = False
overlay_window = None


def create_overlay():

    global overlay_window

    overlay_window = tk.Tk()

    overlay_window.configure(bg="black")

    overlay_window.attributes("-fullscreen", True)

    overlay_window.attributes("-topmost", True)

    overlay_window.overrideredirect(True)

    overlay_window.mainloop()


def enable():

    global privacy_mode

    if privacy_mode:
        return

    privacy_mode = True

    threading.Thread(
        target=create_overlay,
        daemon=True
    ).start()

    print("PRIVACY ENABLED")


def disable():

    global privacy_mode
    global overlay_window

    privacy_mode = False

    if overlay_window is not None:

        overlay_window.after(
            0,
            overlay_window.destroy
        )

        overlay_window = None

    print("PRIVACY DISABLED")


def is_enabled():

    return privacy_mode


def draw_overlay(width, height):

    return None