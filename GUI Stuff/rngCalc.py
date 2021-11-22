from tkinter import *
import random

def rng():
    def doRng():
        x=int(number1.get())
        y=int(number2.get())
        answerLabel.configure(text=random.randrange(x,y))
    
    rngCalc=Tk()

    rngCalc.title("RNG Calculator")

    rngCalc.geometry("400x200")

    rngCalc.configure(bg="#2e2e2e")

    rngCalc.resizable(False,False)

    maximum= Label(rngCalc, bg="#2e2e2e",fg="Green", font=("sans",25), width=10 , text="Minimum")
    minimum= Label(rngCalc, bg="#2e2e2e",fg="Green", font=("sans",25), width=10 , text="Maximum")
    answerLabel=Label(rngCalc, bg="#2e2e2e",fg="Green", font=("sans",25), width=10)
    areaLabel=Label(rngCalc, bg="#2e2e2e",fg="Green", font=("sans",25), width=10 , text="Number")
    number1=Entry(rngCalc,bg="#2e2e2e" , fg="Green", font="sans",width=10,)
    number2=Entry(rngCalc,bg="#2e2e2e" , fg="Green", font="sans",width=10,)
    calculator=Button(rngCalc,bg="#2e2e2e" , fg="Green", font="sans",width=10,text="Roll",command=doRng)


    number1.grid(row=0,column=0)
    number2.grid(row=1,column=0)
    maximum.grid(row=0,column=1)
    minimum.grid(row=1,column=1)
    calculator.grid(row=2,column=1)
    answerLabel.grid(row=3,column=1)
    areaLabel.grid(row=3,column=0)

    rngCalc.mainloop()