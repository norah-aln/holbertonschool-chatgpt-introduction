#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a number using recursion.

    Parameters:
        n (int): A non-negative integer representing the number 
                 we want to compute its factorial.

    Returns:
        int: The factorial result of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)

