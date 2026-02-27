import speech_recognition as sr
import webbrowser
import pyttsx3
# from gtts import gTTS
import time
from dotenv import load_dotenv
import os
import requests
from google import genai

load_dotenv()


recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    # gTTS(text)

def aiProcess(command):    
    client = genai.Client(
        api_key=os.getenv('GEMINI_API_KEY')
    )

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=command,
    )
    speak(response.text)


def processCommand(command):
    if 'open google' in command.lower():
        webbrowser.open('https://google.com')
    elif 'open youtube' in command.lower():
        webbrowser.open("https://youtube.com")
    elif 'news' in command.lower():
        url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={os.environ.get('API_KEY')}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])

            for article in articles:
                speak(article['title'])
        else:
            speak("Something went wrong!")
    else:
        aiProcess(command)

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
                with sr.Microphone() as source:
                    speak("Yes?")
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