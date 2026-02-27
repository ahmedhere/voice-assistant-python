import speech_recognition as sr
import webbrowser
import pyttsx3
import time

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    time.sleep(0.3)
    engine.stop()
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    if 'open google' in command.lower():
        webbrowser.open('https://google.com')
    elif 'open youtube' in command.lower():
        webbrowser.open("https://youtube.com")

if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)

            command = recognizer.recognize_google(audio).lower()
            print("Heard:", command)

            if "jarvis" in command:
                speak("Yes?")
                
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

                command = recognizer.recognize_google(audio)
                processCommand(command)

        except sr.WaitTimeoutError:
            print("Listening timed out...")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except Exception as e:
            print("Error:", e)