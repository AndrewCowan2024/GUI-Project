from tkinter import * 
def photoLib():
    image= Tk()
    image.title("Photo Gallary")
    image.geometry("1600x1000")
    image.configure(bg="#2e2e2e")
    global x
    x=0
    def next():
        global x
        x= x+1
        if x==1:
            imageLabel1.configure(image=firstImage)
        if x==2:
            imageLabel1.configure(image=secondImage)
        if x==3:
            imageLabel1.configure(image=thirdImage)
        if x==4:
            imageLabel1.configure(image= forthImage)
        if x==5:
            imageLabel1.configure(image=fifthImage)
        if x==6:
            imageLabel1.configure(image=sixthImage)
        if x==7:
            imageLabel1.configure(image=seventhImage)
        if x==8:
            imageLabel1.configure(image=eighthImage)
        if x==9:
            imageLabel1.configure(image=ninegthImage)
        if x==10:
            imageLabel1.configure(image=tenthImage)


    def back():
        global x
        x= x-1
        if x==1:
            imageLabel1.configure(image=firstImage)
        if x==2:
            imageLabel1.configure(image=secondImage)
        if x==3:
            imageLabel1.configure(image=thirdImage)
        if x==4:
            imageLabel1.configure(image= forthImage)
        if x==5:
            imageLabel1.configure(image=fifthImage)
        if x==6:
            imageLabel1.configure(image=sixthImage)
        if x==7:
            imageLabel1.configure(image=seventhImage)
        if x==8:
            imageLabel1.configure(image=eighthImage)
        if x==9:
            imageLabel1.configure(image=ninegthImage)
        if x==10:
            imageLabel1.configure(image=tenthImage)





    nextButton1=Button(image,text="NEXT",bg="#2e2e2e",fg="Green", font=("sans",25), width=10,command=next )
    backButton1=Button(image,text="BACK",bg="#2e2e2e",fg="Green", font=("sans",25), width=10,command=back)

    firstImage=PhotoImage(file="haha.png")
    secondImage=PhotoImage(file="heeels.png")
    thirdImage=PhotoImage(file="hi.png")
    forthImage=PhotoImage(file="nail head.png")
    fifthImage=PhotoImage(file="no bones.png")
    sixthImage=PhotoImage(file="omg.png")
    seventhImage=PhotoImage(file="pizza ya.png")
    eighthImage=PhotoImage(file="pizza.png")
    ninegthImage=PhotoImage(file="vr.png")
    tenthImage=PhotoImage(file="wall E.png")


    imageLabel1=Label(image)
    imageLabel2=Label(image)
    imageLabel3=Label(image)
    imageLabel4=Label(image)
    imageLabel5=Label(image)
    imageLabel6=Label(image)
    imageLabel7=Label(image)
    imageLabel8=Label(image)
    imageLabel9=Label(image)
    imageLabel10=Label(image)


    

    


    nextButton1.pack()
    backButton1.pack()
    imageLabel1.pack()
    imageLabel2.pack()
    imageLabel3.pack()
    imageLabel4.pack()
    imageLabel5.pack()
    imageLabel6.pack()
    imageLabel7.pack()
    imageLabel8.pack()
    imageLabel9.pack()
    imageLabel10.pack()

    image.mainloop()
