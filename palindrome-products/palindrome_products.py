from collections import defaultdict

def is_palindrome(num):
    stringified = str(num)
    left, right = 0, len(stringified) - 1
    while left < right:
        if stringified[left] != stringified[right]:
            return False
        left, right = left + 1, right - 1
    return True

def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError('min must be <= max')

    mapping = defaultdict(list)

    for i in range(min_factor, max_factor):
        for j in range(i, max_factor + 1):
            if is_palindrome(i * j):
                mapping[i * j].append([i, j])

    if len(mapping) == 0:
        return None, []

    largest = sorted(mapping.keys())[-1]

    return largest, mapping[largest]



def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError('min must be <= max')

    mapping = defaultdict(list)

    for i in range(min_factor, max_factor):
        for j in range(i, max_factor + 1):
            if is_palindrome(i * j):
                mapping[i * j].append([i, j])

    if len(mapping) == 0:
        return None, []

    smallest = sorted(mapping.keys())[0]

    return smallest, mapping[smallest]
