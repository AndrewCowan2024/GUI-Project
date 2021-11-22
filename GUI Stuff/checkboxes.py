from tkinter import *

def checkIt():
    if check.get()==0:
        words.configure(text="NO")
    else:
        words.configure(text="YES")
main=Tk()

main.title("RNG Calculator")
main.geometry("400x200")
main.configure(bg="#2e2e2e")
main.resizable(False,False)

check=IntVar()
check1=Checkbutton(main, variable=check,onvalue=1,offvalue=0,command=checkIt)

check1.pack()

words=Label(main,text="NO")
words.pack()

main.mainloop()