"""
Given an array of integers (with both positive and negative values), find the
contiguous sequence with the largest sum and return the sum.
"""

def naive(arr):
    """

    O(n^3) time, O(1) space
    """
    max_sum = 0
    for s_i in range(len(arr)):
        for e_i in range(s_i, len(arr)):
            temp = sum(arr[s_i:e_i])
            if temp > max_sum:
                max_sum = temp
    return max_sum


def better_naive(arr):
    """

    O(n^2) time, O(1) space
    """
    max_sum = 0
    for s_i in range(len(arr)):
        running_sum = 0
        for e_i in range(s_i, len(arr)):
            running_sum += arr[e_i]
            if running_sum > max_sum:
                max_sum = running_sum
    return max_sum


def smart(arr):
    """

    O(n) time,
    """
    max_sum = 0
    running_sum = 0
    for num in arr:
        if num > 0:
            running_sum += num
        else:
            if running_sum > max_sum:
                max_sum = running_sum
            if abs(num) >= running_sum:
                running_sum = 0
            else:
                running_sum += num

    return max_sum


inp1 = [3,5,-6,4,-15,7]
inp2 = [2,-8,3,-2,4,-10]

assert naive(inp1) == 8, "naive fails on inp1"
assert better_naive(inp1) == 8, "better_naive fails on inp1"
assert smart(inp1) == 8, "smart fails on inp1"

assert naive(inp2) == 5, "naive fails on inp2"
assert better_naive(inp2) == 5, "better_naive fails on inp2"
assert smart(inp2) == 5, "smart fails on inp2"
