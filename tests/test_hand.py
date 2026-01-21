import pytest

from hand import Hand
from card import Card

class TestHand:
    
    def test_hand_cards_is_empty_when_initialized(self):
        hand = Hand()
        assert hand.cards == []

    def test_hand_add_card_increments_count_by_one(self):
        card = Card("A", "♦")
        hand = Hand()
        len_before_add = len(hand)
        hand.add_card(card)

        assert len(hand) == len_before_add + 1

    @pytest.mark.parametrize(
        "card",
        ["1", ("A", "♦"), ["A", "♦"], {"rank": "A", "suit": "♦"}, None]
    )
    def test_hand_add_card_raises_typeerror_if_not_given_card_instance(self, card):
        hand = Hand()

        with pytest.raises(TypeError):
            hand.add_card(card)

    def test_hand_remove_last_card_decrements_count_by_one(self):
        hand = Hand()
        first_card = Card("A", "♦")
        hand.add_card(first_card)
        second_card = Card("J", "♦")
        hand.add_card(second_card)
        len_before_remove = len(hand)
        hand.remove_last_card()

        assert len(hand) == len_before_remove - 1

    def test_hand_remove_last_card_returns_card_instance(self):
        hand = Hand()
        first_card_added = Card("A", "♦")
        hand.add_card(first_card_added)
        last_card_added = Card("J", "♦")
        hand.add_card(last_card_added)
        removed_card = hand.remove_last_card()

        assert isinstance(removed_card, Card) is True
        assert last_card_added is removed_card
        assert first_card_added is hand.cards[0]

    def test_hand_remove_last_card_raises_valueerror_when_hand_is_empty(self):
        hand = Hand()

        with pytest.raises(ValueError):
            hand.remove_last_card()

    def test_hand_clear_sets_cards_to_empty(self):
        hand = Hand()
        first_card = Card("A", "♦")
        hand.add_card(first_card)
        second_card = Card("J", "♦")
        hand.add_card(second_card)
        hand.clear()

        assert hand.cards == []
        assert len(hand) == 0

    def test_hand_cards_in_hand_property_equals_len(self):
        hand = Hand()
        first_card = Card("A", "♦")
        hand.add_card(first_card)
        second_card = Card("J", "♦")
        hand.add_card(second_card)

        assert hand.cards_in_hand == len(hand)

    def test_hand_str_includes_each_card_string_representation(self):
        hand = Hand()
        first_card = Card("A", "♦")
        hand.add_card(first_card)
        second_card = Card("J", "♦")
        hand.add_card(second_card)

        assert str(first_card) in str(hand)
        assert str(second_card) in str(hand)
