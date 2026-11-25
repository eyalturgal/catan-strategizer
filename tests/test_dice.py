"""Checks that counting dice rolls in code gives the known Catan pip table."""

from fractions import Fraction

import pytest

from catan.board.dice import NUMBER_TOKENS, pips, roll_counts, roll_probability


def test_two_dice_have_36_outcomes():
    assert sum(roll_counts().values()) == 36


def test_counts_match_the_known_table():
    assert roll_counts() == {
        2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1,
    }


def test_seven_is_one_in_six():
    assert roll_probability(7) == Fraction(1, 6)


def test_all_chances_add_up_to_one():
    assert sum(roll_probability(t) for t in range(2, 13)) == 1


@pytest.mark.parametrize(
    "number, expected",
    [(2, 1), (12, 1), (3, 2), (11, 2), (4, 3), (10, 3), (5, 4), (9, 4), (6, 5), (8, 5)],
)
def test_pips_per_token(number, expected):
    assert pips(number) == expected


def test_standard_tokens_total_58_pips():
    assert len(NUMBER_TOKENS) == 18
    assert sum(pips(n) for n in NUMBER_TOKENS) == 58


def test_seven_has_no_token():
    with pytest.raises(ValueError):
        pips(7)
