from enum import IntEnum, unique
from collections import Counter

RANKS = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 11, "Q": 12, "K": 13, "A": 14
}

@unique
class HandRank(IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9
    ROYAL_FLUSH = 10


class Hand:
    def __init__(self, hand_str):
        cards = hand_str.split()
        self.cards = [RANKS[c[:-1]] for c in cards]
        self.suits = [c[-1] for c in cards]
        self.hand_str = hand_str

        self.cards.sort()
        self.same_suit = len(set(self.suits)) == 1
        self.counts = Counter(self.cards)

        self.rank, self.rank_value = self.evaluate()

    def __lt__(self, other):
        return (self.rank, self.rank_value) < (other.rank, other.rank_value)

    def __eq__(self, other):
        return (self.rank, self.rank_value) == (other.rank, other.rank_value)

    def is_straight(self):
        ranks = self.cards
        # Handle low-Ace straight: [2, 3, 4, 5, 14]
        if ranks == [2, 3, 4, 5, 14]:
            return True, 5
        if all(ranks[i] + 1 == ranks[i + 1] for i in range(4)):
            return True, ranks[-1]
        return False, None

    def evaluate(self):
        is_straight, high = self.is_straight()
        same_suit = self.same_suit
        counts = self.counts.most_common()

        if same_suit and is_straight:
            if high == 14:
                return HandRank.ROYAL_FLUSH, ()
            return HandRank.STRAIGHT_FLUSH, (high,)

        if counts[0][1] == 4:
            return HandRank.FOUR_OF_A_KIND, (counts[0][0], counts[1][0])

        if counts[0][1] == 3 and counts[1][1] == 2:
            return HandRank.FULL_HOUSE, (counts[0][0], counts[1][0])

        if same_suit:
            return HandRank.FLUSH, tuple(sorted(self.cards, reverse=True))

        if is_straight:
            return HandRank.STRAIGHT, (high,)

        if counts[0][1] == 3:
            rest = sorted([r for r, c in counts if c == 1], reverse=True)
            return HandRank.THREE_OF_A_KIND, (counts[0][0], *rest)

        if counts[0][1] == 2 and counts[1][1] == 2:
            pair_ranks = sorted([r for r, c in counts if c == 2], reverse=True)
            kicker = [r for r, c in counts if c == 1][0]
            return HandRank.TWO_PAIR, (*pair_ranks, kicker)

        if counts[0][1] == 2:
            rest = sorted([r for r, c in counts if c == 1], reverse=True)
            return HandRank.ONE_PAIR, (counts[0][0], *rest)

        return HandRank.HIGH_CARD, tuple(sorted(self.cards, reverse=True))


def best_hands(hands):
    hands = [Hand(h) for h in hands]
    best = max(hands)
    return [h.hand_str for h in hands if h == best]
