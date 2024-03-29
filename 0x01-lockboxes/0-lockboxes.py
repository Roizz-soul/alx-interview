#!/usr/bin/python3
"""
Algorithm to test if all boxes in a list can be unlocked
"""


def canUnlockAll(boxes):
    """
    function to check if key is in first box to
    unlock other boxes and eventually unlock all boxes
    """
    OurSet = [0]
    set1 = [0]
    los = []
    keys = [0]
    for i in range(len(boxes)):
        for j in keys:
            for k in boxes[j]:
                if k < len(boxes):
                    los.append(k)
        keys = list(set(los))
        set1.extend(los)
        los = []
        OurSet = list(set(set1))
        if len(set(OurSet)) == len(boxes):
            return True

    if len(set(OurSet)) == len(boxes):
        return True
    else:
        return False
