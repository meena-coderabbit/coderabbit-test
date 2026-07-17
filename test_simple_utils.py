"""Unit tests for simple_utils.py."""

import math

import pytest

from simple_utils import celsius_to_fahrenheit, count_words, reverse_string


class TestReverseString:
    def test_reverses_simple_word(self):
        assert reverse_string("hello") == "olleh"

    def test_reverses_sentence_with_spaces(self):
        assert reverse_string("hello world") == "dlrow olleh"

    def test_empty_string_returns_empty_string(self):
        assert reverse_string("") == ""

    def test_single_character_returns_same_character(self):
        assert reverse_string("a") == "a"

    def test_palindrome_returns_same_string(self):
        assert reverse_string("racecar") == "racecar"

    def test_string_with_punctuation_and_numbers(self):
        assert reverse_string("abc123!?") == "?!321cba"

    def test_string_with_unicode_characters(self):
        assert reverse_string("héllo") == "olléh"

    def test_does_not_mutate_input_type(self):
        original = "immutable"
        result = reverse_string(original)
        assert original == "immutable"
        assert result == "elbatummi"


class TestCountWords:
    def test_counts_words_in_simple_sentence(self):
        assert count_words("The quick brown fox") == 4

    def test_single_word_returns_one(self):
        assert count_words("hello") == 1

    def test_empty_string_returns_zero(self):
        assert count_words("") == 0

    def test_whitespace_only_string_returns_zero(self):
        assert count_words("   ") == 0

    def test_multiple_spaces_between_words_collapsed(self):
        assert count_words("hello    world") == 2

    def test_leading_and_trailing_whitespace_ignored(self):
        assert count_words("  hello world  ") == 2

    def test_tabs_and_newlines_treated_as_whitespace(self):
        assert count_words("hello\tworld\nfoo") == 3

    def test_counts_words_with_punctuation_as_single_tokens(self):
        assert count_words("Hello, world!") == 2


class TestCelsiusToFahrenheit:
    def test_freezing_point_of_water(self):
        assert celsius_to_fahrenheit(0) == 32

    def test_boiling_point_of_water(self):
        assert celsius_to_fahrenheit(100) == 212

    def test_body_temperature(self):
        assert math.isclose(celsius_to_fahrenheit(37), 98.6)

    def test_negative_temperature(self):
        assert celsius_to_fahrenheit(-40) == -40

    def test_returns_float_for_fractional_result(self):
        result = celsius_to_fahrenheit(10)
        assert math.isclose(result, 50.0)

    @pytest.mark.parametrize(
        "celsius, expected_fahrenheit",
        [
            (0, 32),
            (100, 212),
            (-40, -40),
            (20, 68),
            (-273.15, -459.67),
        ],
    )
    def test_various_conversions(self, celsius, expected_fahrenheit):
        assert math.isclose(celsius_to_fahrenheit(celsius), expected_fahrenheit, rel_tol=1e-9, abs_tol=1e-9)