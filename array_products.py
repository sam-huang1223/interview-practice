"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at
index i of the new array is the product of all the numbers in the original
array except the one at i. Solve it without using division and in O(n) time.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""


def naive(arr):
    pass


def better_naive(arr):
    pass


if __name__ == "__main__":
    inp1 = [1, 2, 3, 4, 5]
    inp2 = [3, 2, 1]

    assert naive(inp1) == [120, 60, 40, 30, 24], "naive attempt fails on inp1"
    assert naive(inp2) == [2, 3, 6], "naive attempt fails on inp2"
    assert better_naive(inp1) == [120, 60, 40, 30, 24], "better_naive attempt fails on inp1"
    assert better_naive(inp2) == [2, 3, 6], "better_naive attempt fails on inp2"
