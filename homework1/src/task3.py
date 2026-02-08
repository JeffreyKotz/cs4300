"""
Task 3: Control Structures
By Jeffrey Kotz - 2/7/2026

Demonstrate use of control structures
"""

import math # import math for factorial calculations

def sign_of(x) -> str:
    """Check if a given value is positive, negative, or zero using an if statement

    Args:
        x (number): value to check sign of

    Returns:
        str: return string "positive", "negative", or "zero" depending on value of x
    """

    result = "unexpected result"

    # Use if statements to check whether x is positive, negative, or zero
    if (x == 0):
        result = "zero"
    if (x > 0):
        result = "positive"
    if (x < 0):
        result = "negative"

    return result

def print_first_n_primes(n: int):
    """Print the first 10 prime numbers using a for loop

    Args:
        n (int): integer value of the number of in order primes to print
    """

    num_primes = 0
    primes = []

    # i is used to track iteration so the same value infinite loop does not occur
    i = 1
    # find the first n primes
    while (num_primes < n):
        # using prime formula from https://en.wikipedia.org/wiki/Formula_for_primes
        # f(n) = floor((n! mod (n + 1))/n) * (n-1) + 2
        prime = math.factorial(i) % (i + 1)
        prime /= i
        prime = math.floor(prime)
        prime *= (i-1)
        prime += 2

        i += 1

        # If the prime is not in the list of primes add it
        if (not prime in primes):
            primes.append(prime)
            num_primes += 1

    # Using a for loop, print the first n prime numbers
    for i in range(n):
        print(primes[i])

def sum_one_to_n(n: int) -> int:
    """sum all values from one to the value of n

    Args:
        n (int): value to stop summation

    Returns:
        int: summation of 1 to n
    """

    total = 0 # variable tracking summed total to return at end of function

    # starting from 1, add all values from 1 to n to the summation
    i = 1
    while (i <= n):
        total += i
        i += 1

    return total

# Only print output if this specific file is ran
if __name__ == "__main__":
    print("Demonstration: Control Structures - By Jeffrey Kotz")

    # format string to interpolate result of function operations
    print("\nDemonstration of if control structure by finding the sign of values:")
    print(f"-3 is {sign_of(-3)}")
    print(f"3 is {sign_of(3)}")
    print(f"0 is {sign_of(0)}")

    print("\nDemonstration of for loop control structures by printing the first 10 primes:")
    print_first_n_primes(10)

    print("\nDemonstration of while loop control structures by summing all values from 1 to 100:")
    # added new line for multiple files being run at once
    print(f"Summation from 1 to 100 = {sum_one_to_n(100)}\n") 