#!/usr/bin/python3
""" Module for minimum operations copy and paste """


def minOperations(n):
    """ Returns the number of min operations
        needed for the copy and paste ops"""
    if n < 2:
        return 0
    for i in range(2, n+1):
        if n % i == 0:
            return minOperations(int(n/i)) + i
