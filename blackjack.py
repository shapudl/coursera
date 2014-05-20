#try it out ----> http://www.codeskulptor.org/#user33_ybIjaqqMaO_15.py
# Blackjack - with rules simplified a bit

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    
cardB_loc = [CARD_BACK_SIZE[0]+CARD_BACK_CENTER[0], CARD_BACK_SIZE[1]+CARD_BACK_CENTER[1]]
# initialize some useful global variables

in_play = False
outcome = "Start new game - deal"
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
        
class Hand:

    def __init__(self):

        self.hand = []	# create Hand object
        self.value = 0
        self.word = "Hand contains"
        
    def __str__(self):
        # return a string representation of a hand

          return self.word    

    def add_card(self, card):
        
        self.word += " " + str(card) 
                
        self.hand.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        self.value = 0
        Ace  = 0
        
        for crd in self.hand:
            self.value += VALUES[crd.rank]					 # default +1 for Ace
            if crd.rank == 'A' :
                Ace += 1
            
        if (Ace >= 1) and (self.value + 10 < 21) : 	# if Ace already in hand and + 10 < 21
            self.value += 10
            
        return self.value    
       
   
    def draw(self, canvas, pos):
        k = 0
        
        for crd in self.hand :  # draw a hand on the canvas, use the draw method for cards
            crd.draw(canvas,[pos[0] + k*100,pos[1]])
            k +=1

DEALER = Hand()
PLAYER = Hand()
        
# define deck class 
class Deck:
    
    def __init__(self):
        # create a Deck object
        self.cards = []
        for i in SUITS :
            for j in RANKS :
                self.cards.append(Card(i,j))
        self.count = 0

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards)
      

    def deal_card(self):
        # deal a card object from the deck
        self.count +=1
        if self.count > 52:
            self.cards = []
            for i in SUITS :
                for j in RANKS :
                    self.cards.append(Card(i,j))
        
        return self.cards.pop()
    
    def __str__(self):
        # return a string representing the deck
        word = "Deck contains"
        print len(self.cards)
        
        for k in range(len(self.cards)) :
            word += " " + str(self.cards[k])
        return word 

# defintion of global Deck
DECK  = Deck()

#define event handlers for buttons
def deal():
    global outcome, in_play, DEALER, PLAYER
    
    in_play = True
    
    DECK = Deck()
    DECK.shuffle()
    
    DEALER = Hand()
    PLAYER = Hand()
    
    PLAYER.add_card(DECK.deal_card())
    DEALER.add_card(DECK.deal_card())
    PLAYER.add_card(DECK.deal_card())
    DEALER.add_card(DECK.deal_card())
    
    print "Dealer :", DEALER
    print "Player :", PLAYER
    
    outcome = "Hit or stand?"
    

def hit():
    global in_play, outcome, score
    
    PLAYER.add_card(DECK.deal_card())
    print "Player value : ", PLAYER.get_value()
    
    # if the hand is in play, hit the player
    if PLAYER.get_value() <= 21 :
        in_play = True
        outcome = "Hit or stand?"
    else :
        in_play = False
        print "Bust"
        outcome = "You have busted..."
        score -= 1
           
    
    print "Dealer :", DEALER
    print "Player :", PLAYER
   
def stand():
    global in_play, outcome, score

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if PLAYER.get_value() <= 21 :
        in_play = False
        
        while DEALER.get_value() < 17 :
            DEALER.add_card(DECK.deal_card())
        
        if DEALER.get_value() > 21 :
                outcome = "Dealer is bust, you win!"
                score += 1
        else:
            if PLAYER.get_value() <= DEALER.get_value() :
                outcome = "Dealer wins"
                score = score -1
            else :
                outcome = "You win!"
                score += 1
        
    else :
        in_play = False
        outcome = "You have busted"
        score -= 1
        
    print "Dealer :", DEALER
    print "Player :", PLAYER
    
# draw handler    
def draw(canvas):
    global outcome
    
    canvas.draw_text('BLACK',[50,60],30,"White")
    canvas.draw_text('JACK',[155,60],30,"Black")
    
    canvas.draw_text(outcome,[50,120],20,"Yellow")
    
    if score >= 0 :
        canvas.draw_text(str(score),[450,90],40,"lime")
    else : 
        canvas.draw_text(str(score),[450,90],40,"red")
        
    PLAYER.draw(canvas,[100,400])
    DEALER.draw(canvas,[100,200])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [100 + CARD_BACK_SIZE[0]/2, 200 + CARD_BACK_SIZE[1]/2], CARD_BACK_SIZE)
    
    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling

frame.start()
