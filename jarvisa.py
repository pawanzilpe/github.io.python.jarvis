from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import os

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        return query.lower()
    except:
        speak("Sorry, I didn't understand.")
        return "None"

class JarvisApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Tap to Start JARVIS')
        btn = Button(text='🎤 Start Listening', on_press=self.start_jarvis)
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def start_jarvis(self, instance):
        speak("Hi, I am pawan. How can I help you?")
        query = take_command()
        if "youtube" in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")
        elif "google" in query:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        else:
            speak("I will search it on Google.")
            webbrowser.open(f"https://www.google.com/search?q={query}")

if __name__ == "__main__":
    JarvisApp().run()
