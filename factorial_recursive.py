#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number recursively.
    
    This function computes the factorial of n (n!) which is the product
    of all positive integers less than or equal to n.
    
    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.
    
    Returns:
    int: The factorial of n. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
