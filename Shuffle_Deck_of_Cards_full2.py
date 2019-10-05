import random as rand 

def create(): 
     ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']   
     suites = ['H', 'C', 'D', 'S'] 
     deck = [[r + s] for s in suites for r in ranks]    
     return deck   

def cards_dealt(num_cards, num_players, deck): 
     rand.shuffle(deck) 

mydeck = create()
cards_dealt(5, 3, mydeck)
print(mydeck)
"""
mydeck = create()
hands = cards_dealt(5, 3, mydeck)
for hand in hands:
    print(hand)
"""
