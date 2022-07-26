"""
This is the module that tests the count_words script
We use test parameterization to test all methods
"""
# pylint: disable=W0106
# pylint: disable=E1121
import pytest
from count_words import WordCounter

MY_TESTS = [
    ("", 0),
    ("nlpoblano", 1),
    ("I study at Spiced", 4),
    ("<p> We learnt html last week </p>", 5),
    ("<div class='poblano'> <p> This section needs to be different </p> </div>", 6),
    ("%$# My name %$@ is !$@$ Johannes @$@%", 4),
    ("Testing for          multiple           white   spaces", 5)
]


def test_wrong_instance_type():
    """
    Test if the module fails when you
    introduce the wrong instance type
    :return <None>
    """
    text = ["This is a bootcamp college"]
    with pytest.raises(Exception) as error:
        WordCounter(text).count_words(text) == 5
    assert "input must be a string" in str(error.value)


@pytest.mark.parametrize("my_input, my_output", MY_TESTS)
def test_all_tests(my_input, my_output):
    """
    Using test parameterization to test all
    """
    assert WordCounter(my_input).count_words() == my_output
