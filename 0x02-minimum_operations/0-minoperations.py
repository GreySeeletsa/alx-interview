#!/usr/bin/python3
"""Module for task 0
"""


def minOperations(n):
    """In a text file, there is a single character H. Your text editor can
    execute only two operations in this file: Copy All and Paste characters
    in the file

    Args:
        n (int): Num of H characters

    Returns:
        int: Num of min operations needed to get n H characters
    or 0 if it is impossible to achieve n
    """
    if not isinstance(n, int):
        return 0
    ops_count = 0
    clipboard = 0
    done = 1
    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            ops_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            ops_count += 2
        elif clipboard > 0:
            done += clipboard
            ops_count += 1
    return ops_count
