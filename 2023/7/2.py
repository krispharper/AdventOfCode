from collections import Counter

from .common import Card, Hand, HandType, main, parse_hand_bets


class Hand2(Hand):
    @property
    def _use_jokers(self) -> bool:
        return True

    def _compute_hand_type(self) -> HandType:
        base_value = super()._compute_hand_type()
        jack_count = Counter(self.cards).get(Card.JACK)

        if not jack_count:
            return base_value

        if base_value == HandType.FIVE_OF_A_KIND:
            return base_value

        if base_value == HandType.FOUR_OF_A_KIND:
            return HandType.FIVE_OF_A_KIND

        if base_value == HandType.FULL_HOUSE:
            return HandType.FIVE_OF_A_KIND

        if base_value == HandType.THREE_OF_A_KIND:
            if jack_count == 1:
                return HandType.FOUR_OF_A_KIND

            if jack_count == 2:
                raise ValueError(f"Can't have two Jacks and three of a kind")

            if jack_count == 3:
                return HandType.FOUR_OF_A_KIND

        if base_value == HandType.TWO_PAIR:
            if jack_count == 1:
                return HandType.FULL_HOUSE

            if jack_count == 2:
                return HandType.FOUR_OF_A_KIND

        if base_value == HandType.ONE_PAIR:
            return HandType.THREE_OF_A_KIND

        if base_value == HandType.HIGH_CARD:
            return HandType.ONE_PAIR

        raise ValueError(f"Could not compute hand type for {self.string_value}")


if __name__ == "__main__":
    main(hand_type=Hand2)
