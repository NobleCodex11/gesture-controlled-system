# gesture_detector.py

import math


# --------------------------------
# Distance
# --------------------------------

def distance(x1, y1, x2, y2):

    return math.hypot(
        x2 - x1,
        y2 - y1
    )


# --------------------------------
# Finger Detection
# --------------------------------

def finger_up(tip, pip, landmarks):

    return (
        landmarks[tip].y <
        landmarks[pip].y
    )


def thumb_up(landmarks):

    return (
        landmarks[4].y <
        landmarks[3].y
    )


# --------------------------------
# Finger Count Gestures
# --------------------------------

def one_finger(landmarks):

    index = finger_up(8, 6, landmarks)
    middle = finger_up(12, 10, landmarks)
    ring = finger_up(16, 14, landmarks)
    pinky = finger_up(20, 18, landmarks)

    return (
        index
        and not middle
        and not ring
        and not pinky
    )


def two_finger(landmarks):

    index = finger_up(8, 6, landmarks)
    middle = finger_up(12, 10, landmarks)
    ring = finger_up(16, 14, landmarks)
    pinky = finger_up(20, 18, landmarks)

    return (
        index
        and middle
        and not ring
        and not pinky
    )


def three_finger(landmarks):

    index = finger_up(8, 6, landmarks)
    middle = finger_up(12, 10, landmarks)
    ring = finger_up(16, 14, landmarks)
    pinky = finger_up(20, 18, landmarks)

    return (
        index
        and middle
        and ring
        and not pinky
    )


def four_finger(landmarks):

    index = finger_up(8, 6, landmarks)
    middle = finger_up(12, 10, landmarks)
    ring = finger_up(16, 14, landmarks)
    pinky = finger_up(20, 18, landmarks)

    return (
        index
        and middle
        and ring
        and pinky
    )


def five_finger(landmarks):

    thumb = thumb_up(landmarks)

    index = finger_up(8, 6, landmarks)
    middle = finger_up(12, 10, landmarks)
    ring = finger_up(16, 14, landmarks)
    pinky = finger_up(20, 18, landmarks)

    return (
        thumb
        and index
        and middle
        and ring
        and pinky
    )

# --------------------------------
# keyboard Gesture
# --------------------------------

def keyboard_gesture(landmarks):

    thumb = thumb_up(landmarks)

    index = finger_up(8, 6, landmarks)

    middle = finger_up(12, 10, landmarks)

    ring = finger_up(16, 14, landmarks)

    pinky = finger_up(20, 18, landmarks)

    return (
        thumb
        and pinky
        and not index
        and not middle
        and not ring
    )




# --------------------------------
# Fist Gesture
# --------------------------------

def fist(landmarks):

    thumb = thumb_up(landmarks)

    index = finger_up(8, 6, landmarks)
    middle = finger_up(12, 10, landmarks)
    ring = finger_up(16, 14, landmarks)
    pinky = finger_up(20, 18, landmarks)

    return (
        not thumb
        and not index
        and not middle
        and not ring
        and not pinky
    )


# --------------------------------
# Orientation
# --------------------------------

def is_horizontal(
    x1,
    y1,
    x2,
    y2,
    threshold
):

    dx = abs(
        x2 - x1
    )

    dy = abs(
        y2 - y1
    )

    return (
        dx >
        dy + threshold
    )


def is_vertical(
    x1,
    y1,
    x2,
    y2,
    threshold
):

    dx = abs(
        x2 - x1
    )

    dy = abs(
        y2 - y1
    )

    return (
        dy >
        dx + threshold
    )