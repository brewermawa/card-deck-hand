import pytest

from dataclasses import FrozenInstanceError

from card import Card

class TestCard:
    @pytest.mark.parametrize(
        "rank, suit",
        [("2", "♦"), ("K", "♣"), ("8", "♠"), ("7", "♥")]
    )
    def test_card_created_successfully(self, rank, suit):
        card = Card(rank, suit)

        assert card.rank == rank
        assert card.suit == suit

    
    @pytest.mark.parametrize(
        "rank",
        [123, None, True, [1, 2]]
    )
    def test_card_raises_typeerror_when_rank_not_string(self, rank):
        with pytest.raises(TypeError):
            Card(rank, "♠")

    
    @pytest.mark.parametrize(
        "suit",
        [123, None, True, [1, 2]]
    )
    def test_card_raises_typeerror_when_suit_not_string(self, suit):
        with pytest.raises(TypeError):
            Card("A", suit)

    @pytest.mark.parametrize(
        "rank",
        ["X", "13", ""]
    )
    def test_card_raises_valueerror_if_rank_not_valid(self, rank):
        with pytest.raises(ValueError):
            Card(rank, "♠")


    @pytest.mark.parametrize(
        "suit",
        ["spades", "diamonds", ""]
    )
    def test_card_raises_valueerror_if_suit_not_valid(self, suit):
        with pytest.raises(ValueError):
            Card("A", suit)

    @pytest.mark.parametrize(
        "attr, value",
        [
            ("rank", "J"),
            ("suit", "♠")
        ]
    )
    def test_card_raises_frozeninstanceerror_when_trying_to_modify_card(self, attr, value):
        card = Card("A", "♠")

        with pytest.raises(FrozenInstanceError):
            setattr(card, attr, value)

    
    def test_card_string_representation_is_accurate(self):
        card = Card("A", "♠")

        assert str(card) == "A♠"


    def test_card_two_cards_with_same_rank_and_suit_are_equal(self):
        card1 = Card("A", "♠")
        card2 = Card("A", "♠")

        assert card1 == card2


    def test_card_two_different_cards_are_not_equal(self):
        card1 = Card("A", "♠")
        card2 = Card("A", "♥")

        assert card1 != card2

    
    def test_card_set_initialized_with_two_equal_cards_has_len_1(self):
        assert len({Card("A", "♠"), Card("A", "♠")}) == 1


    def test_card_set_initialized_with_two_different_cards_has_len_2(self):
        assert len({Card("A", "♠"), Card("A", "♥")}) == 2


    @pytest.mark.parametrize(
        "rank, suit",
        [("2", "🃏"), ("K", "🃏"), ("A", "🃏")]
    )
    def test_card_raises_value_error_invalid_combination_face_and_joker_suit(self, rank, suit):
        with pytest.raises(ValueError):
            card = Card(rank, suit)


    @pytest.mark.parametrize(
        "rank, suit",
        [("Joker", "♣"), ("Joker", "♦"), ("Joker", "♠"), ("Joker", "♥")]
    )
    def test_card_raises_value_error_invalid_combination_joker_any_suit(self, rank, suit):
        with pytest.raises(ValueError):
            card = Card(rank, suit)


    def test_card_accepts_joker_with_joker_suit(self):
        card_with_joker = Card("Joker", "🃏")

        assert card_with_joker.rank == "Joker"
        assert card_with_joker.suit == "🃏"

