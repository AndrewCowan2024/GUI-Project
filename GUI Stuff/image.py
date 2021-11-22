from tkinter import * 
def photoLib():
    image= Tk()
    image.title("Photo Gallary")
    image.geometry("600x600")
    image.configure(bg="#2e2e2e")
    global x
    x==0
    def next():
        global x
        x= x+1

        if x==1:
            imageLabel1.configure(image=firstImage)
        if x==2:
            imageLabel2.configure(image=secondImage)
        if x==3:
            imageLabel3.configure(image=thirdImage)
        if x==4:
            imageLabel4.configure(image= forthImage)
        if x==5:
            imageLabel5.configure(image=fifthImage)
        if x==6:
            imageLabel6.configure(image=sixthImage)
        if x==7:
            imageLabel7.configure(image=seventhImage)
        if x==8:
            imageLabel8.configure(image=eighthImage)
        if x==9:
            imageLabel9.configure(image=ninegthImage)
        if x==10:
            imageLabel10.configure(image=tenthImage)


    def back():
        global x
        x= x-1

        if x==1:
            imageLabel1.configure(image=firstImage)
        if x==2:
            imageLabel2.configure(image=secondImage)
        if x==3:
            imageLabel3.configure(image=thirdImage)
        if x==4:
            imageLabel4.configure(image= forthImage)
        if x==5:
            imageLabel5.configure(image=fifthImage)
        if x==6:
            imageLabel6.configure(image=sixthImage)
        if x==7:
            imageLabel7.configure(image=seventhImage)
        if x==8:
            imageLabel8.configure(image=eighthImage)
        if x==9:
            imageLabel9.configure(image=ninegthImage)
        if x==10:
            imageLabel10.configure(image=tenthImage)





    nextButton1=Button(image,text="NEXT",bg="#2e2e2e",fg="Green", font=("sans",25), width=10 )
    backButton1=Button(image,text="BACK",bg="#2e2e2e",fg="Green", font=("sans",25), width=10 )

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


    imageLabel1.configure(image=firstImage)
    imageLabel2.configure(image=secondImage)
    imageLabel3.configure(image=thirdImage)
    imageLabel4.configure(image= forthImage)
    imageLabel5.configure(image=fifthImage)
    imageLabel6.configure(image=sixthImage)
    imageLabel7.configure(image=seventhImage)
    imageLabel8.configure(image=eighthImage)
    imageLabel9.configure(image=ninegthImage)
    imageLabel10.configure(image=tenthImage)

    nextButton1.grid(row=0,column=0)
    backButton1.grid(row=1,column=0)
    


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