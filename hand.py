from card import Card

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("card must be an instance of Card")

        self.cards.append(card)

    def __len__(self):
        return len(self.cards)