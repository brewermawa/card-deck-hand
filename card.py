from dataclasses import dataclass


@dataclass(frozen=True)
class Card:
    VALLID_RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    VALID_SUITS = ["♣", "♦", "♠", "♥"]

    rank: str
    suit: str

    def __post_init__(self):
        if not isinstance(self.rank, str) or not isinstance(self.suit, str):
            raise(TypeError)
        
        if self.rank not in self.VALLID_RANKS or self.suit not in self.VALID_SUITS:
            raise(ValueError)
        
    def __str__(self):
        return f"{self.rank}{self.suit}"
