import os
import webbrowser
import pyautogui

def execute_command(command):
    if 'व्हाट्सएप्प खोलो' in command:
        webbrowser.open("https://web.whatsapp.com")
        speak("व्हाट्सएप्प खोल रहा हूँ")
    
    elif 'मैसेज भेजो' in command:
        # मैसेज भेजने का लॉजिक
        pyautogui.write('आपका मैसेज')
        pyautogui.press('enter')
        
    elif 'गूगल पर सर्च करो' in command:
        query = command.replace('गूगल पर सर्च करो', '')
        webbrowser.open(f"https://google.com/search?q={query}")
        
        
        