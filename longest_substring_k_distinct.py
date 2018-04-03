"""
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

from functools import lru_cache

@lru_cache(None)
def smart(s, k):
    """
    no obvious naive solution -> DP required
    """




if __name__ == "__main__":
    inp1_s = "abcba"
    inp1_k = 2

    assert smart(inp1_s, inp1_k) == 'bcb', "smart fails on inp1"