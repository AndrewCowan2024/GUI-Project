from tkinter import *
import pygame 

pygame.mixer.init()
def playSound():
    #load in sound track
    pygame.mixer.music.load("elephant.wav")

    pygame.mixer.music.set_volume(0.2)

    #play the sound
    pygame.mixer.music.play(loops=0)
def human():
    #load in sound track
    pygame.mixer.music.load("you.wav")

    pygame.mixer.music.set_volume(0.2)

    #play the sound
    pygame.mixer.music.play(loops=0)
def deer():
    #load in sound track
    pygame.mixer.music.load("sus.mp3")

    pygame.mixer.music.set_volume(0.2)

    #play the sound
    pygame.mixer.music.play(loops=3)

def crowd():
    #load in sound track
    pygame.mixer.music.load("milkshake.mp3")

    pygame.mixer.music.set_volume(0.2)

    #play the sound
    pygame.mixer.music.play(loops=0)

def ding():
    #load in sound track
    pygame.mixer.music.load("are.mp3")

    pygame.mixer.music.set_volume(0.2)

    #play the sound
    pygame.mixer.music.play(loops=0)

def crash():
    #load in sound track
    pygame.mixer.music.load("ba.mp3")

    pygame.mixer.music.set_volume(0.2)

    #play the sound
    pygame.mixer.music.play(loops=100000)

def bigBang():
    #load in sound track
    pygame.mixer.music.load("big bang.wav")

    pygame.mixer.music.set_volume(0.2)

    #play the sound
    pygame.mixer.music.play(loops=0)

def bidDrama():
    #load in sound track
    pygame.mixer.music.load("dab.mp3")

    pygame.mixer.music.set_volume(0.2)

    #play the sound
    pygame.mixer.music.play(loops=5)

def smart():
    #load in sound track
    pygame.mixer.music.load("pika.mp3")

    pygame.mixer.music.set_volume(0.2)

    #play the sound
    pygame.mixer.music.play(loops=0)

def tv():
    #load in sound track
    pygame.mixer.music.load("hey.mp3")

    pygame.mixer.music.set_volume(0.2)

    #play the sound
    pygame.mixer.music.play(loops=0)
sound=Tk()

sound.title("Photo Gallasound")

sound.geometry("600x600")

sound.configure(bg="#2e2e2e")

sound.resizable(False,False)

soundButton1=Button(sound,text="play sound",bg="#2e2e2e",fg="limegreen",activebackground="#2e2e2e",activeforeground="limegreen", command=playSound)
soundButton1.pack()

tv1=Button(sound,text="play sound",bg="#2e2e2e",fg="limegreen",activebackground="#2e2e2e",activeforeground="limegreen", command=tv)
tv1.pack()


smart=Button(sound,text="play sound",bg="#2e2e2e",fg="limegreen",activebackground="#2e2e2e",activeforeground="limegreen", command=smart)
smart.pack()

bidDrama1=Button(sound,text="play sound",bg="#2e2e2e",fg="limegreen",activebackground="#2e2e2e",activeforeground="limegreen", command=bidDrama)
bidDrama1.pack()

ding1=Button(sound,text="play sound",bg="#2e2e2e",fg="limegreen",activebackground="#2e2e2e",activeforeground="limegreen", command=ding)
ding1.pack()

deer1=Button(sound,text="sus",bg="#2e2e2e",fg="limegreen",activebackground="#2e2e2e",activeforeground="limegreen", command=deer)
deer1.pack()

crash1=Button(sound,text="play sound",bg="#2e2e2e",fg="limegreen",activebackground="#2e2e2e",activeforeground="limegreen", command=crash)
crash1.pack()

human1=Button(sound,text="play sound",bg="#2e2e2e",fg="limegreen",activebackground="#2e2e2e",activeforeground="limegreen", command=human)
human1.pack()

bigbang1=Button(sound,text="play sound",bg="#2e2e2e",fg="limegreen",activebackground="#2e2e2e",activeforeground="limegreen", command=bigBang)
bigbang1.pack()

crowd1=Button(sound,text="play sound",bg="#2e2e2e",fg="limegreen",activebackground="#2e2e2e",activeforeground="limegreen", command=crowd)
crowd1.pack()


sound.mainloop()