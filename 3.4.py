import speech_recognition as sr
import os
import webbrowser
import pyttsx3
import time
import random
import re
import threading
import queue

# Initialize TTS engine with Hindi support
engine = pyttsx3.init()
voice_queue = queue.Queue()

# Try to set Hindi voice if available
try:
    hindi_voices = [v for v in engine.getProperty('voices') if 'hindi' in v.name.lower()]
    if hindi_voices:
        engine.setProperty('voice', hindi_voices[0].id)
    else:
        print("Hindi voice not found. Using default voice.")
except:
    print("Voice property error. Continuing with default voice.")

engine.setProperty('rate', 150)  # Slower speech rate

# Background thread for smooth TTS
def tts_worker():
    while True:
        message = voice_queue.get()
        if message is None:
            break
        try:
            engine.say(message)
            engine.runAndWait()
        except Exception as e:
            print(f"TTS त्रुटि: {e}")
        voice_queue.task_done()

tts_thread = threading.Thread(target=tts_worker, daemon=True)
tts_thread.start()

def text_to_speech(message):
    """Queue Hindi text for speech"""
    voice_queue.put(message)

def voice_to_text():
    """Convert Hindi voice input to text with enhanced recognition"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.8)
        print("सुन रहा हूँ... ('मदद' बोलकर विकल्प देखें)")
        text_to_speech("मैं सुन रहा हूँ")
        
        try:
            audio = r.listen(source, timeout=6, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            return "समय समाप्त"
            
    try:
        # Try Google first for better accuracy
        command = r.recognize_google(audio, language='hi-IN').lower()
        print(f"पहचाना: {command}")
        return command
    except sr.UnknownValueError:
        try:
            # Fallback to Sphinx for offline recognition
            command = r.recognize_sphinx(audio, language='hi-IN').lower()
            print(f"ऑफलाइन पहचाना: {command}")
            return command
        except:
            return "त्रुटि_अज्ञात"
    except sr.RequestError:
        try:
            # Try Sphinx when internet is unavailable
            command = r.recognize_sphinx(audio, language='hi-IN').lower()
            print(f"ऑफलाइन पहचाना: {command}")
            return command
        except:
            return "त्रुटि_अनुरोध"

def generate_website(command):
    """Generate Hindi website with enhanced content"""
    # Sanitize filename
    filename = re.sub(r'[^\w\u0900-\u097F]+', '', command)[:30] + ".html"
    if not filename.replace(".html", "").strip():
        filename = "वेबसाइट_" + str(int(time.time())) + ".html"

    # Generate related content based on command
    related_content = {
        "यात्रा": ["ताजमहल", "हिमालय", "केरल बैकवाटर्स"],
        "खाना": ["नॉर्थ इंडियन रेसिपी", "साउथ इंडियन डिश", "स्वस्थ भोजन"],
        "शिक्षा": ["गणित ट्यूटोरियल", "विज्ञान प्रयोग", "इतिहास पाठ"],
        "खेल": ["क्रिकेट समाचार", "फुटबॉल अपडेट", "खेल टिप्स"]
    }
    
    # Default suggestions
    suggestions = ["तस्वीरों की गैलरी", "संपर्क फॉर्म", "इंटरएक्टिव एलिमेंट्स"]
    
    # Find matching suggestions
    for keyword, items in related_content.items():
        if keyword in command:
            suggestions = items
            break

    # Hindi website template with enhanced features
    html_template = f"""<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>आवाज से बनाई गई: {command}</title>
    <style>
        :root {{
            --primary: #{random.randint(0, 0xFFFFFF):06x};
            --secondary: #{random.randint(0, 0xFFFFFF):06x};
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: 'Nirmala UI', 'Segoe UI', 'Mangal', sans-serif;
            line-height: 1.8;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: linear-gradient(135deg, #f5f7fa 0%, #e4edf5 100%);
            direction: rtl;
        }}
        header {{
            background: var(--primary);
            color: white;
            padding: 2rem;
            text-align: center;
            border-radius: 10px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        h1 {{ font-size: 2.5rem; margin-bottom: 1rem; }}
        .container {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 2rem;
        }}
        .card {{
            background: white;
            border-radius: 10px;
            padding: 1.5rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            transition: transform 0.3s ease;
            text-align: right;
        }}
        .card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.1);
        }}
        h2 {{
            color: var(--primary);
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid var(--secondary);
        }}
        footer {{
            text-align: center;
            padding: 1.5rem;
            background: #333;
            color: white;
            border-radius: 10px;
            font-size: 0.9rem;
        }}
        .voice-command {{
            background: #f0f8ff;
            padding: 1rem;
            border-radius: 5px;
            margin: 1rem 0;
            font-style: italic;
            text-align: center;
            font-family: 'Nirmala UI', sans-serif;
        }}
        .features-list {{
            padding-right: 20px;
        }}
        .screenshot {{
            width: 100%;
            height: 200px;
            background: #eee;
            border-radius: 5px;
            margin: 15px 0;
            display: flex;
            align-items: center;
            justify-content: center;
            font-style: italic;
            color: #666;
        }}
        .action-button {{
            display: block;
            width: 100%;
            padding: 10px;
            background: var(--secondary);
            color: white;
            text-align: center;
            border-radius: 5px;
            margin-top: 15px;
            text-decoration: none;
            font-weight: bold;
        }}
        @media (max-width: 768px) {{
            .container {{ grid-template-columns: 1fr; }}
            body {{ padding: 10px; }}
            h1 {{ font-size: 1.8rem; }}
        }}
    </style>
