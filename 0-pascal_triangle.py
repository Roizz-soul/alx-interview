#!/usr/bin/python3
"""
Pascal triangle algorithm
"""


def pascal_triangle(n):
    if (n <= 0):
        return []
    else:
        list1 = []
        for i in range(n):
            if i == 0:
                list1.append([1])
            elif i == 1:
                list1.append([1, 1])
            else:
                c = 0
                list2 = []
                list2.append(1)
                for t in range(i - 1):
                    list2.append(list1[i-1][c] + list1[i-1][c + 1])
                    c += 1
                list2.append(1)
                list1.append(list2)
        return list1
