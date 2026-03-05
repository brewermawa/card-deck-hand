from cards.card import Card

class Hand:
    def __init__(self):
        self._cards = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("card must be an instance of Card")
        
        self._cards.append(card)

    def remove_last_card(self):
        if len(self._cards) == 0:
            raise ValueError("Cannot remove card, hand is empty")

        return self._cards.pop()
    
    def clear(self):
        self._cards.clear()

    def __len__(self):
        return len(self._cards)
    
    def __str__(self):
        return ", ".join(str(card) for card in self._cards)
    
    @property
    def cards(self):
        return self._cards
    
    @property
    def cards_in_hand(self):
        return self.__len__()