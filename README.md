# Techno-Voice_Assistant

## Description
This is a voice-controlled assistant project using Python.  
Created from **26-12-2024 to 29-12-2024**.  
It runs based on Python version **3.12**.

The assistant can perform multiple tasks, including:
- Recognizing and responding to voice commands.
- Playing YouTube videos.
- Opening desktop applications and URLs.
- Telling jokes.
- Taking screenshots.
- Accessing Wikipedia.
- Providing time and date info.


The assistant uses multiple libraries like pyttsx3 for text-to-speech, speech recognition for voice input, and other libraries to control the system, access the internet, and automate tasks.

## Features
- **Text-to-Speech**: Uses pyttsx3 to convert text responses to speech.
- **Voice Recognition**: Recognizes user commands using speech_recognition.
- **Time & Date**: Provides the current date and time.
- **Application Control**: Can open apps like Notepad, Google Chrome, etc.
- **Web Browser**: Opens URLs directly in the default browser.
- **YouTube**: Plays YouTube videos using pywhatkit.
- **Camera Access**: Takes a photo using the system's camera.
- **Screenshot**: Captures the screen using pyautogui.
- **Jokes**: Tells random jokes using pyjokes.
- **Wikipedia**: Searches Wikipedia for information based on voice commands.
- **System Info**: Provides system info and monitors system performance using psutil.

## Prerequisites

Before running the project, make sure to install the necessary Python libraries. You can do this by running the following command:

```bash
pip install -r requirements.txt
```

This will install all the dependencies listed in the `requirements.txt` file.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ravinandan2005/Techno-Voice_Assistant.git
```

2. Navigate into the project directory:

```bash
cd Techno-Voice_Assistant
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Run the main Python file:

```bash
python voice_assistant.py
```

## Requirements

The following Python libraries are required to run the project:

```
pyttsx3
speechrecognition
datetime
os
subprocess
webbrowser
pywhatkit
opencv-python
time
pyautogui
pyjokes
random
wikipedia
requests
psutil
```

You can install all of them using:

```bash
pip install -r requirements.txt
```

## Usage

Once you run the assistant, it will wait for a voice command. You can say commands like:
- "Open YouTube"
- "Play [song name] on YouTube"
- "What time is it?"
- "Take a screenshot"
- "Tell me a joke"
- "Open [app name]"
- "Search Wikipedia for [topic]"

### Commands included in the main function:
1. **Open YouTube**: Opens the YouTube homepage in the default browser.
2. **Play [song name] on YouTube**: Plays a specific song or video on YouTube.
3. **What time is it?**: Responds with the current time.
4. **Take a screenshot**: Captures a screenshot and saves it in the project directory.
5. **Tell me a joke**: Responds with a random programmer joke.
6. **Open [app name]**: Opens a specified application (like Notepad, Google Chrome, etc.).
7. **Search Wikipedia for [topic]**: Searches Wikipedia for the given topic and reads out the summary.
8. **Exit**: Ends the assistant program.
and much more give it a run

## Future Enhancements

### 1. Natural Language Processing (NLP):
   - Integrating NLP models to improve the assistant's understanding of complex commands, enabling more accurate and efficient communication with the user.

### 2. Task Automation:
   - Adding more personalized task automation features, such as managing emails, to-do lists, reminders, and calendar events, making the assistant more versatile for daily tasks.

### 3. Cross-Platform Compatibility:
   - Expanding the assistant's compatibility across different operating systems and platforms (e.g., macOS, Linux, and mobile devices) to make it accessible to a wider audience.


## Contributions

Feel free to fork this repository, submit issues, or send pull requests. Contributions are welcome!

## If you find this project helpful, please consider giving it a ⭐ and forking it! 🙏


## Contact Me

Feel free to contact me through any of the available platforms in my profile. You can also visit my GitHub profile to explore my projects and get in touch.

- [GitHub Profile](https://github.com/ravinandan2005)

**Done By:** [@Ravinandan2005](https://github.com/ravinandan2005)
