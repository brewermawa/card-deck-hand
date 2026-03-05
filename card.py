from dataclasses import dataclass


@dataclass(frozen=True)
class Card:
    """
    Defines an immutable playing card object with rank and suit attributes.

    Attributes
    rank:
    Represents the rank or face of the playing card
    Must be a string. TypeError if is anything other than str.
    The valid values of rank are: "A", "2", "3", "4", "5", "6", "7", "8",
    "9", "10", "J", "Q" and "K"
    ValueError if not a valid value

    suit:
    Represents the suit of the playing card
    Must be a string. TypeError if is anything other than str.
    The valid values of suit are: "♣", "♦", "♠", "♥"
    ValueError if not a valid value
    """
    VALID_RANKS = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"}
    VALID_JOKER = "Joker"
    VALID_SUITS = {"♣", "♦", "♠", "♥"}
    VALID_JOKER_SUIT = "🃏"

    rank: str
    suit: str

    def __post_init__(self):
        if not isinstance(self.rank, str) or not isinstance(self.suit, str):
            raise TypeError("rank and suit must be of type string (str)") 
        
        if not (self.rank in self.VALID_RANKS or self.rank == self.VALID_JOKER) or not(self.suit in self.VALID_SUITS or self.suit == self.VALID_JOKER_SUIT):
            raise ValueError("rank and suit must have a valid value")
        
        if self.rank in self.VALID_RANKS and self.suit == self.VALID_JOKER_SUIT:
            raise ValueError("Joker suit invalid with rank not Joker")
        
        if self.rank == self.VALID_JOKER and self.suit in self.VALID_SUITS:
            raise ValueError("Joker rank invalid with ♣, ♦, ♠, ♥")
        
    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return f"{self.rank}{self.suit}"