#!/usr/bin/env python3.7
"""
Blackjack Hand class.
"""
from typing import List, Union, Optional, cast, overload, Tuple

from Card import Card


# class Hand:
#     """
#     Uses a complex __init__() method with multiple strategies for initialization.
#     """
#
#     @overload
#     def __init__(self, arg1: "Hand") -> None:
#         ...
#
#     @overload
#     def __init__(self, arg1: "Hand", arg2: Card, *, split: int) -> None:
#         ...
#
#     @overload
#     def __init__(self, arg1: Card, arg2: Card, arg3: Card) -> None:
#         ...
#
#     def __init__(
#             self,
#             arg1: Union["Hand", Card],
#             arg2: Optional[Card] = None,
#             arg3: Optional[Card] = None,
#             split: Optional[int] = None,
#     ) -> None:
#         self.dealer_card: Card
#         self.cards: List[Card]
#
#         if isinstance(arg1, Hand):
#             # Clone an existing hand
#             self.dealer_card = arg1.dealer_card
#             self.cards = arg1.cards
#
#         elif isinstance(arg1, Hand) and isinstance(arg2, Card) and split is not None:
#             # Split an existing hand
#             self.dealer_card = arg1.dealer_card
#             self.cards = [arg1.cards[split], arg2]
#
#         elif isinstance(arg1, Card) and isinstance(arg2, Card) and isinstance(arg3, Card):
#             # Build a fresh, new hand from three cards
#             self.dealer_card = arg1
#             self.cards = [arg2, arg3]
#
#         else:
#             raise TypeError("Invalid constructor {arg1!r} {arg2!r} {arg3!r}")
#
#     def __str__(self) -> str:
#         return ", ".join(map(str, self.cards))
#
#     def __repr__(self):
#         return f"{self.__class__.__name__} ({self.dealer_card!r}, *{self.cards})"

class Hand5:

    def __init__(self, dealer_card: Card, *cards: Card) -> None:
        self.dealer_card = dealer_card
        self.cards = cards

    @staticmethod
    def freeze(other) -> "Hand5":
        hand = Hand5(other.dealer_card, *other.cards)
        return hand

    @staticmethod
    def split(other, card0, card1) -> Tuple["Hand5", "Hand5"]:
        hand0 = Hand5(other.dealer_card, other.cards[0], card0)
        hand1 = Hand5(other.dealer_card, other.cards[1], card1)
        return hand0, hand1

    def __str__(self) -> str:
        return ", ".join(map(str, self.cards))
