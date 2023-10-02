from tkinter import *
import pandas as pd
import random 
data = pd.read_csv("Day-31/french_words.csv")
tolearn = data.to_dict(orient="records")
current_card = {}
def next_card():
     global current_card
     current_card = random.choice(tolearn)
     canvas.itemconfig(cardtitle, text="French")
     canvas.itemconfig(cardword, text=current_card["French"])

def flip_card():
    global current_card
    current_card = random.choice(tolearn)
    canvas.itemconfig(cardtitle, text="English")
    canvas.itemconfig(cardword, text=current_card["English"])
  
window = Tk()

window.title("Flash Card App")
window.after(3000, func=flip_card)
window.config(padx=50,pady=50,bg="#B1DCC6")
canvas = Canvas(width=800,height=526, bg="white")
photo = PhotoImage(file="Day-31/card_front.png")

canvas.create_image(400,263, image=photo)
canvas.config(bg="#B1DCC6",highlightthickness=0)

cardtitle = canvas.create_text(400,150,text="Title", font=("Arial",40,"italic"))
cardword= canvas.create_text(400,263,text="Word", font=("Arial",40,"italic"))
canvas.grid(columnspan=2,row=0)

cross_img = PhotoImage(file="Day-31/wrong.png")
crsbtn = Button(image=cross_img,highlightthickness=0,command=next_card)
crsbtn.grid(column=0,row=1)

cross_img2 = PhotoImage(file="Day-31/right.png")
crsbtn2 = Button(image=cross_img2,highlightthickness=0)
crsbtn2.grid(column=1,row=1)

window.mainloop()