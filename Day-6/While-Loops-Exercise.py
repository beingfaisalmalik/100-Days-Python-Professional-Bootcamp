def jump():
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    

while(at_goal()==False):
    if(wall_in_front()==True):
        jump()
    else:
        move()