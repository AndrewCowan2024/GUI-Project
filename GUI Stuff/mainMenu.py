from tkinter import *
import areaCalc
import rngCalc
import image
import soundPlay
def everyoneIsShortButMicah():

    def areaCalculator():
        mainMenu.destroy()
        areaCalc.area()

    def rngCalculator():
        mainMenu.destroy()
        rngCalc.rng()

    def imageGallary():
        mainMenu.destroy()
        image.photoLib()

    def soundPlay1():
        mainMenu.destroy()
        sound.soundplay
    mainMenu=Tk()
    mainMenu.geometry("600x600")
    mainMenu.title("Main Menu")
    mainMenu.configure(bg="#2e2e2e")

    areaCalcButton=Button(mainMenu, text="Area Calculator",bg="#2e2e2e",fg="limeGreen",font=("sans",20),width=20,activebackground="black",activeforeground="limeGreen",command=areaCalculator)
    areaCalcButton.grid(column=0,row=0)

    photoImage=Button(mainMenu, text="Image Gallary",bg="#2e2e2e",fg="limeGreen",font=("sans",20),width=20,activebackground="black",activeforeground="limeGreen",command=imageGallary)
    photoImage.grid(column=0,row=1)

    rngCalcButton=Button(mainMenu, text="Rng Calculator",bg="#2e2e2e",fg="limeGreen",font=("sans",20),width=20,activebackground="black",activeforeground="limeGreen",command=rngCalculator)
    rngCalcButton.grid(column=1,row=1)

    soundPlayButton=Button(mainMenu, text="Area Calculator",bg="#2e2e2e",fg="limeGreen",font=("sans",20),width=20,activebackground="black",activeforeground="limeGreen",command=soundPlay1)
    soundPlayButton.grid(column=1,row=0)

    mainMenu.mainloop()