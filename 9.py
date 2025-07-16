import speech_recognition as sr
import pyttsx3
import openai
import pyautogui
import time
import os
import pyperclip
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("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")  # ✅ Key should be in the .env file only

# Initialization
recognizer = sr.Recognizer()
engine = pyttsx3.init()
openai.api_key = "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"

def listen_command():
    """Listen to voice command and convert it to text"""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

    try:
        command = recognizer.recognize_google(audio, language="en-IN")
        print(f"You said: {command}")
        return command.lower()
    except Exception as e:
        print("Could not understand:", str(e))
        return ""

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def get_code_from_chatgpt(prompt):
    """Get code from ChatGPT"""
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
        print("ChatGPT Error:", str(e))
        return None

def insert_code_to_vscode(code):
    """Paste code into VS Code using clipboard + Ctrl+V"""
    try:
        pyperclip.copy(code)
        pyautogui.hotkey('alt', 'tab')  # Switch to VS Code
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')  # Paste the code
        speak("Code pasted successfully")
    except Exception as e:
        print("VS Code insertion error:", str(e))
        speak("There was an issue inserting the code")

def process_code_request(command):
    """Process the voice command and fetch code"""
    speak("Requesting code from ChatGPT")
    code_prompt = command.replace("generate code", "").replace("write code", "").strip()
    
    if not code_prompt:
        speak("Please provide details about the code")
        return
    
    code = get_code_from_chatgpt(code_prompt)
    
    if code:
        speak("vs")
        insert_code_to_vscode(code)
    else:
        speak("Failed to get code from ChatGPT")

def main():
    speak("Hello Master, Code Assistant Jarvis is ready to serve you.")
    
    while True:
        command = listen_command()
        
        if not command:
            continue
            
        if 'stop' in command or 'exit' in command or 'shut down' in command:
            speak("Goodbye Master")
            break
            
        if 'generate code' in command or 'write code' in command:
            process_code_request(command)
        else:
            speak("Please provide a code-related command")

if __name__ == "__main__":
    main()
