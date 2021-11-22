from tkinter import *

def numbers():
    cal = Tk()
    cal.geometry("600x600")
    cal.title("Calculator")
    cal.configure(bg="#2e2e2e")


    button1=Button(cal, text="1")
    button2=Button(cal, text="2")
    button3=Button(cal, text="3")
    button4=Button(cal, text="4")
    button5=Button(cal, text="5")
    button6=Button(cal, text="6")
    button7=Button(cal, text="7")
    button8=Button(cal, text="8")
    button9=Button(cal, text="9")
    button0=Button(cal, text="0")


    button1.grid(column=1,row=1)
    button2.grid(column=2,row=1)
    button3.grid(column=3,row=1)
    button4.grid(column=1,row=2)
    button5.grid(column=2,row=2)
    button6.grid(column=3,row=2)
    button7.grid(column=1,row=3)
    button8.grid(column=2,row=3)
    button9.grid(column=3,row=3)
    button0.grid(column=1,row=4)


    cal.mainloop()