"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at
index i of the new array is the product of all the numbers in the original
array except the one at i. Solve it without using division and in O(n) time.
"""


def naive(arr):
    """
    Obtain product of entire array, then divide by each element to obtain result
    O(n + n) time, O(1) space but involves division
    """
    from numpy import prod

    product = arr[0] if arr else 1
    for element in arr[1:]:
        product *= element

    return [product/element if element !=0 else prod([n for n in arr if n != 0]) for element in arr]


def better_naive(arr):
    """
    Multiply each element by the elements on its left and right
    O(n^2) time, O(1) space
    """
    products = []
    for idx in range(len(arr)):
        products.append(1)
        for left_idx in range(idx):
            products[idx] *= arr[left_idx]
        for right_idx in range(idx + 1, len(arr)):
            products[idx] *= arr[right_idx]
    return products


def smart(arr):
    """
    Remove repetitive calculations from better_naive solution - pre-calculate products from left side & right side
    O(n+n+n) time, O(n+n) space
    """
    left_prod = [1]
    right_prod = [1]

    for i in range(len(arr)-1):
        left_prod.append(arr[i] * left_prod[i])
        right_prod.append(arr[len(arr)-i-1] * right_prod[i])
    right_prod.reverse()

    return [left_prod[i] * right_prod[i] for i in range(len(arr))]


def smartest(arr):
    """
    Optimized smart solution to allow for constant space usage
    O(n+n) time, O(1) space
    """
    output = [1]*len(arr)

    l_prod_tracker = 1
    for i in range(len(arr)):
        output[i] *= l_prod_tracker
        l_prod_tracker *= arr[i]

    r_prod_tracker = 1
    for i in reversed(range(len(arr))):
        output[i] *= r_prod_tracker
        r_prod_tracker *= arr[i]

    return output

"""
if __name__ == "__main__":
    inp1 = [1, 2, 3, 4, 5]
    inp2 = [3, 0, 1, 6]  # contains 0
    inp3 = [3, 5, 2, -3, 3]  # contains negatives and duplicates

    assert naive(inp1) == [120, 60, 40, 30, 24], "naive attempt fails on inp1"
    assert naive(inp2) == [0, 18, 0, 0], "naive attempt fails on inp2"
    assert naive(inp3) == [-90, -54, -135, 90, -90], "naive attempt fails on inp3"
    assert better_naive(inp1) == [120, 60, 40, 30, 24], "better_naive attempt fails on inp1"
    assert better_naive(inp2) == [0, 18, 0, 0], "better_naive attempt fails on inp2"
    assert better_naive(inp3) == [-90, -54, -135, 90, -90], "better_naive attempt fails on inp3"
    assert smart(inp1) == [120, 60, 40, 30, 24], "smart attempt fails on inp1"
    assert smart(inp2) == [0, 18, 0, 0], "smart attempt fails on inp2"
    assert smart(inp3) == [-90, -54, -135, 90, -90], "smart attempt fails on inp3"
    assert smartest(inp1) == [120, 60, 40, 30, 24], "smartest attempt fails on inp1"
    assert smartest(inp2) == [0, 18, 0, 0], "smartest attempt fails on inp2"
    assert smartest(inp3) == [-90, -54, -135, 90, -90], "smartest attempt fails on inp3"
"""
