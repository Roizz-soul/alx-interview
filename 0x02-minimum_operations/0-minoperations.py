#!/usr/bin/python3
""" Module for minimum operations copy and paste """


def minOperations(n):
    """ Returns the number of min operations
        for the copy and paste commands"""
    if n < 2:
        return 0

    factors = []
    divisor = 2
    b = n

    while b > 1:
        while b % divisor == 0:
            factors.append(divisor)
            b //= divisor
        divisor += 1

    return max(factors) + (n // max(factors))
