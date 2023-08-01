while(not at_goal()):
    if wall_in_front() == True and not right_is_clear():
            turn_left()
    elif right_is_clear() == True:
        turn_left()
        turn_left()
        turn_left()
        move()
    elif right_is_clear() == True and wall_in_front() == True :
        turn_left()
        turn_left()
        turn_left()
        move()
    else:
        move()
        
        
        
#Use Algorithm
