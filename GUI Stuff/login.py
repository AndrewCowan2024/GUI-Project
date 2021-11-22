from tkinter import *
import mainMenu
import areaCalc
import rngCalc



def notHide():
    passEntry.configure(show="")

def hide():
    passEntry.configure(show="*")
def enter():
    if passEntry.get() == "apple":
        label1.configure(text="ACCESS GRANTED")
        login.destroy()
        mainMenu.everyoneIsShortButMicah()
    else:
        label1.configure(text="ACCESS DENIED")



login=Tk()
login.title("Secret Password")
login.geometry("400x400")
login.resizable(False,False)
login.configure(bg="#2e2e2e")
showButton=Button(login, text="Click to Reveal Password",bg="#2e2e2e",fg="black", font="sans", command=notHide,activebackground="#2e2e2e",activeforeground="black")

passEntry= Entry(login,bg="#2e2e2e", fg="limegreen", font="sans" , show="*")

hideButton=Button(login, text="Hide Password",font="sans",bg="#2e2e2e",fg="black", command=hide,activebackground="#2e2e2e",activeforeground="black" ) 

passwordCheck=Label(login,bg="#2e2e2e",fg="green", )

label1=Label(login,text="", bg="#2e2e2e",fg="limegreen",)

enterButton=Button(login, text="Enter",bg="#2e2e2e",fg="black",command=enter,activebackground="#2e2e2e",activeforeground="black")


enterButton.pack()
label1.pack()
showButton.pack()
passEntry.pack()
hideButton.pack()
passwordCheck.pack()
login.mainloop()
