from math import ceil

import pytest

from card import Card
from deck import Deck

class TestDeck:
    def test_deck_new_deck_must_have_52_cards(self):
        deck = Deck()
        assert len(deck) == 52

    def test_deck_new_deck_with_jokers_must_have_54_cards(self):
        deck = Deck(jokers=True)
        assert len(deck) == 54

    def test_deck_6_decks_must_have_312_cards(self):
        deck = Deck(6)
        assert len(deck) == 312

    def test_deck_6_deck_with_jokers_must_have_324_cards(self):
        deck = Deck(number_of_decks=6, jokers=True)
        assert len(deck) == 324


    @pytest.mark.parametrize(
        "number_of_decks",
        ["1", None, True, 1.5]
    )
    def test_deck_raises_typeerror_when_number_of_decks_not_int(self, number_of_decks):
        with pytest.raises(TypeError):
            deck = Deck(number_of_decks)

    @pytest.mark.parametrize(
        "number_of_decks",
        [0, -1]
    )
    def test_deck_raises_valueerror_when_number_of_decks_less_than_one(self, number_of_decks):
        with pytest.raises(ValueError):
            deck = Deck(number_of_decks)

    def test_deck_draw_returns_list(self):
        deck = Deck()
        cards_drawn = deck.draw(5)
        assert isinstance(cards_drawn, list) is True

    def test_deck_draw_five_returns_list_of_len_five(self):
        deck = Deck()
        cards_drawn = deck.draw(5)
        assert len(cards_drawn) == 5

    def test_deck_draw_one_returns_list_with_one_card_instance(self):
        deck = Deck()
        card = deck.draw()[0]
        assert isinstance(card, Card) is True

    def test_deck_draw_five_returns_list_with_five_card_instances(self):
        deck = Deck()
        cards_drawn = deck.draw(5)
        all_cards = all(isinstance(card, Card) for card in cards_drawn)
        assert all_cards is True

    def test_deck_after_draw_one_deck_len_is_one_less(self):
        deck = Deck() 
        original_len = len(deck)
        deck.draw()
        assert original_len - len(deck) == 1

    def test_deck_after_draw_five_deck_len_is_five_less(self):
        deck = Deck() 
        original_len = len(deck)
        deck.draw(5)
        assert original_len - len(deck) == 5

    def test_deck_raises_indexerror_when_drawing_on_empty_deck(self):
        deck = Deck()
        for _ in range(52):
            deck.draw()

        len_before = len(deck)

        with pytest.raises(IndexError):
            deck.draw()

        assert len_before == len(deck)
        assert deck.cards_remaining == len(deck)

    def test_deck_raises_indexerror_when_drawing_more_than_cards_remaining(self):
        deck = Deck()
        for _ in range(48):
            deck.draw()

        len_before = len(deck)

        with pytest.raises(IndexError):
            deck.draw(5)

        assert len_before == len(deck)
        assert deck.cards_remaining == len(deck)

    @pytest.mark.parametrize(
        "cards_to_draw",
        ["1", None, True, 1.5]
    )
    def test_deck_draw_raises_typeerror_when_number_of_cards_to_draw_is_not_int(self, cards_to_draw):
        deck = Deck()
        len_before = len(deck)
        
        with pytest.raises(TypeError):
            deck.draw(cards_to_draw)

        assert len_before == len(deck)
        assert deck.cards_remaining == len(deck)

    @pytest.mark.parametrize(
        "cards_to_draw",
        [0, -1]
    )
    def test_deck_draw_raises_valueerror_when_number_of_cards_is_less_than_1(self, cards_to_draw):
        deck = Deck()
        len_before = len(deck)

        with pytest.raises(ValueError):
            deck.draw(cards_to_draw)

        assert len_before == len(deck)
        assert deck.cards_remaining == len(deck)

    def test_deck_after_burn_deck_len_is_one_less(self):
        deck = Deck() 
        original_len = len(deck)
        burn_success = deck.burn()
        assert original_len - len(deck) == 1
        assert burn_success is True

    def test_deck_raises_indexerror_when_burning_on_empty_deck(self):
        deck = Deck()
        for _ in range(52):
            deck.burn()

        len_before = len(deck)

        with pytest.raises(IndexError):
            deck.burn()

        assert len_before == len(deck)
        assert deck.cards_remaining == len(deck)

    def test_deck_len_and_cards_remaining_are_equal(self):
        deck = Deck()
        assert len(deck) == deck.cards_remaining

    def test_deck_len_and_cards_remaining_are_equal_after_draw_and_burn(self):
        deck = Deck()
        deck.draw(5)
        deck.burn()
        deck.draw(3)
        assert len(deck) == deck.cards_remaining

    def test_deck_after_shuffle_len_is_the_same_as_initial_deck(self):
        deck = Deck()
        original_len = len(deck)
        deck.shuffle()
        len_after_shuffle = len(deck)
        assert original_len == len_after_shuffle

    #Tests for cut_point

    def test_deck_raises_valueerror_when_cut_on_a_non_full_deck(self):
        deck = Deck()
        deck.draw(5)

        with pytest.raises(ValueError):
            deck.set_cut_point(percent=0.75)


    @pytest.mark.parametrize(
        "percent",
        [0.69, 0.81, 0, 0.99]
    )
    def test_deck_raises_valueerror_when_set_cut_point_percent_out_of_range(self, percent):
        deck = Deck()
        
        with pytest.raises(ValueError):
            deck.set_cut_point(percent=percent)

    def test_deck_needs_shuffle_becomes_true_when_threshold_is_reached(self):
        deck = Deck() #52 cards
        percent=0.75
        deck.set_cut_point(percent=percent)
        cards_to_deal = ceil(52 * percent)
        threshold_remaining = 52 - cards_to_deal

        for _ in range(0, cards_to_deal - 1):
            deck.draw()

        assert len(deck) > threshold_remaining
        assert deck.needs_shuffle is False
        deck.draw()
        assert len(deck) <= threshold_remaining
        assert deck.needs_shuffle is True

    def test_deck_needs_shuffle_remains_true_after_more_draws(self):
        deck = Deck() #52 cards
        percent=0.75
        deck.set_cut_point(percent=percent)
        cards_to_deal = ceil(52 * percent)
        threshold_remaining = 52 - cards_to_deal

        for _ in range(0, cards_to_deal):
            deck.draw()

        assert len(deck) <= threshold_remaining
        assert deck.needs_shuffle is True
        deck.draw()
        assert deck.needs_shuffle is True

    def test_deck_shuffle_cleans_cut_point(self):
        deck = Deck()
        cards_to_deal = len(deck) - 1
        percent=0.75
        deck.set_cut_point(percent=percent)
        deck.shuffle()

        for _ in range(0, cards_to_deal):
            deck.draw()

        assert deck.needs_shuffle is False


    def test_deck_needs_shuffle_is_false_on_new_deck(self):
        deck = Deck()
        assert deck.needs_shuffle is False

    def test_deck_shuffle_sets_needs_shuffle_to_False(self):
        deck = Deck() #52 cards
        percent = 0.75
        cards_to_deal = ceil(52 * percent)
        deck.set_cut_point(percent=percent)

        for _ in range(0, cards_to_deal):
            deck.draw()

        assert deck.needs_shuffle is True
        deck.shuffle()
        assert deck.needs_shuffle is False


    def test_deck_needs_shuffle_remains_false_if_cut_point_not_set(self):
        deck = Deck() #52 cards
        cards_to_deal = len(deck) - 1

        for _ in range(0, cards_to_deal):
            deck.draw()

        assert deck.needs_shuffle is False

    def test_deck_raise_valueerror_when_setting_set_point_twice(self):
        deck = Deck()
        deck.set_cut_point(percent=0.75)

        with pytest.raises(ValueError):
            deck.set_cut_point(percent=0.80)
