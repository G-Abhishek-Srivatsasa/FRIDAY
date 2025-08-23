import smtplib, imaplib, email
from .voice import speak

try:
    from config_example import EMAIL, APP_PASSWORD   # your private secrets
except ImportError:
    from .config_example import EMAIL, APP_PASSWORD

contacts = {
    "mom":"EMAIL 1",
    "dad": "EMAIL 2",
    "brother": "EMAIL 3",
}

def send_email(name, body):
    if name not in contacts:
        speak("Sorry! No contact found.")
        return
    receiver = contacts[name]
    msg = f"Subject: From Friday\n\n{body}"
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL, APP_PASSWORD)
        server.sendmail(EMAIL, receiver, msg)
        server.quit()
        speak(f"Email sent to {name}")
    except Exception as e:
        print("Error:", e)
        speak("Could not send the email")

def read_unread():
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(EMAIL, APP_PASSWORD)
        mail.select("inbox")
        _, messages = mail.search(None, "UNSEEN")
        ids = messages[0].split()
        if not ids:
            speak("No unread emails.")
        else:
            latest = ids[-1]
            _, data = mail.fetch(latest, "(RFC822)")
            msg = email.message_from_bytes(data[0][1])
            speak("Latest unread email. Subject: " + msg["subject"])
    except:
        speak("Could not read emails.")
