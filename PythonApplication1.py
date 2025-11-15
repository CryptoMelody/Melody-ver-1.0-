import pygame
import time
import os
import webbrowser
import json
import pyaudio
import urllib.parse
from vosk import Model, KaldiRecognizer


pygame.mixer.init()

model = Model(r"D:\vosk-model-small-en-us-0.15")
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

def google_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    search_url = search_url.replace(' ', '+')
    webbrowser.open(search_url)

def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer['text']:
                yield answer['text']

def play_sound(file_path):
  
    try:
        
        if not os.path.exists(file_path):
            print(f"Audio file not found: {file_path}")
            return False
        
      
        try:
        
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            return True
        except pygame.error:
        
            try:
                sound = pygame.mixer.Sound(file_path)
                sound.play()
                time.sleep(sound.get_length() + 0.5)
                return True
            except:
                
                print(f"Using system player for: {file_path}")
                os.system(f'start "" "{file_path}"')
                time.sleep(2)  
                return True
                
    except Exception as e:
        print(f"Error playing sound {file_path}: {e}")
        return False

def process_command(command):
    command_lower = command.lower()
    
    if command_lower.startswith('open'):
        site = None
        site_name = command[6:].strip()
        if site_name == "ello" or site_name == "hello":
            site = 'https://yandex.com'
        elif site_name == "youtube" or site_name == "ou tube":
            site = 'https://youtube.com'
        elif site_name == "mail" or site_name == "ail":
            site = 'https://mail.ru'
        
        if site:
            play_sound(r"C:\Users\USER\Desktop\ttt\audio_2025-11-15_18-19-08.ogg")
            webbrowser.open(site)
        else:
            print(f"Unknown site: {site_name}")
            
    elif command_lower.startswith('search'):
        p = command[6:].strip()
        play_sound(r"C:\Users\USER\Desktop\ttt\audio_2025-11-15_18-33-52.ogg")
        google_search(p)
        
    elif command_lower.startswith('find'):
        p = command[5:].strip()
        if p == "browser":
            os.system(f"start browser.exe")
            play_sound(r"C:\Users\USER\Desktop\ttt\audio_2025-11-15_18-28-10.ogg")
        else:
            play_sound(r"C:\Users\USER\Desktop\ttt\audio_2025-11-15_18-28-31.ogg")
            print('Unknown programm')


for text in listen():
    print(f"Recognized: {text}")

    text_lower = text.lower()
    if text_lower == "thanks" or text_lower == "thank you":
        play_sound(r"C:\Users\USER\Desktop\ttt\audio_2025-11-15_18-19-08.ogg")
    elif text_lower == "hello" or text_lower == "ello":
        play_sound(r"C:\Users\USER\Desktop\ttt\audio_2025-11-15_18-03-34.ogg")
    elif text_lower == "how are you":
        play_sound(r"C:\Users\USER\Desktop\ttt\audio_2025-11-15_18-23-22.ogg")
    elif text_lower == "you are asshole":
        play_sound(r"C:\Users\USER\Desktop\ttt\audio_2025-11-15_18-33-04.ogg")
    elif text_lower == "i did that":
        play_sound(r"C:\Users\USER\Desktop\ttt\audio_2025-11-15_18-23-12.ogg")
    elif text_lower == "melody":
        play_sound(r"C:\Users\USER\Desktop\ttt\audio_2025-11-15_18-23-22.ogg")
    else:
      
        process_command(text)