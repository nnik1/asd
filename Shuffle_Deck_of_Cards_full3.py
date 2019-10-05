import random

def shuffle(cards):
    write_index = 0 # to write,
    while write_index < len(cards):
        read_index = random.randint(write_index, len(cards)-1)
        cards[read_index], cards[write_index] = cards[write_index], cards[read_index]
        write_index += 1

def shuffle_v2(cards):
    for i in range(1, len(cards)):
        index = random.randint(0, i-1)
        cards[index], cards[i] = cards[i], cards[index]

cards = []
for i in range(10):
    cards.append(random.randint(1,52))
print(cards)

shuffle(cards)
print(cards)

shuffle_v2(cards)
print(cards)
