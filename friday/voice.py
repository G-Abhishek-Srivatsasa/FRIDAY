import pyttsx3, speech_recognition as sr

engine = pyttsx3.init(driverName="sapi5")
engine.setProperty("rate", 160)
recognizer = sr.Recognizer()

def speak(text: str):
    print("Friday says:", text)
    engine.say(text)
    engine.runAndWait()

def listen(timeout=5, phrase_time_limit=6) -> str | None:
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            return recognizer.recognize_google(audio).lower()
        except Exception:
            return None
