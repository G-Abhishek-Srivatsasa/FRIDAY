import time, re
from .voice import speak, listen
from .news import get_news
from .apps import open_app, close_app
from .mail import send_email, read_unread
from .system import system_status, battery_status, system_control
from .memory import remember, recall
from .search import wiki_search, duckduckgo_query

def run_assistant():
    speak("Systems online. Awaiting your command.")
    while True:
        query = listen()
        if not query:
            continue
        print("You said:", query)

        if "time" in query:
            import datetime
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {now}")

        elif "news" in query:
            for h in get_news(): speak(h)

        elif "open" in query:
            open_app(query.replace("open", "").strip())
            speak("Done.")

        elif "close" in query:
            close_app(query.replace("close", "").strip())
            speak("Closed.")

        elif "send email" in query:
            send_email("amma", "Hello from Friday!")

        elif "read email" in query:
            read_unread()

        elif "system status" in query:
            speak(system_status())

        elif "battery" in query:
            speak(battery_status())

        elif "remember that" in query:
            fact = query.replace("remember that", "").strip()
            remember("fact", fact)

        elif "what did you remember" in query:
            fact = recall("fact")
            speak(f"I remember that {fact}" if fact else "Nothing stored.")

        elif "shutdown" in query or "restart" in query or "lock" in query:
            system_control(query)

        elif "terminate" in query:
            speak("Goodbye boss.")
            break

        else:
            result = wiki_search(query) or duckduckgo_query(query)
            speak(result or "I couldn’t find anything.")
