import tkinter as tk
from tkinter import filedialog
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

current_song = ""

# Functions
def load_music():
    global current_song
    file = filedialog.askopenfilename(
        title="Select Music",
        filetypes=[("Audio Files", "*.mp3 *.wav *.ogg")]
    )

    if file:
        current_song = file
        song_label.config(text=os.path.basename(file))

def play_music():
    if current_song:
        pygame.mixer.music.load(current_song)
        pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

# GUI
root = tk.Tk()
root.title("Simple Music Player")
root.geometry("400x250")
root.resizable(False, False)

title = tk.Label(root, text="Python Music Player", font=("Arial", 16, "bold"))
title.pack(pady=10)

song_label = tk.Label(root, text="No song selected", fg="blue")
song_label.pack(pady=5)

load_btn = tk.Button(root, text="Load Music", width=20, command=load_music)
load_btn.pack(pady=5)

play_btn = tk.Button(root, text="Play", width=20, command=play_music)
play_btn.pack(pady=5)

pause_btn = tk.Button(root, text="Pause", width=20, command=pause_music)
pause_btn.pack(pady=5)

resume_btn = tk.Button(root, text="Resume", width=20, command=resume_music)
resume_btn.pack(pady=5)

stop_btn = tk.Button(root, text="Stop", width=20, command=stop_music)
stop_btn.pack(pady=5)

root.mainloop()