# Card class
The card class defines an immutable playing card object

## Attributes
rank - the face of the card. Must be one of "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"
suit - the suit of the card.  Must be one of "♣", "♦", "♠", "♥"

## Methods
- __str__: returns the string representation of a card rank+suit. ej, "A♥"

## Testing
All the testS for the Card class are in tests/test_card.py. 
Run tests with: pytest -q
