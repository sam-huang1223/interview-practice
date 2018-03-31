"""
This problem was asked by Airbnb

Given a list of integers, write a function that returns the largest
sum of non-adjacent numbers. Input can contain 0 and negative numbers.
"""

import numpy as np


def naive(arr):
    """
    For each element in the input array, iterate through all non-adjacent elements to its left and right,
    checking its sum and the returning the highest sum found
    O(n^2) time, O(n) space
    """
    max_sum = 0
    for idx in range(len(arr)):
        if idx-1 > 0:
            for i in range(0, idx-1):
                if arr[idx] + arr[i] > max_sum:
                    max_sum = arr[idx] + arr[i]
        elif idx+1 < len(arr)-1:
            for i in range(idx+2, len(arr)):
                if arr[idx] + arr[i] > max_sum:
                    max_sum = arr[idx] + arr[i]
    return max_sum


def smart(arr, idx):
    """
    DP solution (determines solution for max sum at idx using max sum at idx-1 and max sum at idx-2)
    O(n!) time, O(n!) space
    """
    if idx == 0:
        return arr[0] if arr[0] > 0 else 0
    if idx == 1:
        if arr[0] <= 0:
            return 0
        elif arr[1] <= 0:
            return 0
        else:
            return max(arr[0], arr[1])
    return max(smart(arr, idx-1), smart(arr, idx-2) + arr[idx])


def smarter(arr, idx, mem):
    """
    DP solution - memoized
    O(n) time, O(n) space
    """
    if idx == 0:
        return arr[0] if arr[0] > 0 else 0
    if idx == 1:
        if arr[0] <= 0:
            return 0
        elif arr[1] <= 0:
            return 0
        else:
            return max(arr[0], arr[1])
    if mem[idx]:
        return mem[idx]
    mem[idx] = max(smart(arr, idx-1), smart(arr, idx-2) + arr[idx])
    return mem[idx]


def smartest(arr):
    """
    Improved bottom-up DP solution (only keeps track of max sum of 0:idx-1 and max sum of 0:idx-2 instead of all sums)
    O(n) time, O(1) space
    """
    prev = arr[1] if arr[1] > 0 else 0
    prevprev = arr[0] if arr[0] > 0 else 0

    for i in range(2, len(arr)):
        temp = prev
        prev = prevprev + arr[i]
        prevprev = max(prevprev, temp)

    return max(prev, prevprev)


"""
if __name__ == "__main__":
    inp1 = [2, 4, 6, 8]
    inp2 = [5, 1, 1, 0, 5]  # contains duplicates and 0
    inp3 = [-4, 5, 9, -3, 2, 1, 2]  # contains duplicates and negatives
    inp4 = [4, 6, -3, -3, 0, 4, 10]  # contains duplicates and negatives and 0

    assert naive(inp1) == 12, "naive attempt fails on inp1"
    #assert naive(inp2) == 11, "naive attempt fails on inp2"
    #assert naive(inp3) == 13, "naive attempt fails on inp3"
        # naive will fail on arrays of size >4 as it only identifies 2 elements

    assert smart(inp1, len(inp1)-1) == 12, "smart attempt fails on inp1"
    assert smart(inp2, len(inp2)-1) == 11, "smart attempt fails on inp2"
    assert smart(inp3, len(inp3)-1) == 13, "smart attempt fails on inp3"
    assert smart(inp4, len(inp4)-1) == 16, "smart attempt fails on inp4"

    assert smarter(inp1, len(inp1)-1, mem=np.zeros(len(inp1))) == 12, "smarter attempt fails on inp1"
    assert smarter(inp2, len(inp2)-1, mem=np.zeros(len(inp2))) == 11, "smarter attempt fails on inp2"
    assert smarter(inp3, len(inp3)-1, mem=np.zeros(len(inp3))) == 13, "smarter attempt fails on inp3"
    assert smarter(inp4, len(inp4)-1, mem=np.zeros(len(inp4))) == 16, "smarter attempt fails on inp4"

    assert smartest(inp1) == 12, "smartest attempt fails on inp1"
    assert smartest(inp2) == 11, "smartest attempt fails on inp2"
    assert smartest(inp3) == 13, "smartest attempt fails on inp3"
    assert smartest(inp4) == 16, "smartest attempt fails on inp4"
"""
