import tkinter as tk
import keyboard
import threading
import time

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 320

cursor_x = 0
cursor_y = 0

click_state = False
last_click = False

last_activity = time.time()

root = None
canvas = None

hover_key = None

keys = []

KEYBOARD_LAYOUT = [
    ["Q","W","E","R","T","Y","U","I","O","P"],
    ["A","S","D","F","G","H","J","K","L"],
    ["Z","X","C","V","B","N","M"]
]

SPECIAL = [
    "SPACE",
    "BACK",
    "ENTER"
]


def create_keyboard():

    global root
    global canvas

    root = tk.Tk()

    root.overrideredirect(True)

    root.attributes("-topmost", True)

    root.configure(bg="black")

    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()

    x = (screen_w - WINDOW_WIDTH) // 2
    y = screen_h - WINDOW_HEIGHT - 50

    root.geometry(
        f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}"
    )

    canvas = tk.Canvas(
        root,
        width=WINDOW_WIDTH,
        height=WINDOW_HEIGHT,
        bg="#101010",
        highlightthickness=0
    )

    canvas.pack()

    build_keys()

    

    update_ui()

    root.mainloop()


def build_keys():

    global keys

    keys.clear()

    start_y = 40

    key_w = 70
    key_h = 55

    row_gap = 20
    col_gap = 10

    for row_i, row in enumerate(KEYBOARD_LAYOUT):

        y = start_y + row_i * (key_h + row_gap)

        row_width = len(row) * (key_w + col_gap)

        start_x = (
            WINDOW_WIDTH - row_width
        ) // 2

        for col_i, key in enumerate(row):

            x = start_x + col_i * (
                key_w + col_gap
            )

            keys.append(
                {
                    "label": key,
                    "x": x,
                    "y": y,
                    "w": key_w,
                    "h": key_h
                }
            )

    special_y = 250

    special_positions = [
        ("SPACE", 200, 220),
        ("BACK", 450, 180),
        ("ENTER", 670, 180)
    ]

    for label, x, width in special_positions:

        keys.append(
            {
                "label": label,
                "x": x,
                "y": special_y,
                "w": width,
                "h": 55
            }
        )


def press_key(key):

    if key == "SPACE":

        keyboard.press_and_release(
            "space"
        )

    elif key == "BACK":

        keyboard.press_and_release(
            "backspace"
        )

    elif key == "ENTER":

        keyboard.press_and_release(
            "enter"
        )

    else:

        keyboard.write(key)


def update_ui():

    global hover_key
    global last_click
    global last_activity

    if root is None:
        return

    canvas.delete("all")

    local_x = int(
        cursor_x * WINDOW_WIDTH
    )

    local_y = int(
        cursor_y * WINDOW_HEIGHT
    )

    hover_key = None

    for key in keys:

        x = key["x"]
        y = key["y"]
        w = key["w"]
        h = key["h"]

        fill = "#101010"

        if (
            x < local_x < x + w
            and
            y < local_y < y + h
        ):

            hover_key = key

            fill = "#00bfff"

        canvas.create_rectangle(
            x,
            y,
            x + w,
            y + h,
            outline="white",
            width=2,
            fill=fill
        )

        canvas.create_text(
            x + w/2,
            y + h/2,
            text=key["label"],
            fill="white",
            font=("Consolas",16,"bold")
        )

    canvas.create_oval(
        local_x - 12,
        local_y - 12,
        local_x + 12,
        local_y + 12,
        outline="#00ffff",
        width=3
    )

    canvas.create_oval(
        local_x - 3,
        local_y - 3,
        local_x + 3,
        local_y + 3,
        fill="#00ffff",
        outline="#00ffff"
    )

    if (
        hover_key is not None
        and
        click_state
        and
        not last_click
    ):

        press_key(
            hover_key["label"]
        )

        last_activity = time.time()

    last_click = click_state

    root.after(
        16,
        update_ui
    )


def start_keyboard():

    threading.Thread(
        target=create_keyboard,
        daemon=True
    ).start()


def update_cursor(
    x,
    y,
    click
):

    global cursor_x
    global cursor_y
    global click_state

    cursor_x = x
    cursor_y = y

    click_state = click



def hide_keyboard():

    global root

    if root is not None:

        root.geometry("1x1+0+0")


def show_keyboard():

    global root

    if root is not None:

        screen_w = root.winfo_screenwidth()
        screen_h = root.winfo_screenheight()

        x = (screen_w - WINDOW_WIDTH) // 2
        y = screen_h - WINDOW_HEIGHT - 50

        root.geometry(
            f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}"
        )