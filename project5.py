# implementation of card game - Memory

import simplegui
import random

cardList = []
cardList.extend(range(0,8))
cardList.extend(range(0,8))
exposed = [0] * 16
turnCount = 0
state = 0
firstClick = None
lastClick = None

# helper function to initialize globals
def new_game():
    global cardList, turnCount, exposed, state
    global firstClick, lastClick
    random.shuffle(cardList)
    turnCount = 0
    exposed = [0] * 16
    state = 0
    firstClick = None
    lastClick = None
    label.set_text("Turns = " + str(turnCount))

     
# define event handlers
def mouseclick(pos):
    global exposed, turnCount, firstClick, lastClick, state
    i = pos[0] / 50
    if exposed[i] == 0:
        exposed[i] = 1
        if firstClick != None and lastClick != None :
            if cardList[firstClick] != cardList[lastClick]:
                exposed[firstClick] = 0
                exposed[lastClick] = 0
            firstClick = None
            lastClick = None
        if state == 0:
            firstClick = i
            state = 1
        elif state == 1:
            lastClick = i
            state = 0       
            turnCount += 1
            label.set_text("Turns = " + str(turnCount))

                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    pos = 0
    border = 'Yellow'
    for i in range(0,16):
        if i % 2 == 1:
            border = 'Yellow'
        else:
            border = 'Blue'
        if exposed[i] == 0:
            canvas.draw_polygon([[pos, 0], [pos+50, 0], [pos+50, 100], [pos, 100]], 1, 'Red', 'Green')
        else:
            canvas.draw_polygon([[pos, 0], [pos+50, 0], [pos+50, 100], [pos, 100]], 1, 'Red', 'Black')
            canvas.draw_text(str(cardList[i]), (pos+10, 50), 48, 'Red')
        pos += 50   


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turnCount))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric