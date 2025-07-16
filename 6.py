def main():
    speak("नमस्ते मालिक, मैं जार्विस आपकी सेवा के लिए तैयार हूँ")
    
    while True:
        command = listen_command()
        
        if 'बंद करो' in command:
            speak("अलविदा मालिक")
            break
            
        execute_command(command)
        
        # जेस्चर डिटेक्शन को पैरेलल में चलाएं
        # (थ्रेड का उपयोग करें)

if __name__ == "__main__":
    main()