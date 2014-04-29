import random 
import simplegui

number = random.randint(1,100)
upper = 100
x = 0
counter = 7

def enter(t):
    global x
    global counter 

    counter -= 1
    if counter == 0 : 
        print "Game over. You are out of tries."	
        guess()
        return x
    else : 
        print "You still have ", counter, "guesses left!"	

    if t.isdigit() :     
        x = int (t)
        print x
        if number < x:
            print "Lower than ", x
        elif number > x:
            print "Higher than ", x
        elif number == x:
            print "Correct"
            guess()
        return x
    else : 
        print "Wrong input. Please enter a number next time."
        print "This try won't count"
        counter +=1
        return x

def guess():
    global upper
    global number
    global counter

       
    if upper == 100 :
        counter = 7
    
    if upper == 1000 :
        counter = 10	
    number = random.randint(1,upper)
    print "You've just started a new game in 1 - ", upper, " range"
    print "Number you want is ", number

def r1():
    global upper
    upper = 100
    print "You selected 1-100 range."
    guess()

def r2():
    global upper
    upper = 1000  
    print "You selected 1-1000 range"
    guess()
   


game = simplegui.create_frame("Guess The Number!", 200, 200)
game.add_button ("Start / Restart", guess , 100)
game.add_button ("Start / Restart Range 1-100", r1, 100)
game.add_button ("Start / Restart Range 1-1000", r2, 100)
game.add_input("Enter a number", enter, 100)

print "Your first game with range 1 - 100 has started.", number
print "Selecting a different range will start a new game" 
game.start()
