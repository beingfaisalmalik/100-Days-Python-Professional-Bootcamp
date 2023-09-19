
from  tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import math
def starttime():
    global reps
    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN *60
    
    if (reps%8==0):
        countdown(long_break_sec)
    elif(reps%2==0):
        countdown(short_break_sec)
    else:
         countdown(work_sec)
def countdown(count):
    count_min = math.floor(count/60)
    count_sec = (count%60)
    
    if count_sec <10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count >0:
        window.after(1000,countdown,count-1)
    
    

# ---------------------------- UI SETUP ------------------------------- #tkinter

window = Tk()
window.title("POMODORO")
window.config(padx=100,pady=50,bg=YELLOW)
timelabel = Label(text="TIMER",font=("Arial",25,'bold'),foreground=GREEN,bg=YELLOW)
timelabel.grid(column=2,row=0)
canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="Day-28/tomato.png")
canvas.create_image(100,112, image=photo)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=1)

sbt = Button(text="Start", highlightthickness=0,command=starttime)
sbt.grid(column=1,row=2)
sbt = Button(text="Reset", highlightthickness=0)
sbt.grid(column=3,row=2)
sbt = Label(text="//", highlightthickness=0,bg=YELLOW)
sbt.grid(column=2,row=2)







window.mainloop()