import tkinter
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)
label = tkinter.Label(text="I am a Label",font=("Arial",25,'bold'))
label.pack()




count = 0
input = tkinter.Entry(width=10)
input.pack()
def buttonclicked():
    c = input.get()
    label["text"] = c

button = tkinter.Button(text="Click Me",command=buttonclicked)
button.pack()
text = tkinter.Text(height=5,width=30)
text.focus()
text.insert(index="20",chars="Faisl")
text.pack()
#Entry 














window.mainloop()