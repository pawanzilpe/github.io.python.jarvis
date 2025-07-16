import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Text-to-Speech Engine Setup
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

def speak(text):
    print("🤖 Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 17:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How can I help you?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("🔍 Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"🗣️ You said: {query}\n")
    except Exception as e:
        speak("Sorry, I didn't catch that. Please say again.")
        return "None"
    return query.lower()

def main():
    wish_me()
    while True:
        query = take_command()

        if "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")

        elif "open google" in query:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")

        elif "play music" in query:
            music_dir = "C:\\Users\\Public\\Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Playing music")

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif "stop" in query or "exit" in query:
            speak("Okay, exiting. Have a great day!")
            break

        else:
            speak("I can search that on Google for you.")
            webbrowser.open(f"https://www.google.com/search?q={query}")

if __name__ == "__main__":
    main()


def speak(text):
    try:
        print("🤖 Jarvis:".encode('utf-8').decode(), text)
    except UnicodeEncodeError:
        print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()
