from itertools import groupby
from collections import defaultdict

cards_priority = {
    "6": 0,
    "7": 1,
    "8": 2,
    "9": 3,
    "T": 4,
    "J": 5,
    "Q": 6,
    "K": 7,
    "A": 8,
}

def beat(deck, card):
    for c in deck:
        if cards_priority[c[0]] > cards_priority[card[0]]:
            return c

with open("input.txt") as f:
    _, _, trump = f.readline().split()
    deck = [(i[0], i[1]) for i in f.readline().split()]
    cards = [(i[0], i[1]) for i in f.readline().split()]
    deck.sort(key=lambda x: (x[1] != trump, cards_priority[x[0]]))
    cards.sort(key=lambda x: (x[1] != trump, cards_priority[x[0]]))
    grouped_deck = {"S": [], "C": [], "D": [], "H": []}
    for key, items in groupby(deck, lambda x: x[1]):
        grouped_deck[key] = list(items)

    for card in cards:
        val, suit = card
        if suit != trump:
            res = beat(grouped_deck[suit], card)
            if res is not None:
                grouped_deck[suit].remove(res)
                continue
        if suit == trump:
            res = beat(grouped_deck[trump], card)
        elif len(grouped_deck[trump]) > 0:
            res = grouped_deck[trump][0]
        else:
            res = None
        if res is not None:
            grouped_deck[trump].remove(res)
            continue
        print("NO")
        quit()
    print("YES")
