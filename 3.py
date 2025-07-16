import speech_recognition as sr
import pyttsx3

# इनिशियलाइज़ेशन
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def listen_command():
    with sr.Microphone() as source:
        print("सुन रहा हूँ...")
        audio = recognizer.listen(source)
        
    try:
        command = recognizer.recognize_google(audio, language="hi-IN")
        print(f"आपने कहा: {command}")
        return command.lower()
    except Exception as e:
        print("समझ नहीं आया, कृपया दोहराएं")
        return ""

def speak(text):
    engine.say(text)
    engine.runAndWait()