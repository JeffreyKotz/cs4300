"""
Task 4: Functions and Duck Typing
By Jeffrey Kotz - 2/7/2026

Demonstrate use of duck typing in functions
"""

def calculate_discount(price, discount):
    """Using duck typing

    Args:
        price (number): base price in dollars accepting any type of number for base price
        discount (number): discount as percentage accepting any type of number for discount

    Returns:
        str: the price after the discount is applied formatted to 2 decimal places for currency conventions
    """

    # divide discount by 100 as it is give as a percentage
    discount /= 100

    resulting_price = price * (1 - discount)

    # Format result with a dollar sign, with value to 2 decimal places for currency
    # var_name:.nf allows for formatting to constrain to n decimal palces
    # https://www.w3schools.com/python/python_string_formatting.asp
    return f"${resulting_price:.2f}"

# Only print output if this specific file is ran
if __name__ == "__main__":
    print("Demonstration: Functions & Duck Typing - By Jeffrey Kotz")
    print(f"Discount with integers $100, & 40%: {calculate_discount(100, 40)}")
    print(f"Discount with integer & float $75, & 15.5%: {calculate_discount(75, 15.5)}")
    print(f"Discount with floats $33.33, and 15.5%: {calculate_discount(33.33, 15.5)}")
    print(f"Discount with float & integer $95.50, & 75%: {calculate_discount(95.50, 75)}\n")

