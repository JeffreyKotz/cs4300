"""
Task 6: File Handling
By Jeffrey Kotz - 2/8/2026

Test functionality of file handling in Task6.py
"""

import pytest

from task6 import count_words_in_file

# Parameterized test, with a set of a file path and an expected word count
@pytest.mark.parametrize("file_path, expected_word_count", [("task6_read_me.txt", 104), ("word_count_test.txt", 10)])
def test_count_words_in_file(file_path, expected_word_count):
    """Test that the number of words in a file is properly counted.

    Args:
        file_path (str): the path of the file to count the words inside of
        expected_word_count (int): the expected word count for the file to match
    """

    # Assert whether the number of expected words is met by the demonstrating function
    assert count_words_in_file(file_path) == expected_word_count