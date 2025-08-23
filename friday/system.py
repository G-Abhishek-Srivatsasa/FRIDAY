import os, psutil
from .voice import speak

def system_status():
    battery = psutil.sensors_battery()
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    return f"Battery {battery.percent}% | CPU {cpu}% | RAM {memory.percent}%"

def battery_status():
    battery = psutil.sensors_battery()
    percent = battery.percent
    charging = battery.power_plugged
    status = f"Battery {percent}% {'and charging' if charging else 'not charging'}"
    if percent < 15 and not charging:
        status += ". Plug in charger soon."
    return status

def system_control(command):
    if "shutdown" in command:
        os.system("shutdown /s /t 1")
    elif "restart" in command:
        os.system("shutdown /r /t 1")
    elif "lock" in command:
        os.system("rundll32.exe user32.dll,LockWorkStation")
