import os, json
from .voice import speak

memory_file = "friday_memory.json"

def load_memory():
    if os.path.exists(memory_file):
        with open(memory_file, "r") as f:
            return json.load(f)
    return {}

def save_memory(data):
    with open(memory_file, "w") as f:
        json.dump(data, f)

def remember(key, value):
    data = load_memory()
    data[key] = value
    save_memory(data)
    speak(f"I’ll remember that your {key} is {value}.")

def recall(key):
    data = load_memory()
    return data.get(key)
