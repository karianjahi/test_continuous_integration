"""
This module counts the no. of words in a sentence
"""

import re
from bs4 import BeautifulSoup


class WordCounter:
    """
    This is the class that contains the attributes
    and methods for word counting
    """

    def __init__(self, text):
        """
        Class constructor
        :param text: <str>  text is a string
        :return <None>
        """
        assert isinstance(text, str), "input must be a string"
        self.text = text

    def __repr__(self):
        """
        Representative method
        """
        return f"Text to count: {self.text}"

    def count_words(self):
        """
        This is the method that actually counts the words
        :return: <int>
        """
        self.run_text_through_html_filter
        self.run_text_through_a_symbol_filter
        return len(self.text.split())

    @property
    def run_text_through_html_filter(self):
        """
        We only need text from html
        return: None
        """
        soup = BeautifulSoup(self.text, "html.parser")
        self.text = soup.text

    @property
    def run_text_through_a_symbol_filter(self):
        """
        Symbols should not be counted
        :return <None>
        """
        self.text = re.sub("[^A-Za-z0-9]", " ", self.text)


if __name__ == "__main__":
    TEXT = ["I am studying data science"]
    INST = WordCounter(TEXT)
    print(INST.count_words())
    #print(BeautifulSoup(TEXT, "html.parser").text)