</head>
<body>
    <header>
        <h1>{command} वेबसाइट</h1>
        <p>आवाज के निर्देश पर बनाई गई</p>
    </header>
    
    <main>
        <section class="container">
            <article class="card">
                <h2>इस साइट के बारे में</h2>
                <p>यह पूरी वेबसाइट आवाज पहचान तकनीक से बनाई गई है!</p>
                <div class="voice-command">
                    "आपने कहा: <strong>{command}</strong>"
                </div>
                <p>आप इसमें ये सुविधाएँ जोड़ सकते हैं:</p>
                <ul class="features-list">
                    <li>{suggestions[0]}</li>
                    <li>{suggestions[1]}</li>
                    <li>{suggestions[2]}</li>
                </ul>
                
                <div class="screenshot">
                    वेबसाइट प्रीव्यू इमेज
                </div>
            </article>
            
            <article class="card">
                <h2>कैसे शुरू करें</h2>
                <p>इस टेम्पलेट को कस्टमाइज़ करें:</p>
                <ol class="features-list">
                    <li>HTML कंटेंट संपादित करके</li>
                    <li>CSS स्टाइल बदलकर</li>
                    <li>जावास्क्रिप्ट फंक्शनैलिटी जोड़कर</li>
                </ol>
                
                <h2>अगले कदम</h2>
                <p>नई वेबसाइट बनाने के लिए:</p>
                <a href="#" class="action-button">नई साइट बनाएँ</a>
            </article>
        </section>
    </main>
    
    <footer>
        <p>पायथन से बनाई गई • {time.strftime('%Y-%m-%d %H:%M')} • आवाज वेबसाइट जनरेटर</p>
    </footer>
</body>
</html>"""
    
    # Save to file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_template)
    
    return os.path.abspath(filename)

def show_help():
    """Hindi help instructions with more options"""
    help_text = """
    आवाज कमांड विकल्प:
    - वेबसाइट विषय बोलें (जैसे: 'यात्रा ब्लॉग', 'पोर्टफोलियो')
    - 'फोल्डर खोलो': बनाई गई वेबसाइट्स दिखाएं
    - 'नई साइट': नई वेबसाइट बनाएं
    - 'सभी साइट खोलो': सभी बनाई गई वेबसाइट खोलें
    - 'मदद': यह सहायता देखें
    - 'बंद करो': प्रोग्राम बंद करें
    """
    print(help_text)
    text_to_speech("आप बोल सकते हैं: यात्रा ब्लॉग बनाओ, पोर्टफोलियो वेबसाइट बनाओ, फोल्डर खोलो, या बंद करो")

def open_all_websites():
    """Open all generated websites in browser"""
    html_files = [f for f in os.listdir() if f.endswith('.html')]
    if not html_files:
        text_to_speech("कोई वेबसाइट नहीं मिली")
        return
    
    text_to_speech(f"{len(html_files)} वेबसाइट खोली जा रही हैं")
    for file in html_files:
        webbrowser.open(f'file://{os.path.abspath(file)}')

def main():
    text_to_speech("आवाज वेबसाइट जनरेटर में आपका स्वागत है! आप किस प्रकार की वेबसाइट बनाना चाहते हैं?")
    print("'मदद' बोलकर विकल्प देखें")
    
    while True:
        command = voice_to_text()
        
        if command == "समय समाप्त":
            text_to_speech("समय समाप्त हो गया। कृपया फिर से प्रयास करें")
            continue
            
        if command in ["त्रुटि_अज्ञात", "त्रुटि_अनुरोध"]:
            text_to_speech("क्षमा करें, मैं समझ नहीं पाया। कृपया फिर से बोलें")
            continue
            
        if "बंद करो" in command or "रुक जाओ" in command or "समाप्त करो" in command:
            text_to_speech("प्रोग्राम बंद किया जा रहा है। अलविदा!")
            # Stop TTS thread
            voice_queue.put(None)
            tts_thread.join(timeout=1)
            break
            
        if "मदद" in command or "सहायता" in command:
            show_help()
            continue
            
        if "फोल्डर खोलो" in command or "डायरेक्टरी खोलो" in command:
            folder = os.path.abspath(".")
            webbrowser.open(folder)
            text_to_speech("वेबसाइट फोल्डर खोला गया")
            continue
            
        if "नई साइट" in command or "दूसरी" in command or "नया वेबसाइट" in command:
            text_to_speech("नई वेबसाइट किस विषय पर बनाएँ?")
            continue
            
        if "सभी साइट खोलो" in command or "सभी वेबसाइट" in command:
            open_all_websites()
            text_to_speech("सभी वेबसाइट खोल दी गई हैं")
            continue
            
        # Generate website
        text_to_speech(f"{command} वेबसाइट बनाई जा रही है...")
        filepath = generate_website(command)
        
        # Open in browser
        webbrowser.open(f'file://{filepath}')
        text_to_speech(f"आपकी {command} वेबसाइट तैयार है! नई साइट बनाने के लिए 'नई साइट' बोलें या 'बंद करो' बोलकर समाप्त करें")

if __name__ == "__main__":
    main()