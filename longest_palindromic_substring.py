"""
This problem was asked by Amazon.

Given a string, find the longest palindromic contiguous substring.
If there are more than one with the maximum length, return any one.
"""


def naive(inp):
    """
    no obvious naive solution -> DP required
    """


if __name__ == "__main__":
    inp1 = 'aabcdcb'
    inp2 = 'bananas'

    assert naive(inp1) == 'bcdcb', "naive fails on inp1"
    assert naive(inp2) == 'anana', "naive fails on inp2"
