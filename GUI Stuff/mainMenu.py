from tkinter import *
import areaCalc
import rngCalc
def everyoneIsShortButMicah():

    def areaCalculator():
        mainMenu.destroy()
        areaCalc.area()

    def rngCalculator():
        mainMenu.destroy()
        rngCalc.rng()


    mainMenu=Tk()
    mainMenu.geometry("600x600")
    mainMenu.title("Main Menu")
    mainMenu.configure(bg="#2e2e2e")

    areaCalcButton=Button(mainMenu, text="Area Calculator",bg="#2e2e2e",fg="limeGreen",font=("sans",20),width=20,activebackground="black",activeforeground="limeGreen",command=areaCalculator)
    areaCalcButton.grid(column=0,row=0)

    rngCalcButton=Button(mainMenu, text="Rng Calculator",bg="#2e2e2e",fg="limeGreen",font=("sans",20),width=20,activebackground="black",activeforeground="limeGreen",command=rngCalculator)
    rngCalcButton.grid(column=0,row=1)

    mainMenu.mainloop()