from hand import Hand


class Player:
    def __init__(self, name: str, hand: Hand = None):
        self.name: str = name
        self.hand = hand
        self.big_blind: bool = False
        self.small_blind: bool = False
