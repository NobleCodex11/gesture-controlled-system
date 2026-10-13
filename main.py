import cv2
import mediapipe as mp
import time
import pyautogui
import math
import numpy as np
import keyboard
from plyer import notification
import system_state

from gesture_detector import (
    distance,
    three_finger,
    five_finger,
    four_finger,
    two_finger,
    fist,
    keyboard_gesture,
    is_horizontal,
    is_vertical
)

from volume_controller import (
    volume_up,
    volume_down,
    get_volume
)

from brightness_controller import (
    brightness_up,
    brightness_down,
    get_brightness
)

from privacy_mode import (
    enable,
    disable,
    is_enabled,
    draw_overlay
)

from voice_listener import start_listener

from air_keyboard import (
    start_keyboard,
    update_cursor,
    hide_keyboard,
    show_keyboard
)


from config import *

# --------------------------------
# CAMERA
# --------------------------------

webcam = cv2.VideoCapture(0)
start_listener()



webcam.set(
    cv2.CAP_PROP_FRAME_WIDTH,
    CAMERA_WIDTH
)

webcam.set(
    cv2.CAP_PROP_FRAME_HEIGHT,
    CAMERA_HEIGHT
)

# --------------------------------
# WINDOW
# --------------------------------

#cv2.namedWindow(
#    WINDOW_NAME,
 #   cv2.WINDOW_NORMAL
#)

#cv2.setWindowProperty(
#    WINDOW_NAME,
#    cv2.WND_PROP_FULLSCREEN,
#   cv2.WINDOW_FULLSCREEN
#)

# --------------------------------
# MEDIAPIPE
# --------------------------------

mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

draw = mp.solutions.drawing_utils

# --------------------------------
# VARIABLES
# --------------------------------

last_action_time = 0

privacy_start = None
privacy_lost_time = None

screenshot_start = None
screenshot_lost_time = None

unlock_start = None
unlock_lost_time = None

mode = "READY"
system_locked = False

smoothed_distance = None
# Mouse Mode
mouse_mode = False
mouse_mode_start = None
mouse_exit_start = None


#keyboard mode

keyboard_mode = False
keyboard_mode_start = None
keyboard_exit_start = None

keyboard_window_started = False


KEYBOARD_ROWS = [
    "QWERTYUIOP",
    "ASDFGHJKL",
    "ZXCVBNM"
]

SPECIAL_KEYS = [
    "SPACE",
    "BACK",
    "ENTER"
]

selected_key = None
key_pressed = False




screen_width, screen_height = pyautogui.size()

prev_x = 0
prev_y = 0

last_click_time = 0
CLICK_COOLDOWN = 0.5

dragging = False
drag_start = None

left_pinch_active = False
right_pinch_active = False
click_candidate = False

SMOOTHING = 8

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=3
    )

# --------------------------------
# HUD BAR
# --------------------------------

def draw_bar(
    frame,
    label,
    value,
    x,
    y
):

    cv2.putText(
        frame,
        f"{label}: {value}%",
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255,255,255),
        2
    )

    cv2.rectangle(
        frame,
        (x, y),
        (x + 250, y + 25),
        (255,255,255),
        2
    )

    fill = int(
        (value / 100) * 250
    )

    cv2.rectangle(
        frame,
        (x, y),
        (x + fill, y + 25),
        (0,255,0),
        -1
    )
    

# --------------------------------
# MAIN LOOP
# --------------------------------

