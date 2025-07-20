import speech_recognition as sr
import pyttsx3
import webbrowser
import os
from datetime import datetime

# Initialize Text-to-Speech
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change voice index if needed

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        
    try:
        command = r.recognize_google(audio).lower()
        print(f"Command: {command}")
        return command
    except:
        return ""

def generate_website(elements):
    """Generate HTML/CSS based on voice commands"""
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Generated Website</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            .container {{ max-width: 800px; margin: 0 auto; }}
            {elements.get('css', '')}
        </style>
    </head>
    <body>
        <div class="container">
            {elements.get('html', '<h1>Voice-Generated Website</h1>')}
            <p>Created on {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
        </div>
    </body>
    </html>
    """
    return html_template

def process_command(command):
    elements = {'html': '', 'css': ''}
    
    # Header detection
    if 'header' in command or 'heading' in command:
        text = extract_phrase_after(command, ['header', 'heading'])
        elements['html'] += f"<h1>{text.capitalize()}</h1>" if text else "<h1>Welcome</h1>"
    
    # Paragraph detection
    if 'paragraph' in command or 'text' in command:
        text = extract_phrase_after(command, ['paragraph', 'text', 'say'])
        elements['html'] += f"<p>{text.capitalize()}</p>" if text else "<p>Sample paragraph</p>"
    
    # Button detection
    if 'button' in command:
        text = extract_phrase_after(command, ['button'])
        elements['html'] += f"<button>{text or 'Click Me'}</button>"
    
    # Color customization
    if 'color' in command:
        colors = ['red', 'blue', 'green', 'yellow', 'black', 'white']
        found = [c for c in colors if c in command]
        if found:
            elements['css'] += f"body {{ background-color: {found[0]}; }}"
    
    # Image insertion
    if 'image' in command or 'picture' in command:
        elements['html'] += """<img src="https://via.placeholder.com/400x200?text=Voice+Generated" 
        alt="Generated Image">"""
    
    return generate_website(elements)

def extract_phrase_after(command, keywords):
    for kw in keywords:
        if kw in command:
            idx = command.index(kw) + len(kw)
            return command[idx:].strip()
    return ""

# Main workflow
if __name__ == "__main__":
    speak("Welcome to Voice Website Generator. What would you like to create?")
    
    while True:
        command = listen_command()
        
        if 'exit' in command:
            speak("Goodbye!")
            break
            
        if command:
            website_code = process_command(command)
            with open("generated_website.html", "w") as f:
                f.write(website_code)
            
            # Open in browser
            webbrowser.open('file://' + os.path.realpath("generated_website.html"))
            speak("Website generated successfully!")
        else:
            speak("Sorry, I didn't understand. Please try again.")
            
            