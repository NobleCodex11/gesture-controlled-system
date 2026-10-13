import os
import pickle
import speech_recognition as sr
import pyttsx3

PROFILE_FILE = "profiles/voice_profile.pkl"

engine = pyttsx3.init()

def speak(text):

    print(text)

    engine.say(text)

    engine.runAndWait()


def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        print("Listening...")

        audio = recognizer.listen(source)

    try:

        text = recognizer.recognize_google(
            audio
        ).lower()

        print("You said:", text)

        return text

    except:

        return ""


def register_voice():

    print(
        "No Voice Profile Found"
    )

    print(
        "Voice Registration Started"
    )

    samples = {
        "wake up": [],
        "good night": []
    }

    for phrase in samples:

        for i in range(3):

            speak(
                f"Please say {phrase}"
            )

            text = ""

            while phrase not in text:

                text = listen()

            samples[phrase].append(
                phrase
            )

            speak(
                f"Sample {i+1} captured"
            )

    os.makedirs(
        "profiles",
        exist_ok=True
    )

    with open(
        PROFILE_FILE,
        "wb"
    ) as file:

        pickle.dump(
            samples,
            file
        )

    speak(
        "Voice profile saved"
    )


def load_profile():

    if not os.path.exists(
        PROFILE_FILE
    ):

        register_voice()

    with open(
        PROFILE_FILE,
        "rb"
    ) as file:

        return pickle.load(file)


def verify_command(command):

    profile = load_profile()

    if command in profile:

        return True

    return False