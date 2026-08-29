"""
Exercise: Shuffle & Deal
------------------------
1. Build a standard 52-card deck as a list of strings like "10 of Hearts", "Ace of Spades".
   Suits: Hearts, Diamonds, Clubs, Spades. Ranks: 2-10, Jack, Queen, King, Ace.
2. Write `build_deck() -> list[str]` returning the full 52-card deck (any fixed order).
3. Write `deal_hands(deck, num_players, hand_size) -> list[list[str]]` that:
   - shuffles a COPY of the deck (never mutate the caller's original deck)
   - deals `num_players` hands of `hand_size` cards each, with no repeated cards across hands
   - returns a list of hands (a list of lists)

Try it yourself before peeking at solutions/tier1_general/ex02_shuffle_deck.py.
"""

import random

SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


def build_deck() -> list[str]:
    # TODO: return all 52 "{rank} of {suit}" strings
    # list = []
    # for _suits in SUITS:
    #     for _rank in RANKS:
    #         list.append(f"{_rank} of {_suits}")
    # return list
    return [f"{_rank} of {_suits}" for _suits in SUITS for _rank in RANKS]


def deal_hands(deck: list[str], num_players: int, hand_size: int) -> list[list[str]]:
    # TODO: copy + shuffle the deck, then deal hands with no repeated cards
    shuffle = deck.copy()
    random.shuffle(shuffle)

    hands = []
    for _ in range(num_players):
        hand = [shuffle.pop() for _ in range(hand_size)]
        hands.append(hand)
    return hands


if __name__ == "__main__":
    deck = build_deck()
    hands = deal_hands(deck, num_players=4, hand_size=13)
    for i, hand in enumerate(hands, start=1):
        print(f">> Player {i}: {hand}")
