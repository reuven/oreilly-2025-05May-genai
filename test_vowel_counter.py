# test_vowel_counter.py
# Tests for the count_vowels function

import pytest
from count_vowels import count_vowels

def test_empty_string():
    """Test that an empty string returns zeros for all vowels."""
    result = count_vowels("")
    expected = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    assert result == expected

def test_no_vowels():
    """Test that a string with no vowels returns zeros for all vowels."""
    result = count_vowels("xyz")
    expected = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    assert result == expected

def test_single_vowel():
    """Test strings with just one vowel."""
    test_cases = [
        ("a", {'a': 1, 'e': 0, 'i': 0, 'o': 0, 'u': 0}),
        ("e", {'a': 0, 'e': 1, 'i': 0, 'o': 0, 'u': 0}),
        ("i", {'a': 0, 'e': 0, 'i': 1, 'o': 0, 'u': 0}),
        ("o", {'a': 0, 'e': 0, 'i': 0, 'o': 1, 'u': 0}),
        ("u", {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 1})
    ]
    
    for input_str, expected in test_cases:
        assert count_vowels(input_str) == expected

def test_multiple_vowels():
    """Test a string with multiple vowels."""
    result = count_vowels("hello")
    expected = {'a': 0, 'e': 1, 'i': 0, 'o': 1, 'u': 0}
    assert result == expected

def test_repeated_vowels():
    """Test a string with repeated vowels."""
    result = count_vowels("banana")
    expected = {'a': 3, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    assert result == expected

def test_all_vowels():
    """Test a string containing all vowels."""
    result = count_vowels("education")
    expected = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
    assert result == expected

def test_case_sensitivity():
    """Test that the function is case-sensitive (uppercase vowels aren't counted)."""
    result = count_vowels("ApplE")
    expected = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}  # Since 'A' and 'E' are uppercase
    assert result == expected

def test_with_punctuation():
    """Test a string with punctuation and spaces."""
    result = count_vowels("Hello, world!")
    expected = {'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0}
    assert result == expected

def test_with_numbers():
    """Test a string containing numbers."""
    result = count_vowels("abc123")
    expected = {'a': 1, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    assert result == expected

def test_long_text():
    """Test with a longer piece of text."""
    text = "the quick brown fox jumps over the lazy dog"
    result = count_vowels(text)
    expected = {'a': 1, 'e': 3, 'i': 1, 'o': 4, 'u': 2}
    assert result == expected
