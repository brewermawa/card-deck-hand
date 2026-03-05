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


# Deck class

- The Deck class defines a deck of playing cards.
- Deck uses the Card object to create each card.
- A deck consists of every combination of RANK and SUITS. In a normal deck of cards (French-suided playing cards) there are 52 cards obtained from the  combination of 13 ranks and 4 suits. 2 jokers are optional.
- Internal to the class, deck is a list containing the current cards. The code using a Deck instance cannot ask for the full deck
- RANK and SUITS (and JOKERS) constants are defined at the beginning of the class
- When the using code initializes a Deck instance the Deck class fills the deck list with all the combinations of cards (plus jokers if indicated) and calls shuffle
- A deck can consist of 1 or more playing cards decks. This is used to allow games like black jack than can use several decks

## Parameters
number_of_decks: how many full decks of 52 cards. Defaults to 1.
jokers: flag to indicate if jokers are desired in the deck. Defaults to False.

## Attributes
decks: number of decks
jokers: a flag that indicates if jokers are part of the deck

## Methods
- draw(number_of_cards=1): removes and returns (as a list, in the order that weere drwan) from the top the number of cards requested. As a result the deck is `number_of_cards` cards less than before. Raises an IndexError if `number_of_cards` is larger than the cards remaining in the deck. Raises ValueError if number_of_cards is not an integer. Raises ValueError if number of cards is less than 1.
- burn: like draw, it removes the top card from the deck. Unlike draw, it does not return the card. Raises IndexError if deck is empty otherwise it returns True
- shuffle: initializes the deck (all cards) and randomizes the order of the cards
- `__str__`: Returns a human readable representation of the deck in its current state example: Deck with 37 cards
- `__len__`: Returns the number of card remaining in the deck
- cards_remaining (property): It does the same as `__len__`, but with a more human readable name
- set_cut_point(percent: float | None = None) -> None
Defines the shuffle cut point used for Blackjack-style shoe depletion.

### Rules
* Must be called on a full deck (i.e., immediately after shuffle()). If the deck is not complete, raises ValueError.

* The cut point represents the penetration percentage of the deck: The proportion of cards that may be dealt before the deck is marked as needing a shuffle.

* If percent is provided: It must be within the inclusive range [0.70, 0.80].  Otherwise, raises ValueError.

* If percent is not provided: A random value in [0.70, 0.80] is chosen.

* The number of cards to be dealt before shuffle is math.ceil(len(deck) * percent). set_cut_point is valid only on a full deck, as stated in the first rule.

* The deck maintains a boolean flag needs_shuffle, initially False.

* After each draw() operation: If cards_remaining <= cut_threshold, then needs_shuffle becomes True. Once set to True, it remains True until the deck is explicitly shuffled.

* Calling shuffle(): Resets needs_shuffle to False. Clears the current cut point (None), requiring set_cut_point() to be called again.

* The deck does not automatically shuffle when needs_shuffle becomes True.

* The decision of when to shuffle belongs to the game controller / engine, not to Deck.

## Comments
- In methods draw and burn the "top" of the deck really means the last item of the list. This makes it straightforward to use the pop() method of a list object.


# Hand class
- A hand instance is a container of cards.
- A game engine uses the Hand class to manage the cards held by each player or dealer.
- The hand class has no knowledge of the game that is being played. It does not calculate score or enforce game logic
- A hand can contain the "same" card two or more times. This can happen when the full Deck/Shoe contains 2 or more decks.
- Cards property exposes the internal list directly. Callers should not modify it directly — use add_card, remove_last_card, and clear instead.

## Responsibilities
- Holding a collection of Card instances.
- Exposing its contents in a controlled way.
- Allowing cards to be: added, removed, cleared, transferred to other containers by the game engine (e.g., discard piles, other hands).
- Keeping card management independent of any specific game.


## Attributes
- cards: a list of Card instances. It is empty when initializing the instance

## Methods
- add_card(card): adds a card to the hand list. A separate game engine needs to draw a card from the deck and add it to the hand via this method. Raises TypeError if the card given is not an instance of Card
- remove_last_card(): Removes and returns the last card added to the hand
- clear(): removes all cards from the hand
- __len__: returns the current count of cards in the hand
- cards_in_hand (property): equals `__len__`, but with a more human readable name
- __str__: string representation of cards in hand


## Comments
“DiscardPile is intentionally out of scope for v1. Card lifecycle is managed by clearing hands and shuffling the deck as needed.”

