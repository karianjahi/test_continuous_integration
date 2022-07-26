"""
This is the module that tests the count_words script
"""

# pylint: disable=R0201
# pylint: disable=W0106
import pytest
from count_words import WordCounter


class TestWordCounter:
    """
    The class that has the attrs and methods
    for testing
    """

    def test_empty_string(self):
        """
        Testing if our module can count
        zero words
        :return <None>
        """
        text = ""
        assert WordCounter(text).count_words() == 0

    def test_one_word(self):
        """
        Testing  if we can count just one word
        :return <None>
        """
        text = "nlpoblano"
        assert WordCounter(text).count_words() == 1

    def test_multiple_words(self):
        """
        Testing if we can count multiple words
        :return <None>
        """
        text = "I study at Spiced"
        assert WordCounter(text).count_words() == 4

    def test_text_enclosed_in_html(self):
        """
        Testing if our module can count words
        within a html document
        :return <None>
        """
        text = "<p> We learnt html last week </p>"
        assert WordCounter(text).count_words() == 5

    def test_html_with_attributes(self):
        """
        Same as html test but with attributes
        :return <None>
        """
        text = "<div class='poblano'> <p> This section needs to be different </p> </div>"
        assert WordCounter(text).count_words() == 6

    def test_if_we_can_count_words_amidst_symbols(self):
        """
        Testing count words on non-symbols
        :return None
        """
        text = "%$# My name %$@ is !$@$ Johannes @$@%"
        assert WordCounter(text).count_words() == 4

    def test_multiple_white_spaces(self):
        """
        Testing for multiple white spaces
        :return <None>
        """
        text = "Testing for          multiple           white   spaces"
        assert WordCounter(text).count_words() == 5

    def test_wrong_instance_type(self):
        """
        Test if the module fails when you
        introduce the wrong instance type
        :return <None>
        """
        text = ["This is a bootcamp college"]
        with pytest.raises(Exception) as error:
            WordCounter(text).count_words() == 5
        assert "input must be a string" in str(error.value)
