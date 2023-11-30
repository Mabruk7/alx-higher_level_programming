#!/usr/bin/python3
"""Module that finds a peak in a list of integers"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): a list of integers

    Your algorithm must have the lowest complexity.
    Note: there might be more than one peak in the list.

    The most simplistic approach to this problem is to simply examine each component separately to see whether it qualifies as a peak. 
    In the worst scenario, this solution will have O(n) time complexity and O(1) space complexity, which is excellent for the majority of 
    algorithmic problems. This is where it gets tricky: use O(log(n)) time complexity to solve it!

    Typically, Binary Search is applied to sorted arrays (which may also refer to Bitonic arrays or arrays sorted in other ways). However,
    this particular instance is a little bit unique because the array cannot be sorted.


    When using Binary Search, we always look at the middle value to determine if it meets the criteria to be considered a peak; if not, 
    we adjust the start or end pointer to obtain a new middle value.


    Returns:
        int: peak(s)
    """
    list_ = list_of_integers
    # if there is no list of integers return None
    if list_ == []:
        return None
    length = len(list_)

    start, end = 0, length - 1
    while start < end:
        mid = start + (end - start) // 2
        if list_[mid] > list_[mid - 1] and list_[mid] > list_[mid + 1]:
            return list_[mid]
        if list_[mid - 1] > list_[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return list_[start]
