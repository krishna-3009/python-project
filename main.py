import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://www.google.com")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in command:
        webbrowser.open("https://instagram.com")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
    else:
        speak("I didn't understand the command.")

if __name__ == "__main__":
    speak("Initializing Krishna...")

    while True:
        try:
            # Listen for the wake word "Krishna"
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=2)
                
                word = recognizer.recognize_google(audio).lower()
                if word == "krishna":
                    speak("Yes, how can I help you?")
                    
                    # Listen for the actual command
                    with sr.Microphone() as source:
                        print("Listening for command...")
                        recognizer.adjust_for_ambient_noise(source)
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        
                        command = recognizer.recognize_google(audio)
                        processCommand(command)
        
        except sr.UnknownValueError:
            print("Sorry, I did not catch that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")



    
