from tkinter import *

window = Tk()

window.title("This is a test")
window.minsize(width=500, height=500)
label=Label(text="0")
label.grid(column=4,row=0)

input = Entry(width=10)
input.grid(column=2,row=0)
input2 = Entry(width=10)
input2.grid(column=3,row=0)
def buttonclick():
    sum = int(input.get()) + int(input2.get())
    label["text"]= sum


button2 = Button(text="Add",command=buttonclick)

button2.grid(column=10,row=2)

button3 = Button(text="Multiply",command=buttonclick)

button3.grid(column=50,row=2)

button = Button(text="Subtract",command=buttonclick)

button.grid(column=30,row=2)
window.mainloop()