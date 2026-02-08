"""
Task 2: Variables and Data Types
By Jeffrey Kotz - 2/7/2026

This script demonstrates various data types such as integer, float, strings, and boolean.
"""

### Integer operations ###
def integer_add(x: int, y: int) -> int:
    """demonstrate addition of integers

    Args:
        x (int): First integer to add.
        y (int): Second integer to add.

    Returns:
        int: result of adding x and y.
    """

    return x + y

def integer_div(x: int, y: int) -> int:
    """demonstrate 

    Args:
        x (int): dividende
        y (int): divisor

    Returns:
        int: quotient result of division of x by y
    """

    # Cast result of division to int to demonstrate removal of decimal place
    return int(x / y)

### Float Operations
def float_mult(x: float, y: float) -> float:
    """Demonstrate float multiplication

    Args:
        x (float): First value to multiply
        y (float): _description_

    Returns:
        float: _description_
    """

    return x * y

def float_div(x: float, y: float) -> float:
    """Demonstrate float division

    Args:
        x (float): dividend
        y (float): divisor

    Returns:
        float: quotient the result of dividing floats x by y
    """
    return x / y

### String Operations
def string_concat(str1: str, str2: str) -> str:
    """demonstrate concatenation of two strings

    Args:
        str1 (str): first string to concatenate
        str2 (str): second string to concatenate

    Returns:
        str: result of concatenating strings
    """
    return str1 + str2

def string_print(string: str):
    """print the argument given

    Args:
        string (str): string to print
    """
    print(string)

### Boolean Operations
def bool_select(x: int, y: int, first_value: bool) -> int:
    """Demosntrate: Conditional selectlection of x or y depending on first_value boolean flag

    Args:
        x (int): first value given
        y (int): second value given
        firstValue (bool): selecting flag for first value, if true return x, else return y

    Returns:
        int: x or y depending on state of first_value flag
    """

    # pick x or y depending on value of first_value
    if first_value:
        result = x
    else:
        result = y

    return result

def bool_equals(x: int, y: int) -> bool:
    """Demonstrate use of equals comparison to show resulting boolean

    Args:
        x (int): first value compared
        y (int): second value compared

    Returns:
        bool: result of equality comparison of x and y
    """

    return x == y

# Only executes if this specific file is ran
if __name__ == "__main__":
    print("Demonstration: Data Type - By Jeffrey Kotz")

    # Demonstrate Integer Data type
    print("\nDemonstration of data type: int")
    # using format string to for interporlation of result of demo function calls
    print(f"Addition: 1 + 2 = {integer_add(1,2)}") # Basic integer operation
    print(f"Division (decimal not preserved): 5 / 2 = {integer_div(5,2)}")

    # Demonstrate Float Data Type
    print("\nDemonstration of data type: float")
    print(f"Multiplication: 0.5 * 6.0 = {float_mult(0.5, 6.0)}")
    print(f"Division (decimal preserved): 5.0 / 2.0 = {float_div(5.0, 2.0)}")

    # Demonstrate String Data Type
    print("\nDemonstration of data type: str")
    print(f"Concatenation: \"Hello, \" and \"World!\" => {string_concat("Hello, ", "World!")}")
    print("Printing of string: \"This is a String!\"")
    string_print("This is a String!")

    # Demonstration of Boolean Data Type
    print("\nDemonstration of data type: bool")
    print(f"Conditional operations: first_value is true, select -3 or 4: {bool_select(-3, 4, True)}")
    print(f"Conditional operations: first_value is false, select -3 or 4: {bool_select(-3, 4, False)}")
    print(f"Conditional comparison: 2 == 3: {bool_equals(2, 3)}")
    # added new line for multiple files being run at once
    print(f"Conditional comparison: 5 == 5: {bool_equals(5, 5)}\n")

