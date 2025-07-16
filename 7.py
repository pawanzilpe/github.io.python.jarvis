import speech_recognition as sr
import pyttsx3
import openai
import pyautogui
import time
import os
import pyperclip
from dotenv import load_dotenv

# एनवायरनमेंट वेरिएबल्स लोड करें
load_dotenv()
OPENAI_API_KEY = os.getenv('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')

# इनिशियलाइज़ेशन
recognizer = sr.Recognizer()
engine = pyttsx3.init()
openai.api_key = OPENAI_API_KEY

def listen_command():
    """आवाज से कमांड सुनें और टेक्स्ट में कन्वर्ट करें"""
    with sr.Microphone() as source:
        print("सुन रहा हूँ...")
        recognizer.adjust_for_ambient_noise(source)
        #audio = recognizer.listen(source, timeout=5)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

    try:
        command = recognizer.recognize_google(audio, language="hi-IN")
        print(f"आपने कहा: {command}")
        return command.lower()
    except Exception as e:
        print("समझ नहीं आया", str(e))
        return ""

def speak(text):
    """टेक्स्ट को आवाज में बदलें"""
    engine.say(text)
    engine.runAndWait()

def get_code_from_chatgpt(prompt):
    """ChatGPT से कोड प्राप्त करें"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful coding assistant. Provide only the code without any explanations."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print("ChatGPT एरर:", str(e))
        return None

def insert_code_to_vscode(code):
    """कोड को VS Code में इंसर्ट करें"""
    try:
        # VS Code एक्टिवेट करें
        pyautogui.hotkey('alt', 'tab')
        time.sleep(1)
        
        # कोड टाइप करें
        pyautogui.write(code, interval=0.01)
        speak("कोड सफलतापूर्वक इंसर्ट किया गया")
    except Exception as e:
        print("VS Code इंसर्शन एरर:", str(e))
        speak("कोड इंसर्ट करने में समस्या आई")

def process_code_request(command):
    """कोड रिक्वेस्ट को प्रोसेस करें"""
    speak("ChatGPT से कोड रिक्वेस्ट कर रहा हूँ")
    code_prompt = command.replace("कोड बनाओ", "").strip()
    
    if not code_prompt:
        speak("कृपया कोड के बारे में विवरण दें")
        return
    
    code = get_code_from_chatgpt(code_prompt)
    
    if code:
        speak("कोड प्राप्त हुआ, अब VS Code में इंसर्ट कर रहा हूँ")
        insert_code_to_vscode(code)
    else:
        speak("ChatGPT से कोड प्राप्त करने में असफल")

def main():
    speak("नमस्ते मालिक, कोड असिस्टेंट जार्विस आपकी सेवा के लिए तैयार है")
    
    while True:
        command = listen_command()
        
        if not command:
            continue
            
        if 'बंद करो' in command or 'रुको' in command:
            speak("अलविदा मालिक")
            break
            
        if 'कोड बनाओ' in command or 'कोड लिखो' in command:
            process_code_request(command)
        else:
            speak("कृपया कोड से संबंधित कमांड दें")

if __name__ == "__main__":
    main()
    
def insert_code_to_vscode(code):
    """कोड को VS Code में पेस्ट करें (pyperclip + Ctrl+V method)"""
    try:
        pyperclip.copy(code)  # कोड क्लिपबोर्ड में कॉपी करें
        pyautogui.hotkey('alt', 'tab')  # VS Code एक्टिवेट करें
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')  # पेस्ट करें
        speak("कोड सफलतापूर्वक पेस्ट किया गया")
    except Exception as e:
        print("VS Code इंसर्शन एरर:", str(e))
        speak("कोड इंसर्ट करने में समस्या आई")