while True:

    if not system_state.camera_enabled:

        if webcam.isOpened():
            webcam.release()

        cv2.waitKey(1)

        continue
    if not webcam.isOpened():

        webcam = cv2.VideoCapture(0)

    success, frame = webcam.read()




    if not success:
        break

    frame = cv2.flip(
        frame,
        1
    )

    h, w, _ = frame.shape

    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    result = hands.process(rgb)

    current_time = time.time()
    mode = "READY"

    # ----------------------------
    # HAND FOUND
    # ----------------------------

    if result.multi_hand_landmarks:

        hand = result.multi_hand_landmarks[0]

        landmarks = hand.landmark
        gesture_mode = False


        #mouse mode



        if not mouse_mode:
            if two_finger(
                landmarks
            ):
                if mouse_mode_start is None:

                    mouse_mode_start = current_time
                elif current_time - mouse_mode_start > 2:
                    mouse_mode = True
                    show_notification("Mouse Mode Activated", "You can now control the mouse with your hand gestures.")
                    mouse_mode_start = None
            else:
                mouse_mode_start = None
        else:
            if five_finger(
                landmarks
            ):
                print("five fingers detected exiting mouse mode")
                if mouse_exit_start is None:
                    mouse_exit_start = current_time
                elif current_time - mouse_exit_start > 2:
                    mouse_mode = False
                    show_notification("Mouse Mode Deactivated", "You have exited mouse mode.")
                    mouse_exit_start = None
            else:
                mouse_exit_start = None

        #keyboard mode

        if not keyboard_mode and not mouse_mode:

            if keyboard_gesture(
                landmarks
            ):
                print("KEYBOARD GESTURE DETECTED")

                if keyboard_mode_start is None:

                    keyboard_mode_start = current_time

                elif (
                    current_time -
                    keyboard_mode_start
                ) > 2:

                    keyboard_mode = True


                    if not keyboard_window_started:

                        start_keyboard()

                        keyboard_window_started = True
                    
                    show_keyboard()





                    show_notification(
                        "Keyboard Mode",
                        "Enabled"
                    )

                    keyboard_mode_start = None

            else:

                keyboard_mode_start = None

        #exit keyboard mode

        if keyboard_mode:



            index_tip = landmarks[8]
            middle_tip = landmarks[12]

            cursor_x = np.interp(
                index_tip.x,
                (0.0, 1.0),
                (0.0, 1.0)
            )

            cursor_y = np.interp(
                index_tip.y,
                (0.0, 1.0),
                (0.0, 1.0)
            )

            index_middle = distance(
                int(index_tip.x * w),
                int(index_tip.y * h),
                int(middle_tip.x * w),
                int(middle_tip.y * h)
            )

            click_state = (
                index_middle < 25
            )

            update_cursor(
                cursor_x,
                cursor_y,
                click_state
            )
            
            






            if five_finger(landmarks):

                if keyboard_exit_start is None:

                    keyboard_exit_start = current_time

                elif (
                    current_time -
                    keyboard_exit_start
                ) > 2:

                    keyboard_mode = False

                    hide_keyboard()

                    keyboard_window_started = False

                    keyboard_exit_start = None

            else:

                keyboard_exit_start = None


            cv2.waitKey(1)

            continue

            
















        thumb = landmarks[4]
        index = landmarks[8]

        x1 = int(
            index.x * w
        )

        y1 = int(
            index.y * h
        )

        x2 = int(
            thumb.x * w
        )

        y2 = int(
            thumb.y * h
        )

        hand_distance = int(
            distance(
                x1,
                y1,
                x2,
                y2
            )
        )

        if smoothed_distance is None:

            smoothed_distance = hand_distance
        else:

            smoothed_distance = int(
                0.7 * smoothed_distance
                +
                0.3 * hand_distance
            )
        hand_distance = smoothed_distance

        horizontal = is_horizontal(
            x1,
            y1,
            x2,
            y2,
            ORIENTATION_THRESHOLD
        )

        vertical = is_vertical(
            x1,
            y1,
            x2,
            y2,
            ORIENTATION_THRESHOLD
        )

        dx = abs(
            x2 - x1
        )
        dy = abs(
            y2 - y1
        )



        # ----------------------------
        # PRIVACY MODE OFF
        # ----------------------------

        if is_enabled():

            if five_finger(
                landmarks
            ):
                unlock_lost_time = None
                gesture_mode = True

                if unlock_start is None:

                    unlock_start = current_time

                hold_time = (
                    current_time -
                    unlock_start
                )

                if (
                    hold_time >=
                    UNLOCK_HOLD_TIME
                ):

                    disable()

                    mode = (
                        "PRIVACY OFF"
                    )

                    unlock_start = None

            else:

                if unlock_start is not None:

                    if unlock_lost_time is None:

                        unlock_lost_time = current_time

                    elif (
                        current_time -
                        unlock_lost_time
                    ) > 0.5:

                        unlock_start = None
                        unlock_lost_time = None

        # ----------------------------
        # PRIVACY MODE ON
        # ----------------------------

        else:

            if three_finger(
                landmarks
            ):
                gesture_mode = True

                privacy_lost_time = None

                if privacy_start is None:

                    privacy_start = current_time

                hold_time = (
                    current_time -
                    privacy_start
                )

                mode = (
                    f"PRIVACY IN "
                    f"{int(max(0,
                    PRIVACY_HOLD_TIME -
                    hold_time))}"
                )

                if (
                    hold_time >=
                    PRIVACY_HOLD_TIME
                ):

                    enable()

                    mode = (
                        "PRIVACY ON"
                    )

                    privacy_start = None

            else:

                if privacy_start is not None:

                    if privacy_lost_time is None:

                        privacy_lost_time = current_time

                    elif (
                        current_time -
                        privacy_lost_time
                    ) > 0.5:

                        privacy_start = None
                        privacy_lost_time = None

























        # ----------------------------
            # MOUSE MODE
        # ----------------------------


        if mouse_mode:

           mode = "MOUSE MODE"

           index_tip = landmarks[8]

           cursor_x = np.interp(
              index_tip.x,
              (0.2, 0.8),
              (0, screen_width)
           )

           cursor_y = np.interp(
                index_tip.y,
                (0.2, 0.8),
                (0, screen_height)
           ) 

           curr_x = prev_x + (cursor_x - prev_x) / SMOOTHING
           curr_y = prev_y + (cursor_y - prev_y) / SMOOTHING

           pyautogui.moveTo(curr_x, curr_y)

           prev_x = curr_x
           prev_y = curr_y

           thumb_tip = landmarks[4]
           middle_tip = landmarks[12]

           thumb_index = distance(
              int(thumb_tip.x * w),
              int(thumb_tip.y * h),
              int(index_tip.x * w),
              int(index_tip.y * h)
            )

           thumb_middle = distance(
             int(thumb_tip.x * w),
             int(thumb_tip.y * h),
             int(middle_tip.x * w),
             int(middle_tip.y * h)
          )

           if thumb_index < 35:

                if drag_start is None:

                    drag_start = current_time
                    click_candidate = True

                elif (
                    current_time - drag_start > 0.5
                    and not dragging
                ):

                    pyautogui.mouseDown()

                    dragging = True
                    click_candidate = False

           else:
                
                if click_candidate and not dragging:

                    pyautogui.click()
                click_candidate = False

                drag_start = None

                if dragging:

                    pyautogui.mouseUp()

                    dragging = False

                elif (
                      thumb_middle < 35 and
                      current_time - last_click_time > CLICK_COOLDOWN
                    ):

                     pyautogui.rightClick()
                     last_click_time = current_time



        # ----------------------------
        # CONTROLS
        # ----------------------------

        if (
            not mouse_mode
            and not gesture_mode
            and not is_enabled()
            and
            (
                current_time -
                last_action_time
            )
            >
            CONTROL_COOLDOWN
        ):
            print("control active")

            # ------------------------
            # VOLUME
            # ------------------------

            if (
                horizontal
                and hand_distance < CONTROL_MAX_DISTANCE
            ):

                if (
                    hand_distance >
                    DISTANCE_OPEN
                ):
                    print("Volume Up", hand_distance)

                    volume_up()

                    mode = (
                        "VOLUME UP"
                    )

                    last_action_time = (
                        current_time
                    )

                elif (
                    hand_distance <
                    DISTANCE_CLOSE
                ):
                    print("Volume Down", hand_distance)

                    volume_down()

                    mode = (
                        "VOLUME DOWN"
                    )

                    last_action_time = (
                        current_time
                    )

            # ------------------------
            # BRIGHTNESS
            # ------------------------

            elif (
                vertical
                and hand_distance < CONTROL_MAX_DISTANCE
         ):

                if (
                    hand_distance >
                    DISTANCE_OPEN
                ):
                    print("Brightness Up", hand_distance)

                    brightness_up()

                    mode = (
                        "BRIGHTNESS UP"
                    )

                    last_action_time = (
                        current_time
                    )

                elif (
                    hand_distance <
                    DISTANCE_CLOSE
                ):
                    print("Brightness Down", hand_distance)

                    brightness_down()

                    mode = (
                        "BRIGHTNESS DOWN"
                    )

                    last_action_time = (
                        current_time
                    )

        # ----------------------------
        # DRAW HUD
        # ----------------------------

        if not is_enabled():


            if four_finger(
                landmarks
            ):
                gesture_mode = True
                screenshot_lost_time = None
                if screenshot_start is None:

                    screenshot_start = current_time
                hold_time = (
                    current_time - screenshot_start
                )
                mode = f"SCREENSHOT {int(max(0, 2 - hold_time))}"
                if hold_time >= 2:
                    filename = ( f"screenshot_"f"{int(time.time())}.png"
                )
                    pyautogui.screenshot(
                        filename
                   )

                    mode = "SCREENSHOT Saved"
                    show_notification("Screenshot Taken", f"Your screenshot has been saved as {filename}.") 

                    screenshot_start = None
            else:

                if screenshot_start is not None:

                    if screenshot_lost_time is None:

                        screenshot_lost_time = current_time

                    elif (
                        current_time -
                        screenshot_lost_time
                    ) > 0.5:

                        screenshot_start = None
                        screenshot_lost_time = None





            draw.draw_landmarks(
                frame,
                hand,
                mp_hands.HAND_CONNECTIONS
            )

            cv2.circle(
                frame,
                (x1, y1),
                10,
                (0,255,255),
                -1
            )

            cv2.circle(
                frame,
                (x2, y2),
                10,
                (255,0,255),
                -1
            )

            cv2.line(
                frame,
                (x1, y1),
                (x2, y2),
                (0,255,0),
                3
            )

            display_mode =(f"MOUSE | {mode}" if mouse_mode else mode)

            cv2.putText(
                frame,
                display_mode,
                (20,40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,0),
                2
            )

            cv2.putText(
                frame,
                f"DIST:{hand_distance}",
                (20,80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255,255,255),
                2
            )

            draw_bar(
                frame,
                "Volume",
                get_volume(),
                20,
                130
            )

            draw_bar(
                frame,
                "Brightness",
                get_brightness(),
                20,
                210
            )

           

            cv2.putText(
                frame,
                f"DX:{dx} DY:{dy}",
                (20,300),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0,255,255),
                2
            )

            cv2.putText(
                frame,
                f"H:{horizontal} V:{vertical}",
                (20,340),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0,255,255),
                2
            )

    else:

        privacy_start = None
        privacy_lost_time = None

        unlock_start = None
        unlock_lost_time = None

        smoothed_distance = None
        prev_x = 0
        prev_y = 0

    # ----------------------------
    # DISPLAY
    # ----------------------------
    if SHOW_CAMERA:
        pass
        
       # if is_enabled():

          #  black_screen = draw_overlay(
           #     w,
           #     h
           # )

           # cv2.imshow(
           #     WINDOW_NAME,
          #      black_screen
          #  )

      #  else:

       #     cv2.imshow(
         #       WINDOW_NAME,
         #       frame
         #   )

    # ----------------------------
    # EXIT
    # ----------------------------
    if SHOW_CAMERA:
        key = cv2.waitKey(1)

        if key == 27:
            break

        if key & 0xFF == ord("q"):
            break

# --------------------------------
# CLEANUP
# --------------------------------

webcam.release()

cv2.destroyAllWindows()