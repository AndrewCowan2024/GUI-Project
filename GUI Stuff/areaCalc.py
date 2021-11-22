from tkinter import *

def area():
    def doMath():
        x=int(width.get())
        y=int(height.get())
        answerLabel.configure(text=x * y)
    
    areaCalc=Tk()

    areaCalc.title("Area Calculator")
    areaCalc.geometry("400x200")
    areaCalc.configure(bg="#2e2e2e")
    areaCalc.resizable(False,False)

    widthLabel= Label(areaCalc, bg="#2e2e2e",fg="Green", font=("sans",25), width=10 , text="Width")
    heightLabel= Label(areaCalc, bg="#2e2e2e",fg="Green", font=("sans",25), width=10 , text="Height")
    answerLabel=Label(areaCalc, bg="#2e2e2e",fg="Green", font=("sans",25), width=10)
    areaLabel=Label(areaCalc, bg="#2e2e2e",fg="Green", font=("sans",25), width=10 , text="Area")

    width=Entry(areaCalc,bg="#2e2e2e" , fg="Green", font="sans",width=10,)
    height=Entry(areaCalc,bg="#2e2e2e" , fg="Green", font="sans",width=10,)

    calculator=Button(areaCalc,bg="#2e2e2e" , fg="Green", font="sans",width=10,text="Calculator",command=doMath)


    widthLabel.grid(row=0,column=0)
    heightLabel.grid(row=1,column=0)
    width.grid(row=0,column=1)
    height.grid(row=1,column=1)
    calculator.grid(row=2,column=1)
    answerLabel.grid(row=3,column=1)
    areaLabel.grid(row=3,column=0)


    areaCalc.mainloop()