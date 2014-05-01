#### work in progress
## stopwatch game for two players

import simplegui

# Global variables
interval = 100
count_try = 0
count_win =0
count = 0
minutes = "00"
sec = "00"
mili = "0"

# Button handlers
def go():
    global count
    
    if count == 0:
        count += 1
        print "Start"
        timer.start()
    count +=1
    timer.start()
    
def stop():
    global count
    
    count = 0
    count_try = 0
    count_win = 0
    timer.stop()

def pause():
    print "wait"
    timer.stop()
    
def play():
    global count_try
    global count_win
    
    count_try += 1
    if count % 10 == 0 :
        count_win += 1
   
    
    
# Helper functions    
def format(t):
    # time format
    global mili
    global sec
    global minutes
    
    #milisecs
    mili = str (count % 10)
    
    #seconds
    if (count / 10) % 60 < 10 :
        sec = "0" + str ((count / 10) % 60)
    else : 
        sec = str ((count / 10) % 60)
    
    #minutes
    if (count / 600) < 10:
        minutes = "0" + str(count / 600)
    else :
        minutes = str(count / 600)
        
    time = minutes + ":" + sec + "." + mili
    return time 
    
def score(w, t):
    #score format
    s = str(w) + "/" + str(t)
    return s

def decor(canvas):
    
    canvas.draw_line([0,35], [299,35], 1 , "White")
    canvas.draw_line([0,260], [299,260], 1 , "White")
    canvas.draw_text("Score", [135,285], 20, "White")
    canvas.draw_text("Purple",[50,250], 20, "Purple")
    canvas.draw_text("vs.", [150,250], 20 , "White")
    canvas.draw_text("Yellow", [210,250], 20, "Yellow")
    
# Define handlers        
def draw(canvas):
    
    decor(canvas)
    
    canvas.draw_text(format(count), [80,150], 50, "Maroon")
    canvas.draw_text(score(count_win, count_try), [250, 22] , 20, "Yellow")
    canvas.draw_text(score(count_win, count_try), [25, 22] , 20, "Purple")


frame = simplegui.create_frame("Stopwatch game", 300,300)
timer = simplegui.create_timer(100, go )

frame.set_draw_handler(draw)
frame.set_canvas_background("silver")
frame.add_button("Start", go, 100)
frame.add_button("Stop", pause , 100)
frame.add_button("Reset", stop, 100)
frame.add_button("Click", play, 100)

player1 = frame.add_label("Purple player:")
player2 = frame.add_label("Yellow player:")

frame.start()
timer.start()
