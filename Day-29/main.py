from tkinter import *
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("POMODORO")
window.config(padx=50,pady=50,bg="white")
webname = StringVar()
password = StringVar()
email = StringVar()

def add_clicked():
    with open(file='Day-29/data.txt', mode="a") as file:
        file.write(f"\n{webname.get()} | {email.get()} |  {password.get()}",) 

def generatepass():
        l = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
        randompass = ''
        for i in range(10):
            randompass += str(random.choice(l))
        passentry.insert(0,f"{randompass}")

canvas = Canvas(width=200,height=200, bg="white")
photo = PhotoImage(file="Day-29/logo.png")
canvas.create_image(100,100, image=photo)

canvas.grid(column=1,row=0)
weblabel = Label(text="Website: ",background="white")
weblabel.grid(column=0,row=1)
emaillabel = Label(text="Email/Username: ",background="white")
emaillabel.grid(column=0,row=2)
passlabel = Label(text="Password: ",background="white")
passlabel.grid(column=0,row=3)

webentry = Entry(width=35,textvariable=webname)
webentry.grid(column=1,row=1,columnspan=2)
webentry.focus()
emalentry = Entry(width=35,textvariable=email)
emalentry.grid(column=1,row=2,columnspan=2)
emalentry.insert(0,"beingfaisalmalik@gmail.com")
passentry = Entry(width=21,textvariable=password)
passentry.grid(column=1,row=3)


#Buttons

passbtn = Button(text="Generate Password",command=generatepass)
passbtn.grid(row=3,column=2)
addbtn = Button(text="ADD",width=36,command=add_clicked)
addbtn.grid(row=4,column=1,columnspan=2)
window.mainloop()

