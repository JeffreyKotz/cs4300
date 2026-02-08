"""
Task 5: Lists and Dictionaries
By Jeffrey Kotz - 2/7/2026

Demonstrate use of Lists and Dictionaries using books as an example
"""

def print_favorite_n_books(n: int, books: list[(str, str)]):
    """print favorite n books in list of books

    Args:
        n (int): number of books to print from start
        books (list[(str, str))]): list of books where each element is a tuple of 2 strings representing Title and Author
    """

    for book in books[0:n]:
        print(f"Title: {book[0]}, Author: {book[1]}")

def create_student_dictionary(n) -> dict[str, int]:
    """Creates a dictionary of students representing a basic student database

    Args:
        n (int): number of students included in database

    Returns:
        dict[str, int]: dictionary of student name to id
    """

    database = {}

    for i in range(n):
        # add StudentName{i+1} with id of i + 1 for the student
        database[f"StudentName{i+1}"] = i + 1
    
    return database

# Only print output when this specific file is ran
if __name__ == "__main__":
    print("Demonstration: Functions & Duck Typing - By Jeffrey Kotz")

    # A list of 6 books, each element is a tuple containing (Title, Author)
    favorite_books = [ ("1984", "George Orwell"),
        ("The Giving Tree", "Shel Silverstein"),
        ("The Great Gatsby", "Scott Fitzgerald"),
        ("Harry Potter and The Socerer's Stone", "J.K. Rowling"),
        ("Great Expectations", "Charles Dickens"),
        ("DOUG: A DougDoug Story", "Douglas Scott Wreden"),
        ]

    print("\nDemonstration of list data structure by printing titles and authors of 3 books using slicing:")
    print_favorite_n_books(3, favorite_books)

    print ("\nDemonstration of Dictionary representing a basic student database")
    student_database = create_student_dictionary(7)

    print(f"Creating a dictionary of 7 fake students: {student_database}")
    print(f"id of StudentName5 using name as a key = {student_database["StudentName5"]}")
    print(f"id of StudentName1 using name as a key = {student_database["StudentName1"]}")
