"""Dice odds for two six-sided dice, found by counting every possible roll.

Two dice have 6 x 6 = 36 equally likely outcomes. The number of outcomes that
add up to a total is that total's "pips": the dots printed on a number token.
"""

from collections import Counter
from fractions import Fraction

# The 18 number tokens in classic Catan: one 2, one 12, two of each other number.
# There is no 7 token: a 7 moves the robber instead of producing resources.
NUMBER_TOKENS = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]


def roll_counts() -> dict[int, int]:
    """How many of the 36 possible rolls make each total from 2 to 12."""
    counts = Counter(a + b for a in range(1, 7) for b in range(1, 7))
    return dict(sorted(counts.items()))


def roll_probability(total: int) -> Fraction:
    """Chance of rolling this total, as an exact fraction (for example 7 gives 1/6)."""
    return Fraction(roll_counts().get(total, 0), 36)


def pips(number: int) -> int:
    """Pips on a number token: how many of the 36 rolls produce that number."""
    if number not in NUMBER_TOKENS:
        raise ValueError(f"{number} is not a Catan number token")
    return roll_counts()[number]
