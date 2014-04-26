
# Rock-paper-scissors-lizard-Spock 


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
import random

def name_to_number(name):
    name = name.lower()
    if name == "rock":
     number = 0
    elif name == "spock":
     number = 1
    elif name == "paper":
     number = 2
    elif name == "lizard":
     number = 3
    elif name == "scissors":
     number = 4
    else : 
        print "Error input"
    
    return number

def number_to_name(number):
    if number == 0:
     return "rock"
    elif number == 1:
     return "Spock"
    elif number == 2:
     return "paper"
    elif number == 3:
     return "lizard"
    elif number == 4:
     return "scissors"
    else : 
     print "Wrong number"
    

def rpsls(player_choice):
    
    computer_choice = random.randint(0,4)
    print "Your choice is ", player_choice, "."
    print "Computer choose ", number_to_name(computer_choice), "."
    player_choice = name_to_number(player_choice)
    
    print computer_choice, "-", player_choice, "=" , computer_choice - player_choice
    
    ## to battle we ride 
    result = computer_choice - player_choice 	
    
    if result < 0 : 
     result += 5
   
    if result == 1 or result == 2 :
     return "You lose!"
    elif result == 3 or result == 4:
     return "You win!"
    else: 
     return "There are no winners."	

    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
