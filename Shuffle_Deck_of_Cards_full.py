import random

def define_cards():
    rank_string = ("ace","2","3","4","5","6","7","8","9","10","jack","queen","king")
    suit_string = ("clubs","diamonds","hearts","spades")
    cards = []
    for suit in range(4):
        for rank in range(13):
            card_string = rank_string[rank] + " " + suit_string[suit]
            cards.append(card_string)
    return cards

def create_deck(deck):
    for i in range(52):
        deck.append(i)
        return

def shuffle_deck(deck):
    random.shuffle(deck)
    return

def deal_card(deck):
    return deck.pop(0)

deck=[]
"""
create_deck(deck)
shuffle_deck(deck)
print "The first 10 cards are:"
for i in range(10):             # I don't know why won't work
    deal_card(card)
    print define_cards()
"""
deck = define_cards()
shuffle_deck(deck)
print("The first 10 cards are:")
for i in range(10):
    card = deal_card(deck)
    print(card)
