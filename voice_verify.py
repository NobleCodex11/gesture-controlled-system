from resemblyzer import VoiceEncoder, preprocess_wav
from pathlib import Path
import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np
import os

PROFILE_FOLDER = "profiles"

SAMPLE_RATE = 16000
DURATION = 2

encoder = VoiceEncoder()


def record_audio(filename):

    print(f"Recording {filename}...")

    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    wav.write(
        filename,
        SAMPLE_RATE,
        audio
    )

    print(f"Saved: {filename}")


def profile_exists():

    return os.path.exists(
        f"{PROFILE_FOLDER}/wakeup_0.wav"
    )


def register_voice():

    os.makedirs(
        PROFILE_FOLDER,
        exist_ok=True
    )

    phrases = [
        "wakeup",
        "goodnight"
    ]

    for phrase in phrases:

        for i in range(3):

            input(
                f"\nPress ENTER and say "
                f"'{phrase}' Sample {i+1}"
            )

            filename = (
                f"{PROFILE_FOLDER}/"
                f"{phrase}_{i}.wav"
            )

            record_audio(
                filename
            )

    print(
        "\nVoice Profile Saved"
    )


def get_embedding(file_path):

    wav_data = preprocess_wav(
        Path(file_path)
    )

    return encoder.embed_utterance(
        wav_data
    )


def verify_speaker():

    temp_file = (
        f"{PROFILE_FOLDER}/temp.wav"
    )

    print(
        "\nSay Wake Up"
    )

    record_audio(
        temp_file
    )

    test_embedding = get_embedding(
        temp_file
    )

    scores = []

    for i in range(3):

        reference = (
            f"{PROFILE_FOLDER}/"
            f"wakeup_{i}.wav"
        )

        ref_embedding = get_embedding(
            reference
        )

        similarity = np.inner(
            ref_embedding,
            test_embedding
        )

        scores.append(
            similarity
        )

    average = sum(scores) / len(scores)

    print(
        "\nSimilarity:",
        round(average, 3)
    )

    return average > 0.1