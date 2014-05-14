#IN PROGRESS
#implementation of card game - Memory
# try it out here : http://www.codeskulptor.org/#user32_CBgCeL1mXa_6.py


import simplegui
import random


state= 0
turn = 0
pairs = []
size = 4
# helper function to initialize globals

def new_game():
    
    create_pairs()

    
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
    global state
    
    if state == 0 or state == 1 :
        state += 1
    else : 
        state = 1
    
    for k in range(size*2):
        if pos[0]>k*50 and pos[0]<(k+1)*50:
            print k
            return k
        
    
    
        
def show_card(k):
    pass

# cards are logically 50x100 pixels in size    
def draw(canvas):
    
    for k in range(size*2):
        canvas.draw_polygon([(k * 50, 0), ((k+1)*50, 0), ((k+1)*50, 100), (k*50,100)], 1, "Yellow","Red")
    
    

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", size * 100, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
