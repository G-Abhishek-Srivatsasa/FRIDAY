import os, subprocess

def open_app(app_name):
    if "notepad" in app_name:
        os.system("notepad")
    elif "calculator" in app_name:
        subprocess.Popen("calc.exe")
    elif "paint" in app_name:
        os.system("mspaint")
    elif "chrome" in app_name:
        os.system("start chrome")
    elif "spotify" in app_name:
        os.system("start spotify://")
    elif "whatsapp" in app_name:
        os.system("start whatsapp://")
    else:
        print("Application not supported")

def close_app(app_name):
    if "notepad" in app_name:
        os.system("taskkill /im notepad.exe /f")
    elif "calculator" in app_name:
        os.system("taskkill /im calc.exe /f")
    elif "paint" in app_name:
        os.system("taskkill /im mspaint.exe /f")
    elif "chrome" in app_name:
        os.system("taskkill /im chrome.exe /f")
    elif "whatsapp" in app_name:
        os.system("taskkill /im WhatsApp.exe /f")
    elif "spotify" in app_name:
        os.system("taskkill /im Spotify.exe /f")
    else:
        print("Application not supported")
