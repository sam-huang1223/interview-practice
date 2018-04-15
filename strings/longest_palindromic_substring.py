"""
This problem was asked by Amazon.

Given a string, find the longest palindromic contiguous substring.
If there are more than one with the maximum length, return any one.
"""


def naive(inp):
    """
    Find all contiguous substrings, check if they are palindromes, then return the longest found
    O(n^3) time, O(1) space
    """
    def check_palindrome(substr):
        for idx in range(int(len(substr)/2)):
            if substr[idx] != substr[-idx-1]:
                return False
        return True

    longest_palindrome = inp[0]

    for idx_start in range(len(inp)):
        for idx_end in range(idx_start + 1, len(inp) + 1):
            if check_palindrome(inp[idx_start:idx_end]):
                if idx_end - idx_start > len(longest_palindrome):
                    longest_palindrome = inp[idx_start:idx_end]

    return longest_palindrome


def smart(inp, mem):
    """
    DP solution
    O(n^2)
    """
    max_len = 1

    for i in range(len(inp)):
        mem[i][i] = True

    if inp[0] == inp[1]:
        mem[0][1] = True
    if inp[len(inp)-2] == inp[len(inp)-1]:
        mem[len(inp)-2][len(inp)-1] = True

    for i in range(1, len(inp)-1):
        if inp[i] == inp[i+1]:
            mem[i][i+1] = True
        if inp[i] == inp[i-1]:
            mem[i][i-1] = True


    for i in range(2, len(inp)-1):
        for j in range(3, len(inp)):
            if mem[i+1, j-1] and inp[i]==inp[j]:
                mem[i, j] = True
    print(mem)










if __name__ == "__main__":
    inp1 = 'aabcdcb'
    inp2 = 'bananas'
    inp3 = 'HYTBCABADEFGHABCDEDCBAGHTFYW1234567887654321ZWETYGDE'

    assert naive(inp1) == 'bcdcb', "naive fails on inp1"
    assert naive(inp2) == 'anana', "naive fails on inp2"
    assert naive(inp3) == '1234567887654321', "naive fails on inp3"

    from numpy import zeros
    print(smart(inp1, mem=zeros((len(inp1), len(inp1)), dtype=bool)))
