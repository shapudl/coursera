# Implementation of classic arcade game Pong
# try to play here : http://www.codeskulptor.org/#user32_uVcypfVRu8_5.py
# LEFT PLAYER : 'q' for up, 'a' for down
# RIGHT PLAYER: up and down arrow keys 

import simplegui
import random
import math
import time

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 800
HEIGHT = 400       
BALL_RADIUS = 40
PAD_WIDTH = 20
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

paddle1_pos = 0
paddle2_pos = 0
paddle1_vel = 0
paddle2_vel = 0
score1=0
score2=0

# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0,0]

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    score1 = 0 
    score2 = 0
    
    ball_vel[0] = random.choice([-2,2])
    ball_vel[1] = random.choice([-2,2])
    
    paddle1_pos = HEIGHT / 2 - PAD_HEIGHT / 2
    paddle2_pos = HEIGHT / 2 - PAD_HEIGHT / 2
    
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle2_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[1] - BALL_RADIUS /2 < 0 or ball_pos[1] + BALL_RADIUS /2 > HEIGHT :
        ball_vel[1] = -ball_vel[1]
    
        # do ball and pad collide  
            #left
    if ball_pos[0] - BALL_RADIUS / 2 < PAD_WIDTH :
        if distance([0,ball_pos[1] - BALL_RADIUS], [0,paddle1_pos]) < PAD_HEIGHT and distance([0,ball_pos[1] + BALL_RADIUS], [0,paddle1_pos + PAD_HEIGHT]) < PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0]
        else:
            #time.sleep(2000)
            update()
            score2 += 1
            
            #right
    if ball_pos[0] + BALL_RADIUS / 2 > WIDTH - PAD_WIDTH:
        if distance([0,ball_pos[1] - BALL_RADIUS], [0,paddle2_pos]) < PAD_HEIGHT and distance([0,ball_pos[1] + BALL_RADIUS], [0,paddle2_pos + PAD_HEIGHT]) < PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0]
        else:
            #time.sleep(2000)
            update()
            score1 +=1 
            
            
    # draw ball
    canvas.draw_circle([ball_pos[0], ball_pos[1]], 1, BALL_RADIUS, "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos =paddle1_pos + paddle1_vel 
    paddle2_pos =paddle2_pos + paddle2_vel
    
    if paddle1_pos <= 0 or (paddle1_pos + PAD_HEIGHT >= HEIGHT) : 
        paddle1_vel = - paddle1_vel  
        
    if paddle2_pos <= 0 or (paddle2_pos + PAD_HEIGHT >= HEIGHT) : 
        paddle2_vel = -paddle2_vel
        
    
    # draw paddles
        # left paddle
    canvas.draw_line([0,paddle1_pos],[PAD_WIDTH,paddle1_pos],1,"White")
    canvas.draw_line([0,paddle1_pos + PAD_HEIGHT],[PAD_WIDTH,paddle1_pos + PAD_HEIGHT],1,"White")
        # right paddle
    canvas.draw_line([WIDTH -1 ,paddle2_pos],[WIDTH - 1 - PAD_WIDTH,paddle2_pos],1,"White")
    canvas.draw_line([WIDTH -1 ,paddle2_pos + PAD_HEIGHT],[WIDTH-1 -PAD_WIDTH,paddle2_pos + PAD_HEIGHT],1,"White")  
    
    # draw scores
    canvas.draw_text(str(score1),[WIDTH / 4,100],20,"aqua")
    canvas.draw_text(str(score2),[3*WIDTH /4 ,100],20,"aqua")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    #left paddle - 'q' for up , 'a' for down
    if key == simplegui.KEY_MAP['q'] :
        paddle1_vel -= 1
    if key == simplegui.KEY_MAP['a']:
        paddle1_vel += 1
     
    #right paddle - up down arrows
    if key == simplegui.KEY_MAP['up'] :
        paddle2_vel -= 1
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel += 1
        
        
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
        
def distance(p,q):
    d = math.sqrt( (p[0]-q[0]) ** 2 + (p[1]-q[1]) ** 2  ) 
    return d

def update():
    global ball_pos
    
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel[0] = random.choice([-2,2])
    ball_vel[1] = random.choice([-2,2])
   


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
