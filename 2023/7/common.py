from abc import ABC, abstractmethod
from collections import Counter
from dataclasses import dataclass
from enum import Enum

from common.input_data import parse_input


class Card(Enum):
    def __init__(self, face: str, rank: int):
        self.face = face
        self.rank = rank

    ACE = ("A", 13)
    KING = ("K", 12)
    QUEEN = ("Q", 11)
    JACK = ("J", 10)
    TEN = ("T", 9)
    NINE = ("9", 8)
    EIGHT = ("8", 7)
    SEVEN = ("7", 6)
    SIX = ("6", 5)
    FIVE = ("5", 4)
    FOUR = ("4", 3)
    THREE = ("3", 2)
    TWO = ("2", 1)


class HandType(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

    def __repr__(self) -> str:
        return self.name


class Hand(ABC):
    def __init__(self, string_value: str):
        self.string_value = string_value
        self.cards = self._parse_cards()
        self.hand_type = self._compute_hand_type()

    @property
    @abstractmethod
    def _use_jokers(self) -> bool:
        pass

    def _parse_cards(self) -> list[Card]:
        return [Hand._parse_card(c) for c in self.string_value]

    @staticmethod
    def _parse_card(card_name: str):
        for enum_value in Card:
            if card_name == enum_value.face:
                return enum_value

    def __repr__(self) -> str:
        return f"{self.string_value} {self.hand_type}"

    def __hash__(self) -> int:
        return self.string_value.__hash__()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Hand):
            return False

        return self.string_value == other.string_value

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Hand):
            return False

        if self == other:
            return False

        if self.hand_type.value > other.hand_type.value:
            return True

        if self.hand_type.value < other.hand_type.value:
            return False

        for left_card, right_card in zip(self.cards, other.cards):

            def _get_rank(card: Card) -> int:
                if card == Card.JACK and self._use_jokers:
                    return 0

                return card.rank

            if _get_rank(left_card) == _get_rank(right_card):
                continue

            return _get_rank(left_card) > _get_rank(right_card)

    def __lt__(self, other: object) -> bool:
        return not self.__gt__(other)

    def _compute_hand_type(self) -> HandType:
        counter_values = sorted(list(Counter(self.cards).values()))

        if counter_values == [5]:
            return HandType.FIVE_OF_A_KIND

        if counter_values == [1, 4]:
            return HandType.FOUR_OF_A_KIND

        if counter_values == [2, 3]:
            return HandType.FULL_HOUSE

        if counter_values == [1, 1, 3]:
            return HandType.THREE_OF_A_KIND

        if counter_values == [1, 2, 2]:
            return HandType.TWO_PAIR

        if counter_values == [1, 1, 1, 2]:
            return HandType.ONE_PAIR

        if counter_values == [1, 1, 1, 1, 1]:
            return HandType.HIGH_CARD

        raise ValueError(f"Could not compute hand type for {self.string_value}")


@dataclass
class HandBet:
    hand: Hand
    bid: int


def parse_hand_bets(hand_type: type) -> list[HandBet]:
    lines = parse_input(__file__)
    return [_parse_hand_bet(line, hand_type) for line in lines]


def _parse_hand_bet(line: str, hand_type: type) -> HandBet:
    hand_str, bid = line.split(" ")

    return HandBet(hand=hand_type(hand_str), bid=int(bid))


def main(hand_type: type):
    hand_bets = parse_hand_bets(hand_type)
    hand_bets = sorted(hand_bets, key=lambda h: h.hand)
    result = sum((i + 1) * h.bid for i, h in enumerate(hand_bets))

    print(result)
