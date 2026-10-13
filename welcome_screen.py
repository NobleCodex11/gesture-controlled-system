import asyncio
import edge_tts
import tempfile
import os
from datetime import datetime
from playsound import playsound


def get_greeting():

    hour = datetime.now().hour

    if 5 <= hour < 12:
        return "Good morning sir.All systems ready. Gesture control activated."

    elif 12 <= hour < 17:
        return "Good afternoon sir.All systems ready. Gesture control activated."

    elif 17 <= hour < 21:
        return "Good evening sir.All systems ready. Gesture control activated."

    else:
        return "Welcome back sir.All systems ready. Gesture control activated."


async def speak_text(text):

    voice = "en-US-ChristopherNeural"

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp3"
    )

    temp_path = temp_file.name

    temp_file.close()

    communicate = edge_tts.Communicate(
        text,
        voice
    )

    await communicate.save(
        temp_path
    )

    playsound(temp_path)

    os.remove(temp_path)


def show_welcome():

    message = get_greeting()

    asyncio.run(
        speak_text(message)
    )