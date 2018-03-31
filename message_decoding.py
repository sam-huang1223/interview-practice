"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa, 'ka', and 'ak'.
"""
import string


def naive(msg, mapping):
    """

    O(n*n!) time, O(n!) space complexity (from call stack)
    """
    print(mapping)


def smart(msg, mapping):
    """
    no easy brute force solution - use dynamic programming
    decode in 2 by 2 chunks?
    """


if __name__ == "__main__":
    mapping = {key: idx+1 for idx, key in enumerate(string.ascii_lowercase)}

    inp1 = '111'
    inp2 = ''

    assert naive(inp1, mapping) == 3, "naive attempt fails on inp1"
    assert naive(inp2, mapping) == 0, "naive attempt fails on inp2"
    assert smart(inp1, mapping) == 3, "better_naive attempt fails on inp1"
    assert smart(inp2, mapping) == 0, "better_naive attempt fails on inp2"
