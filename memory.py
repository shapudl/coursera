
#implementation of card game - Memory
#try it here --- http://www.codeskulptor.org/#user32_CBgCeL1mXa_17.py

import simplegui
import random
card = -1

state= 0
turn = 0
pairs = []
clicked = []
hand = []
size = 8
# helper function to initialize globals

def new_game():
    global turn, clicked, pairs
    
    clicked = []
    pairs = []
    turn = 0
    for k in range(size*2) :
        clicked.append(False);
    
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
    global state,card,turn, clicked, hand
    
    if state == 0 or state == 1 :
        state +=1
    else :
        state = 1
        turn += 1
        inp.set_text('Turn =' + str(turn))
    
    for k in range(size*2):
        
        if pos[0]>k*50 and pos[0]<(k+1)*50:
            if clicked[k] == False :
                
                clicked[k] = True
                
                if state == 1 and len(hand) == 2:
                    clicked[hand[0][0]] = False
                    clicked[hand[1][0]] = False
                    hand = []
                              
                hand.append([k,pairs[k]])
                if len(hand) == 2 :
                    if hand[0][1] == hand[1][1] :
                        print "Found a pair!"
                        hand = []
                  
    
        
def show_card(k):
    pass

# cards are logically 50x100 pixels in size    
def draw(canvas):
    global pos,pairs,clicked
    
    for k in range(len(pairs)):
        canvas.draw_text(str(pairs[k]), ( k*50+ 16,60), 40,"teal")
        
    for k in range(size*2):
        if clicked[k] == True :
            canvas.draw_polygon([(k * 50, 0), ((k+1)*50, 0), ((k+1)*50, 100), (k*50,100)], 1, "gray")
    
        else:
            canvas.draw_polygon([(k * 50, 0), ((k+1)*50, 0), ((k+1)*50, 100), (k*50,100)], 1, "Yellow","teal")
        

    

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", size * 100, 100)
frame.set_canvas_background('Silver')
frame.add_button("Reset", new_game)
inp = frame.add_label('Turn = 0' , 50)
inp.set_text('Turn =' + str(turn))


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

