import speech_recognition as sr
import threading
import system_state

from voice_verify import verify_speaker
from privacy_mode import enable, disable, is_enabled
from welcome_screen import show_welcome


listener_running = False
import time

last_command_time = 0

COMMAND_COOLDOWN = 5


def process_command(command):
    global last_command_time

    current_time = time.time()

    if (
        current_time -
        last_command_time
    ) < COMMAND_COOLDOWN:

        return

    last_command_time = current_time

    command = command.lower()

    if (
       "good night" in command
        or
       "goodnight" in command
   ):

        print("Good Night Detected")

        if verify_speaker():

            print("Voice Verified")

            enable()
            system_state.camera_enabled = False

        else:

            print("Voice Verification Failed")

    elif "wake up" in command:

        print("Wake Up Detected")

        if verify_speaker():

            print("Voice Verified")

            disable()
            system_state.camera_enabled = True

            show_welcome()

        else:

            print("Voice Verification Failed")


def listen_loop():

    recognizer = sr.Recognizer()

    microphone = sr.Microphone()

    while True:

        try:

            with microphone as source:

                recognizer.adjust_for_ambient_noise(
                    source,
                    duration=0.5
                )

                print("Listening...")

                audio = recognizer.listen(
                    source,
                    phrase_time_limit=3
                )

            command = recognizer.recognize_google(
                audio
            )

            print(
                "Heard:",
                command
            )

            process_command(
                command
            )

        except Exception:
            pass


def start_listener():

    global listener_running

    if listener_running:
        return

    listener_running = True

    threading.Thread(
        target=listen_loop,
        daemon=True
    ).start()