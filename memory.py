#IN PROGRESS
#implementation of card game - Memory
#try it out here --> http://www.codeskulptor.org/#user32_CBgCeL1mXa_10.py

import simplegui
import random
card = -1

state= 0
turn = 0
pairs = []
clicked = []
size = 4
# helper function to initialize globals

def new_game():
    global turn, clicked
    
    turn = 0
    clicked = []
    create_pairs()
    for k in pairs:
        print k, pairs[k]
    
def create_pairs():
    global pairs
    
    for k in range(size):
        pairs.append(k)
        pairs.append(k)
     
    random.shuffle(pairs)
    print pairs
    
# define event handlers
def mouseclick(pos):
    # add game state
    global state,card,turn, clicked
    
   
    print "State & turn: ", state, turn 
    for k in range(size*2):
        if pos[0]>k*50 and pos[0]<(k+1)*50:
            card = k
            if k in clicked:
                if state == 0 or state == 1 :
                     state += 1
                else : 
                    state = 1
                    turn += 1
                    clicked.pop()
            else:
                clicked.append(k)
        
    print clicked
    
    
        
def show_card(k):
    pass

# cards are logically 50x100 pixels in size    
def draw(canvas):
    global pos,pairs,clicked
    
    for k in range(len(pairs)):
        canvas.draw_text(str(pairs[k]), ( k*50+ 16,60), 40,"aqua")
        
    for k in range(size*2):
        if k in clicked :
            canvas.draw_polygon([(k * 50, 0), ((k+1)*50, 0), ((k+1)*50, 100), (k*50,100)], 1, "Yellow")
    
        else:
            canvas.draw_polygon([(k * 50, 0), ((k+1)*50, 0), ((k+1)*50, 100), (k*50,100)], 1, "Yellow","Red")
        

    

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", size * 100, 100)
frame.add_button("Reset", new_game)
label = frame.add_label('Turn = ' + str(turn), 50)


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

