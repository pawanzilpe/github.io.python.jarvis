from gtts import gTTS
import playsound
import os
import speech_recognition as sr
import datetime
import webbrowser

def speak(text):
    print("Jarvis (Hindi):", text)
    tts = gTTS(text=text, lang='hi')
    tts.save("voice.mp3")
    playsound.playsound("voice.mp3")
    os.remove("voice.mp3")

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("सुप्रभात!")
    elif 12 <= hour < 17:
        speak("नमस्कार! शुभ दोपहर!")
    else:
        speak("शुभ संध्या!")
    speak("मैं हूँ जार्विस। मैं आपकी क्या मदद कर सकता हूँ?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 सुन रहा हूँ...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("🔍 पहचान रहा हूँ...")
        query = r.recognize_google(audio, language='hi-IN')
        print(f"🗣️ आपने कहा: {query}")
    except:
        speak("माफ कीजिए, मैं समझ नहीं पाया। कृपया फिर से कहें।")
        return "none"
    return query.lower()

def main():
    wish_me()
    while True:
        query = take_command()

        if "youtube" in query:
            webbrowser.open("https://www.youtube.com")
            speak("यूट्यूब खोल रहा हूँ...")

        elif "goolge" in query:
            webbrowser.open("https://www.google.com")
            speak("गूगल खोल रहा हूँ...")

        elif "संगीत" in query:
            music_dir = "C:\\Users\\Public\\Music"
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, songs[0]))
                speak("संगीत चला रहा हूँ...")
            else:
                speak("संगीत फोल्डर खाली है।")

        elif "समय" in query or "टाइम" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"अभी समय है {strTime}")

        elif "बंद" in query or "बाय" in query or "रुको" in query:
            speak("ठीक है, अलविदा!")
            break

        else:
            speak("मैं इसे गूगल पर खोज रहा हूँ।")
            webbrowser.open(f"https://www.google.com/search?q={query}")

if __name__ == "__main__":
    main()
