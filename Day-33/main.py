from tkinter import *
import requests
qoute = ''

def qoute_generator():
    try:
        resonse = requests.get(' https://api.kanye.rest/')
        d = resonse.json()
        m = d['quote']
        return m
    except:
        return "Error"
        
    

def get_quote():
    qoute = qoute_generator()
    canvas.itemconfig(quote_text, text=f"{qoute}")
    



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="Day-33/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="Day-33/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)
window.mainloop()