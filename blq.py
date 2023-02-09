import keyboard
import winsound
from tkinter import *
import pygame

root = Tk()
root.title("Bloqueo de Mayúsculas")
root.geometry("200x100")

caps_lock_count = 0
word = ""
monitoring = False

def start_monitoring():
    global monitoring
    monitoring = True
    keyboard.on_press(on_press)

def stop_monitoring():
    global monitoring
    monitoring = False
    keyboard.unhook_all()

def on_press(key):
    global caps_lock_count, word
    if not monitoring:
        return
    if key.name == "caps lock":
        caps_lock_count = 0
    elif key.name == "space":
        if caps_lock_count >= 3:
            pygame.mixer.init()
            pygame.mixer.music.load("output.wav")
            pygame.mixer.music.play()
        caps_lock_count = 0
        word = ""
    elif key.name.isupper():
        word += key.name
        caps_lock_count += 1
        if caps_lock_count >= 3:
            pygame.mixer.init()
            pygame.mixer.music.load("output.wav")
            pygame.mixer.music.play()

start_button = Button(root, text="Iniciar Monitoreo", command=start_monitoring)
start_button.pack()

stop_button = Button(root, text="Detener Monitoreo", command=stop_monitoring)
stop_button.pack()

root.mainloop()
