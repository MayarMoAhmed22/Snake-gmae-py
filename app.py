import random
import curses
# initialize the curses library to create our screen
screen=curses.initscr()
# hide the mouse cursor
curses.curs_set(0)
# get screen height and width
screen_height , screen_width=screen.getmaxyx()
window = curses.newwin(screen_height , screen_width ,0 ,0)
# allow window to recieve input from keyboard
window.keypad(1)
# set delay for updating screen
window.timeout(125)
# set x,y coordinates of the initial position of snake's head (hytl3 menen)
snake_x= screen_width//4
snake_y=screen_height//2
# define positon of snake body
snake=[[snake_y,snake_x],
       [snake_y,snake_x-1],
       [snake_y,snake_x-2]
       ]
# create food in the middle of window 
food = [screen_height//2,screen_width//2]
# add food in shape of pi character
window.addch(food[0],food[1],curses.ACS_PI)
# set initial movement to right
key = curses.KEY_RIGHT
# create game loop that looops untill lose
while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key
    # check if snake hit the wall or itself
    if snake[0][0] in [0,screen_height] or snake[0][1] in [0,screen_width] or snake[0] in snake[1:] :
        # what happen when one of conditions meet 
          # close the window
        curses.endwin()  
    #set new position to the head of snake
    new_head = [snake[0][0],snake[0][1]]
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1    
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    # insert newhead to snake 
    snake.insert(0,new_head)
    # check if snake ate the food 
    if snake[0] == food:
        # Remove the food
        food = None
        # while food is removed create food in random
        
        while food is None:
            new_food = [
                random.randint(1,screen_height-1),
                random.randint(1,screen_width-1)
            ]
            food = new_food if new_food not in snake else None
        # make theshape of pi appear
        window.addch(food[0],food[1],curses.ACS_PI)
    else:
        # remove the tail of snake 
        tail=snake.pop()
        window.addch(tail[0],tail[1],' ')
        
# update the positoon of snake On scrren
        window.addch(snake[0][0],snake[0][1],curses.ACS_CKBOARD)

