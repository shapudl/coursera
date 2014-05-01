#### work in progress
## stopwatch game for two players


import simplegui

# Global variables
interval = 100
count_try_1 = 0
count_win_1 = 0
count_try_2 = 0
count_win_2 = 0 
score1 = 0
score2 = 0

count = 0
minutes = "00"
sec = "00"
mili = "0"
name1 = "Purple"
name2 = "Yellow"

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
    global count_try_1
    global count_try_2
    global count_win_1
    global count_win_2
    
    count = 0
    count_win_1 = 0
    count_win_2 = 0
    count_try_1 = 0
    count_try_2 = 0
    timer.stop()

def pause():
    print "wait"
    timer.stop()
    
    
    
def play_1():
    global count_try_1
    global count_win_1
    global score1
    
    count_try_1 += 1
    if count % 10 == 0 :
        count_win_1 += 1
        score1 += 3 
    else : 
        score1 -= 1
        
def play_2():
    global count_try_2
    global count_win_2
    global score2
    
    count_try_2 += 1
    if count % 10 == 0 :
        count_win_2 += 1
        score2 += 3
    else : 
        score2 -= 1
    
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
    canvas.draw_text("Score", [137,285], 20, "White")
    canvas.draw_text(name1 ,[50,250], 20, "Purple")
    canvas.draw_text("vs.", [150,250], 20 , "White")
    canvas.draw_text(name2, [210,250], 20, "Yellow")
    canvas.draw_text(str(score1), [63,289], 30, "White")
    canvas.draw_text(str(score2), [229,289], 30, "White")
    
    
# Define handlers        
def draw(canvas):
    
    decor(canvas)
    
    canvas.draw_text(format(count), [80,150], 50, "Maroon")
    canvas.draw_text(score(count_win_2, count_try_2), [250, 22] , 20, "Yellow")
    canvas.draw_text(score(count_win_1, count_try_1), [25, 22] , 20, "Purple")
    
def purple_handler(text):
    global name1
    
    name1 = text
    return name1

def yellow_handler(text):
    global name2
    
    name2 = text
    return name2 

def key_handler(key1):
    if key == simplegui.KEY_MAP['left']:
        play_1
    return



# Register handlers

frame = simplegui.create_frame("Stopwatch game", 300,300)
timer = simplegui.create_timer(100, go )

frame.set_draw_handler(draw)
frame.set_canvas_background("silver")
frame.add_button("Start", go, 100)
frame.add_button("Stop", pause , 100)
frame.add_button("Reset", stop, 100)
frame.add_button("Click 1", play_1, 100)
frame.add_button("Click 2", play_2, 100)






player1 = frame.add_input("Purple player:", purple_handler , 100)
print str(name1)
player2 = frame.add_input("Yellow player:", yellow_handler , 100)
print name2

frame.start()
timer.start()
