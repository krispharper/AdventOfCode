from collections import Counter

from .common import Hand, HandType, main, parse_hand_bets


class Hand1(Hand):
    @property
    def _use_jokers(self) -> bool:
        return False


if __name__ == "__main__":
    main(hand_type=Hand1)
