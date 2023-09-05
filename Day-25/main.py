from turtle import Turtle,Screen
import pandas as pd
screen = Screen()
turtle = Turtle()
df = pd.read_csv("Day-25/50_states.csv")
image = "Day-25/blank_states_img.gif"
screen.bgpic(image)

while True:

    a = screen.textinput(title="Guess The State",prompt="Whats The Next State")


    allstates = df["state"]
    stateslist = allstates.to_list()

    if a in stateslist:
        s = True 
    else:
        s = False

    if s:
        st = df[df["state"] == a]
        state_dic = st.to_dict()
        keydic = state_dic['state']
        key ,value = list(keydic.items())[0]
        print(str(key))
        state = state_dic['state'][key]
        xcorr = state_dic['x'][key]
        ycor = state_dic['y'][key]
        turtle.penup()
        turtle.goto(xcorr,ycor)
        turtle.write(f'{a}', True, align="center")
        print(state,xcorr,ycor)
    else:
        print("Invalid state")
        break


screen.exitonclick()