# test_piglatin.py
# Tests for the pl_word and pl_sentence functions based on the actual implementation

import pytest
from piglatin import pl_word, pl_sentence

class TestPlWord:
    """Tests for the pl_word function."""
    
    @pytest.mark.parametrize("input_word, expected_output, test_description", [
        # Words starting with vowels (add 'way')
        ("apple", "appleway", "Word starting with 'a'"),
        ("elephant", "elephantway", "Word starting with 'e'"),
        ("igloo", "iglooway", "Word starting with 'i'"),
        ("orange", "orangeway", "Word starting with 'o'"),
        ("umbrella", "umbrellaway", "Word starting with 'u'"),
        
        # Words starting with consonants (move first letter to end and add 'ay')
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

    def test_pl_word_with_index_error(self):
        """Test that passing an empty string raises an IndexError."""
        with pytest.raises(IndexError):
            pl_word("")
    
    def test_pl_word_none_input(self):
        """Test that passing None raises an AttributeError."""
        with pytest.raises(AttributeError):
            pl_word(None)
    
    def test_pl_word_non_string_input(self):
        """Test that passing non-string inputs raises an AttributeError."""
        with pytest.raises(AttributeError):
            pl_word(123)

class TestPlSentence:
    """Tests for the pl_sentence function."""
    
    @pytest.mark.parametrize("input_sentence, expected_output, test_description", [
        # Basic sentences
        ("hello world", "ellohay orldway", "Basic two-word sentence"),
        ("this is a test", "histay siay away esttay", "Four-word sentence"),
        
        # Example from your code
        ("this is a very interesting demo of chatbots", 
         "histay siay away eryvay nterestingiay emoday foay hatbotscay", 
         "Example from your code"),
        
        # Sentences with words starting with vowels
        ("an apple a day", "nay appleway away ayday", "Sentence with words starting with vowels"),
        
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
    
    def test_pl_sentence_none_input(self):
        """Test that passing None raises an AttributeError."""
        with pytest.raises(AttributeError):
            pl_sentence(None)
    
    def test_pl_sentence_non_string_input(self):
        """Test that passing non-string inputs raises an AttributeError."""
        with pytest.raises(AttributeError):
            pl_sentence(123)
    
    def test_pl_sentence_with_multiple_spaces(self):
        """Test that multiple spaces are handled correctly."""
        input_sentence = "hello  world"
        expected_output = "ellohay  orldway"
        result = pl_sentence(input_sentence)
        assert result == expected_output, "Multiple spaces should be preserved"
