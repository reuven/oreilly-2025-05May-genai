# test_piglatin.py
# Corrected tests for the pl_word and pl_sentence functions

import pytest
from piglatin import pl_word, pl_sentence

class TestPlWord:
    """Tests for the pl_word function."""
    
    @pytest.mark.parametrize("input_word, expected_output, test_description", [
        # Words starting with vowels
        ("apple", "appleway", "Word starting with 'a'"),
        ("elephant", "elephantway", "Word starting with 'e'"),
        ("igloo", "iglooway", "Word starting with 'i'"),
        ("orange", "orangeway", "Word starting with 'o'"),
        ("umbrella", "umbrellaway", "Word starting with 'u'"),
        
        # Words starting with consonants
        ("computer", "omputercay", "Word starting with 'c'"),
        ("papaya", "apayapay", "Word starting with 'p'"),
        ("hello", "ellohay", "Word starting with 'h'"),
        ("dog", "ogday", "Short word starting with consonant"),
        
        # Examples from your code
        ("computer", "omputercay", "Example from your code - computer"),
        ("apple", "appleway", "Example from your code - apple"),
        ("papaya", "apayapay", "Example from your code - papaya"),
        ("elephant", "elephantway", "Example from your code - elephant"),
    ])
    def test_pl_word_basic(self, input_word, expected_output, test_description):
        """Test pl_word with basic inputs."""
        result = pl_word(input_word)
        assert result == expected_output, f"Failed on test: {test_description}"

    def test_pl_word_with_empty_string(self):
        """Test that passing an empty string raises an IndexError."""
        with pytest.raises(IndexError):
            pl_word("")
    
    @pytest.mark.parametrize("test_input, test_description", [
        (None, "None input"),
        (123, "Integer input"),
        (["h", "e", "l", "l", "o"], "List input"),
    ])
    def test_pl_word_invalid_inputs(self, test_input, test_description):
        """Test that passing invalid inputs raises appropriate exceptions."""
        with pytest.raises((AttributeError, TypeError)):
            pl_word(test_input)


class TestPlSentence:
    """Tests for the pl_sentence function."""
    
    @pytest.mark.parametrize("input_sentence, expected_output, test_description", [
        # Basic sentences
        ("hello world", "ellohay orldway", "Basic two-word sentence"),
        ("this is a test", "histay siay away esttay", "Four-word sentence"),
        
        # Example from your code - CORRECTED expected output
        ("this is a very interesting demo of chatbots", 
         "histay siay away eryvay interestingway emoday ofway hatbotscay", 
         "Example from your code"),
        
        # Sentences with words starting with vowels
        ("an apple a day", "anway appleway away ayday", "Sentence with words starting with vowels"),
        
        # Sentences with mixed vowel/consonant starts
        ("python is awesome", "ythonpay siay awesomeway", "Mixed vowel/consonant starts"),
        
        # Single word sentences
        ("hello", "ellohay", "Single word - consonant start"),
        ("apple", "appleway", "Single word - vowel start"),
    ])
    def test_pl_sentence_basic(self, input_sentence, expected_output, test_description):
        """Test pl_sentence with basic inputs."""
        result = pl_sentence(input_sentence)
        assert result == expected_output, f"Failed on test: {test_description}"
    
    def test_pl_sentence_empty_string(self):
        """Test pl_sentence with an empty string."""
        result = pl_sentence("")
        assert result == "", "Empty string should return empty string"
    
    @pytest.mark.parametrize("test_input, test_description", [
        (None, "None input"),
        (123, "Integer input"),
        (["hello", "world"], "List input"),
    ])
    def test_pl_sentence_invalid_inputs(self, test_input, test_description):
        """Test that passing invalid inputs raises appropriate exceptions."""
        with pytest.raises((AttributeError, TypeError)):
            pl_sentence(test_input)
    
    def test_pl_sentence_with_multiple_spaces(self):
        """Test handling of multiple spaces between words."""
        input_sentence = "hello  world"
        # Your implementation will create ["hello", "", "world"] when splitting
        # Empty strings will cause IndexError when passed to pl_word
        with pytest.raises(IndexError):
            pl_sentence(input_sentence)
