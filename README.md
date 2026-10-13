# Windows Hand Gesture Control System

A Python-based, real-time hand gesture and voice-controlled system for Windows that makes computer interaction easier through computer vision, gesture recognition, and voice processing.

The application uses a webcam to detect hand movements and translate predefined gestures into computer operations. It also includes voice-related modules for voice interaction and verification.

The system is designed to provide touch-free interaction with a computer using commonly available hardware.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technology Stack](#technology-stack)
4. [System Requirements](#system-requirements)
5. [Project Structure](#project-structure)
6. [Installation](#installation)
7. [Voice Profile Setup](#voice-profile-setup)
8. [How to Run the Application](#how-to-run-the-application)
9. [Gesture Controls](#gesture-controls)
10. [Voice Features](#voice-features)
11. [Testing Individual Modules](#testing-individual-modules)
12. [Troubleshooting](#troubleshooting)
13. [Privacy and Security](#privacy-and-security)
14. [Limitations](#limitations)
15. [Future Enhancements](#future-enhancements)
16. [License](#license)

---

## 1. Project Overview

The Windows Hand Gesture Control System is a computer vision-based application that allows users to interact with their computers using hand gestures.

Traditional computer interaction depends on physical input devices such as keyboards, mice, and buttons. This project explores an alternative approach using a webcam and hand landmark detection.

The system processes webcam frames using OpenCV and MediaPipe. It identifies hand landmarks, analyzes finger positions, recognizes predefined gestures, and executes the corresponding operations.

The project also contains voice-related modules for voice input and verification.

### Working Principle

The system follows this processing pipeline:

Webcam Input
    |
    v
OpenCV Video Processing
    |
    v
MediaPipe Hand Landmark Detection
    |
    v
Gesture Recognition
    |
    v
Gesture-to-Action Mapping
    |
    v
Windows System Operation

The voice subsystem uses microphone input and the project's voice processing and verification modules.

Depending on the configured functionality, recognized commands or verified voice input can be used to interact with the application.

---

## 2. Features

### Hand Gesture Recognition

- Real-time hand detection using a webcam.
- Hand landmark tracking using MediaPipe.
- Recognition of predefined finger configurations.
- Gesture-based computer interaction.

### System Controls

- Windows system volume adjustment.
- Screen brightness adjustment.
- Screenshot capture.
- Privacy Mode activation and deactivation.

### Voice-Related Features

- Voice listener module.
- Voice assistant module.
- Voice verification module.
- Support for voice-related processing using the configured dependencies.

**Note:** The exact voice commands and authentication workflow depend on the implementation in the source files.

### Additional Modules

- Air keyboard functionality.
- Brightness controller.
- Volume controller.
- Central application logic.
- System state management.

---

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| OpenCV | Webcam access and image processing |
| MediaPipe | Hand detection and landmark tracking |
| NumPy | Numerical calculations |
| PyAutoGUI | Computer automation and screenshot operations |
| PyCAW | Windows audio volume control |
| comtypes | Windows COM integration |
| screen-brightness-control | Display brightness adjustment |
| Resemblyzer | Voice representation and speaker-related processing |
| SpeechBrain | Speech and speaker-related processing |
| Edge-TTS | Text-to-speech functionality, where used |
| Pillow | Image processing, where required |

The application is primarily designed for Windows.

---

## 4. System Requirements

### Hardware Requirements

- A Windows desktop computer or laptop.
- A working webcam.
- A working microphone for voice features.
- At least 8 GB RAM recommended.
- Sufficient storage for Python, dependencies, and project files.
- A supported display for brightness control.

### Software Requirements

- Windows 10 or Windows 11.
- Python 3.11 recommended as an initial environment.
- pip package manager.
- Git, if cloning the repository.
- A code editor such as Visual Studio Code (optional).

### Important Compatibility Note

Package compatibility can vary by Python version, operating system, and installed dependencies.

If a package fails to install, check its supported Python versions and the error message before changing the environment.

---

## 5. Project Structure

The main project files are organized as follows:

```text
gesture-controlled-system/
│
├── main.py
├── config.py
├── system_state.py
├── gesture_detector.py
│
├── volume_controller.py
├── brightness_controller.py
├── privacy_mode.py
├── air_keyboard.py
│
├── voice_assistant.py
├── voice_listener.py
├── voice_verify.py
│
├── brig_test.py
├── test_listener.py
├── test_voice.py
├── test_welcome.py
│
├── requirements.txt
├── README.md
├── .gitignore
│
└── profiles/
    └── Local voice-profile data, if required by the implementation
```

The `profiles/` directory is not included in the public repository because user-specific voice data should not be distributed with the source code.

The application may require this directory or another configured location for locally generated voice-profile data. Follow the voice setup instructions before using voice-dependent features.

### Main Files

| File | Purpose |
|---|---|
| `main.py` | Main application entry point |
| `config.py` | Application configuration |
| `system_state.py` | System state management |
| `gesture_detector.py` | Gesture detection and recognition |
| `volume_controller.py` | Volume control |
| `brightness_controller.py` | Brightness control |
| `privacy_mode.py` | Privacy Mode functionality |
| `air_keyboard.py` | Air keyboard functionality |
| `voice_assistant.py` | Voice assistant functionality |
| `voice_listener.py` | Voice listening functionality |
| `voice_verify.py` | Voice verification functionality |
| `test_voice.py` | Voice-related testing |
| `test_listener.py` | Listener testing |
| `test_welcome.py` | Welcome-related testing |
| `brig_test.py` | Brightness-related testing |

The exact responsibilities of individual modules may vary according to their implementation.

---

## 6. Installation

Follow these steps when installing the project on a new Windows computer.

### Step 1: Install Python

Install a compatible Python version.

Python 3.11 is a recommended starting point for this project.

Verify the installation by opening PowerShell:

```powershell
python --version
```

Check that pip is available:

```powershell
python -m pip --version
```

If the commands are not recognized, verify the Python installation and PATH configuration.

### Step 2: Clone the Repository

Open PowerShell and navigate to the directory where you want to store the project.

Run:

```powershell
git clone https://github.com/NobleCodex11/gesture-controlled-system.git
```

Navigate into the project directory:

```powershell
cd gesture-controlled-system
```

Alternatively, download the repository as a ZIP file from GitHub and extract it.

### Step 3: Create a Virtual Environment

Create an isolated Python environment:

```powershell
python -m venv venv312
```

The virtual environment keeps the project's dependencies separate from other Python applications.

### Step 4: Activate the Virtual Environment

Run:

```powershell
.\venv312\Scripts\Activate.ps1
```

If PowerShell blocks activation because of its execution policy, you can use Command Prompt instead:

```cmd
venv312\Scripts\activate.bat
```

Alternatively, use the following PowerShell command for the current terminal session if necessary:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv312\Scripts\Activate.ps1
```

### Step 5: Upgrade pip

Run:

```powershell
python -m pip install --upgrade pip
```

### Step 6: Install Dependencies

Install the project's dependencies:

```powershell
pip install -r requirements.txt
```

Wait for the installation to finish.

Some machine-learning and audio-processing packages may require additional downloads or compatible package versions.

If installation fails, inspect the error message and check the compatibility of the relevant package.

### Step 7: Check the Installation

Run:

```powershell
python -m pip check
```

This checks for incompatible installed package requirements.

A successful result indicates that pip did not find dependency conflicts among the installed packages. It does not guarantee that every application feature will work.

---

## 7. Voice Profile Setup

**Important: Voice-dependent functionality may not work immediately after installation.**

The public repository does not contain a ready-to-use personal voice profile.

A new installation may therefore require local voice enrollment or profile initialization before voice verification can be used.

Voice profile data should be generated locally rather than copied from another person's computer.

### Step 1: Connect a Microphone

Connect a working microphone or enable the computer's built-in microphone.

Check the Windows microphone settings and ensure that the application has permission to access the microphone.

### Step 2: Prepare the Local Profile Storage

If the application expects a `profiles` directory in the project root, create it:

```powershell
New-Item -ItemType Directory -Force -Path profiles
```

If the application uses a different configured location, use that location instead.

Creating this directory does not itself enroll a voice or generate a profile.

### Step 3: Inspect the Voice Verification Module

Open:

```text
voice_verify.py
```

Check whether the module provides a voice enrollment or registration procedure.

If an enrollment procedure is implemented, follow its prompts to record the required voice samples and generate the local voice profile.

If the module only verifies an existing profile, the project needs a separate enrollment or initialization procedure before verification can work.

Do not assume that simply running the verification module will create a profile.

### Step 4: Inspect the Voice Assistant and Listener

Review these files:

```text
voice_assistant.py
voice_listener.py
```

Determine how the modules are initialized and how voice commands are supplied to the application.

Check whether the application requires a specific wake-up phrase, command format, or configuration setting.

Use the commands and enrollment procedure actually implemented by the project.

### Step 5: Verify the Voice Setup

Inspect and run the voice-related test or enrollment entry point provided by the project.

The repository includes:

```text
test_voice.py
test_listener.py
```

These filenames alone do not establish whether the scripts perform enrollment, verification, or testing only.

Follow the test procedure implemented in those files.

### Step 6: Confirm Voice Verification

Before relying on voice-dependent features, verify that:

- The microphone can capture audio.
- The application can access its configured voice profile.
- The voice-processing dependencies are installed.
- The verification module completes successfully.
- The intended command or authentication flow works as expected.

### Voice Data Security

Voice profiles can contain biometric information.

- Never upload personal voice recordings or voice profiles to a public repository.
- Do not copy another user's voice profile to bypass verification.
- Keep private profile files in the local environment.
- Avoid committing generated voice data.
- Review the storage and deletion behavior of the implemented voice modules.

**Implementation note:** The exact enrollment command, profile filename, supported voice commands, and required number of voice samples must be documented from the actual source code. They should not be guessed.

---

## 8. How to Run the Application

After completing installation and any required local profile setup, follow these steps.

### Step 1: Open the Project Directory

```powershell
cd gesture-controlled-system
```

If the terminal is already inside the directory, this step is unnecessary.

### Step 2: Activate the Virtual Environment

```powershell
.\venv312\Scripts\Activate.ps1
```

### Step 3: Check Dependencies

```powershell
python -m pip check
```

### Step 4: Connect the Required Hardware

Before starting the application:

- Connect or enable the webcam.
- Ensure that Windows can access the webcam.
- Connect or enable the microphone if using voice features.
- Enable microphone permission in Windows.
- Ensure the display supports the intended brightness-control operation.

### Step 5: Start the Main Application

Run:

```powershell
python main.py
```

This is the expected startup command if `main.py` is the project's main entry point.

### Step 6: Allow Camera Access

If Windows requests camera permission, allow access to the webcam.

Position your hand within the camera's field of view.

### Step 7: Test the Gesture Controls

Perform the supported gestures described in the Gesture Controls section.

Start with one gesture at a time to confirm that the corresponding action is recognized.

### Step 8: Test Voice Features

Once the local voice profile has been configured, test the voice functionality using the implemented command or test procedure.

If the voice system is not initialized, continue using the gesture functionality only if the application supports operating without the voice subsystem.

### Step 9: Exit the Application

Use the application's configured exit method.

If the application uses an OpenCV display window, check whether the implementation provides a keyboard shortcut or window-closing mechanism.

Do not assume a particular exit key unless it is implemented in the source code.

---

## 9. Gesture Controls

The following table documents the intended gesture mappings for the project.

The exact detection thresholds and gesture classification logic are controlled by the implementation.

| Gesture | Intended Action |
|---|---|
| Thumb and index finger movement in the configured horizontal orientation | Volume control |
| Thumb and index finger movement in the configured vertical orientation | Brightness control |
| Three raised fingers | Activate Privacy Mode |
| Five raised fingers | Deactivate Privacy Mode |
| Four raised fingers held for approximately two seconds | Capture a screenshot |

### 9.1 Volume Control

The system tracks the distance between the thumb and index finger.

The measured distance is mapped to a volume range.

The volume controller uses the supported Windows audio interface to adjust the system volume.

### 9.2 Brightness Control

The system uses the configured thumb-index movement or orientation to identify the brightness-control gesture.

The recognized movement is mapped to a brightness value.

Brightness control depends on display and driver compatibility.

### 9.3 Privacy Mode

The three-finger gesture is intended to activate Privacy Mode.

The five-finger gesture is intended to deactivate it.

The implementation uses a full-screen black overlay to obscure the display.

The overlay is a visual privacy feature, not a security boundary. It should not be treated as a replacement for locking Windows.

### 9.4 Screenshot Capture

Hold the four-finger gesture for approximately two seconds.

The application is intended to capture a screenshot after the hold-duration condition is satisfied.

The exact save location and screenshot naming behavior depend on the implementation.

### Gesture Recognition Tips

For better recognition:

- Keep your hand visible to the webcam.
- Use adequate lighting.
- Avoid placing your hand too close to the camera.
- Keep your fingers distinguishable.
- Avoid rapid movements when performing a hold gesture.
- Test one gesture at a time.
- Ensure the camera is not being used exclusively by another application.

---

## 10. Voice Features

The project includes separate voice-related modules.

### Voice Listener

The listener module is responsible for voice-listening functionality implemented by the project.

### Voice Assistant

The assistant module contains the project's voice assistant logic.

### Voice Verification

The verification module handles the implemented voice verification process.

Resemblyzer and SpeechBrain are included in the intended voice-processing technology stack.

### Text-to-Speech

Edge-TTS may be used to generate spoken responses where integrated into the application.

### First-Time Voice Usage

On a new computer, voice functionality may require:

1. Microphone configuration.
2. Dependency installation.
3. Local voice-profile enrollment, if required.
4. Voice verification initialization.
5. Testing the configured commands.
6. Confirming that the application can access the generated profile.

The actual enrollment and command sequence must match the implementation.

---

## 11. Testing Individual Modules

The repository contains several testing and utility scripts.

Run these from the project root with the virtual environment activated.

### Voice Testing

```powershell
python test_voice.py
```

### Listener Testing

```powershell
python test_listener.py
```

### Welcome Screen Testing

```powershell
python test_welcome.py
```

### Brightness Testing

```powershell
python brig_test.py
```

**Important:** These commands execute the corresponding scripts. Their actual behavior depends on the code inside each file. Review the source before running scripts that record audio, change system settings, or create files.

The test scripts may require additional configuration or dependencies.

---

## 12. Troubleshooting

### Problem: Python Is Not Recognized

**Possible solution:**

Check whether Python is installed:

```powershell
python --version
```

If the command fails, verify the installation and PATH configuration.

### Problem: Dependency Installation Fails

Run:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If a specific package fails, check its supported Python versions and the installation error.

### Problem: Webcam Is Not Detected

Check:

- Windows camera permissions.
- Webcam connection.
- Camera availability.
- Whether another application is using the webcam.

If necessary, inspect the camera initialization logic in `main.py`.

### Problem: Hand Gestures Are Not Recognized

Check:

- Lighting conditions.
- Hand visibility.
- Camera position.
- Finger positioning.
- Gesture thresholds in the implementation.

### Problem: Volume Control Does Not Work

Check that:

- The operating system is Windows.
- PyCAW and comtypes are installed.
- The selected audio endpoint is available.
- The application has access to the relevant Windows audio interface.

### Problem: Brightness Does Not Change

Some external monitors do not support brightness changes through the same interface used by laptop displays.

Check display compatibility and the brightness controller implementation.

### Problem: Voice Features Do Not Work

Check:

- Microphone permissions.
- Microphone availability.
- Installed voice-processing dependencies.
- Local voice-profile initialization.
- Voice verification configuration.
- The voice listener and assistant implementation.

If the application expects a registered voice profile, installing the dependencies alone will not create that profile.

### Problem: Voice Profile Cannot Be Found

Confirm that the profile was generated successfully and stored in the configured location.

Check the path expected by `voice_verify.py` and any relevant configuration settings.

### Problem: Privacy Mode Does Not Unlock

Check whether:

- The webcam is still active.
- Hand detection is continuing.
- The five-finger gesture is recognized.
- The overlay allows the relevant gesture-control process to continue operating.

Use a normal Windows screen-lock mechanism when actual access protection is required.

---

## 13. Privacy and Security

This application uses a webcam and may use a microphone.

Users should understand how these inputs are processed and where generated data is stored.

### Recommendations

- Review camera and microphone permissions.
- Keep voice recordings and voice profiles out of public repositories.
- Exclude local profiles and private configuration files from Git.
- Never commit passwords, API keys, or authentication secrets.
- Review the source code before enabling voice authentication.
- Do not treat gesture recognition or a black overlay as strong computer authentication.
- Use Windows account security and screen locking when appropriate.

The project should not be assumed to provide secure biometric authentication or guarantee that all processing remains local until those properties have been verified in the source code.

---

## 14. Limitations

Potential limitations include:

- Gesture recognition can be affected by lighting.
- Webcam quality can influence landmark detection.
- Hand position and finger visibility affect recognition.
- Brightness control depends on display compatibility.
- Voice features require microphone access and appropriate configuration.
- Voice verification requires a supported enrollment and verification workflow.
- Different Windows configurations may require dependency adjustments.
- Gesture recognition may occasionally produce false detections.

The actual limitations depend on the implemented algorithms and hardware.

---

## 15. Future Enhancements

Potential improvements include:

- Additional configurable gestures.
- Mouse pointer control.
- Gesture-based clicking and scrolling.
- Expanded air keyboard functionality.
- Improved gesture recognition.
- Customizable gesture-to-action mappings.
- Better voice enrollment and management.
- Enhanced voice verification.
- Improved user feedback.
- Cross-platform support.
- More automated tests.
- A graphical settings interface.

These are potential enhancements and should not be interpreted as features already implemented.

---

## 16. License

A license has not been specified in this repository.

If you intend to distribute the project publicly, choose an appropriate open-source license and add the corresponding `LICENSE` file.

Until a license is added, others should not assume they have permission to reuse, modify, or redistribute the project's code.

---

## Author

**NobleCodex11**

GitHub Repository:

https://github.com/NobleCodex11/gesture-controlled-system
