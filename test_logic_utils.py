"""Unit tests for the corrected guessing-game logic_utils.py module.

Run with: python3 -m pytest -v
"""
import pytest

from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    update_score,
)


@pytest.mark.parametrize("difficulty, expected", [
    ("Easy", (1, 20)),
    ("Normal", (1, 100)),
    ("Hard", (1, 200)),
    ("Unknown", (1, 100)),
])
def test_difficulty_ranges(difficulty, expected):
    assert get_range_for_difficulty(difficulty) == expected


@pytest.mark.parametrize("raw, expected", [
    ("9", (True, 9, None)),
    ("-25", (True, -25, None)),
    (" 10 ", (True, 10, None)),
    ("0", (True, 0, None)),
])
def test_parse_valid_integer(raw, expected):
    assert parse_guess(raw) == expected


@pytest.mark.parametrize("raw", [None, "", "   ", "hello", "9.8", "1e2"])
def test_parse_invalid_input(raw):
    ok, value, message = parse_guess(raw)
    assert ok is False
    assert value is None
    assert isinstance(message, str) and message


@pytest.mark.parametrize("guess, secret, expected_outcome, expected_hint", [
    (9, 5, "Too High", "LOWER"),
    (9, 25, "Too Low", "HIGHER"),
    (9, 9, "Win", "Correct"),
    (9, -25, "Too High", "LOWER"),
])
def test_check_guess(guess, secret, expected_outcome, expected_hint):
    outcome, message = check_guess(guess, secret)
    assert outcome == expected_outcome
    assert expected_hint in message


@pytest.mark.parametrize("score, outcome, attempt, expected", [
    (0, "Win", 1, 90),
    (0, "Win", 5, 50),
    (0, "Win", 12, 10),
    (20, "Too High", 2, 15),
    (20, "Too Low", 3, 15),
    (20, "Other", 3, 20),
])
def test_update_score(score, outcome, attempt, expected):
    assert update_score(score, outcome, attempt) == expected
