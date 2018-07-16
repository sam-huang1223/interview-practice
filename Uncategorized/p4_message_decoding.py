"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
count the number of ways it can be decoded.
"""


def naive(msg, mapping):
    """
    Recursive solution -
    O(k*n!) time, O(n) space due to call stack
    """
    if not msg or '0' in msg:
        return 1

    total = 0
    for i in mapping.values():
        if msg[:len(i)] == i:  # if message starts with i
            total += naive(msg[len(i):], mapping)  # O(n!) recursive calls

    return total


from functools import lru_cache
@lru_cache(None)  # lru_cache implements memoization
def smart(msg, mapping):
    """
    no easy brute force solution - use dynamic programming
    O(k*n) time, O(n) space due to memoization
    """
    if not msg or '0' in msg:
        return 1

    total = 0
    for i in mapping:
        if msg[:len(i)] == i:  # if message starts with i
            total += smart(msg[len(i):], mapping)  # O(n) time once memoized

    return total


if __name__ == "__main__":
    from string import ascii_lowercase
    mapping = {key: str(idx+1) for idx, key in enumerate(ascii_lowercase)}

    inp1 = '111'
    inp2 = '9217'
    inp3 = ''  # is null
    inp4 = '1215'
    inp5 = '3014'  # contains 0
    inp6 = '111111111111111111111111111111'  # long input

    assert naive(inp1, mapping) == 3, "naive attempt fails on inp1"
    assert naive(inp2, mapping) == 3, "naive attempt fails on inp2"
    assert naive(inp3, mapping) == 1, "naive attempt fails on inp3"
    assert naive(inp4, mapping) == 5, "naive attempt fails on inp4"
    assert naive(inp5, mapping) == 1, "naive attempt fails on inp5"

    from time import clock
    startTime = clock()
    naive(inp6, mapping)
    print("naive runtime on long input is:", clock() - startTime)  # ~25s on surface pro 4

    mapping = tuple(str(idx + 1) for idx in range(len(ascii_lowercase)))

    assert smart(inp1, mapping) == 3, "smart attempt fails on inp1"
    assert smart(inp2, mapping) == 3, "smart attempt fails on inp2"
    assert smart(inp3, mapping) == 1, "smart attempt fails on inp3"
    assert smart(inp4, mapping) == 5, "smart attempt fails on inp4"
    assert smart(inp5, mapping) == 1, "smart attempt fails on inp5"

    startTime = clock()
    smart(inp6, mapping)
    print("smart runtime on long input is:", clock() - startTime)  # 0s on surface pro 4