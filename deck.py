from typing import List
from card import Card
import random

class Deck():
    def __init__(self):
        self.cards: List[Card] = []
        self.discarded: List[Card] = []

    def generate_fresh_deck(self):
        colors = ["red", "black"]
        suits = ["spades", "clubs", "hearts", "diamonds"]
        numbers = [x for x in range(1, 14)]

        for color in colors:
            for suit in suits:
                for num in numbers:
                    self.cards.append(Card(num, suit, color))

    def discard_card(self, card):
        self.discarded.append(card)
        self.cards.remove(card)

    def get_random_cards(self, num_cards) -> List[Card]:
        if num_cards > len(self.cards):
            raise ValueError("adhveeryu")

        output_hand = random.sample(self.cards, num_cards)
        return output_hand

    
        