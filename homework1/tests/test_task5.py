"""
Task 5: Lists and Dictionaries test
By Jeffrey Kotz - 2/7/2026

Test functionality of list and dictionary function demonstrations
"""

import pytest

from task5 import print_favorite_n_books, create_student_dictionary

@pytest.fixture
def favorite_books() -> list[(str, str)]:
    """fixture providing a set of test books for verification

    Returns:
        list[(str, str)]: prepared list of books
    """

    books = []

    for i in range(1,21):
        books.append((f"book{i}", f"author{i}"))


    # list of from 1 to n
    return books


def test_print_favorite_n_books(capsys, favorite_books: list[(str, str)]):
    """test correctness of slicing of list data structure

    Args:
        capsys: capsys provides output capture for verification
        favorite_books (list[(str, str)): list of 20 favorite books provided by the fixture
    """

    # print the first 5 favorite books
    print_favorite_n_books(5, favorite_books)

    output = capsys.readouterr()

    # The format should follow "Title: book{n}. Author: author{n}" for every book printed 1 to n
    # in this case 5 books will be printed in this format
    assert output.out == """Title: book1, Author: author1
Title: book2, Author: author2
Title: book3, Author: author3
Title: book4, Author: author4
Title: book5, Author: author5
"""

def test_create_student_dictionary():
    """test that a dictonary is properly created by matching all keys to their value
    in this case matching students by name to their ID
    """

    is_valid = True

    size = 20

    # creating a list of 20 students following of key: StudentName{n}, value: {n} from n of 1 to 20
    database = create_student_dictionary(size)

    for i in range(1, size + 1):
        # if any of the students created don't have the right id
        # the demonstration is not valid
        if (database[f"StudentName{i}"] != i):
            is_valid = False
    
    assert is_valid