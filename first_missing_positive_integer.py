"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


def naive(arr):
    """ Iterates through all positive integers and tries to find them in the array one at a time
    O(n^2)
    """
    for integer in range(1, len(arr)+1):
        for element in arr:
            if element == integer:
                break
        else:
            return integer
    return len(arr) + 1


def better_naive(arr):
    """ sort array in-place (heapsort allows for O(1) space complexity),
    then iterate through all positive integers to find first missing number
    O(nlogn + nlogn)
    """
    arr = sorted(arr)
    for integer in range(1, len(arr)+1):
        if integer not in arr:
            return integer
    return len(arr) + 1


def best_naive(arr):
    """ sort array in-place (heapsort allows for O(1) space complexity),
    then iterate through array to find missing number
    O(nlogn + n)
    """
    arr = sorted(arr)  # assume heapsort
    tracker = 1
    for idx in range(len(arr)):
        if arr[idx] > 0:  # allows for negatives in array
            if arr[idx] == arr[idx-1]:  # allows for duplicates in array
                continue
            elif arr[idx] == tracker:
                tracker += 1
            else:
                return tracker
    return len(arr) + 1


def smart(arr):
    """
    Build a hash table of all positive elements in the array, then
    look for the existence of all positive numbers starting from 1 to len(arr)
    O(n + n) BUT O(n) space
    """
    hash_table = {element: element for element in arr if element > 0}
    for pos in range(1, len(arr) + 1):
        try:
            temp = hash_table[pos]
        except KeyError:
            return pos
    return len(arr) + 1


def smarter(arr):
    """
    Loops through array looking for positive numbers below the array size
    (greater than array size implies that the missing integer must be less than it),
    then changes the sign of the array entry at the index of that number to negative,
    marking the presence of that positive number.
    Then loops through array looking for the first non-negative entry, returning
    that index as the missing positive integer
    *This approach only works if no negative numbers exist in the array
    O(n + n)
    """
    temp_arr = arr[:]
    for element in temp_arr:
        idx = abs(element)-1  # convert back to previously positive number and account for 0-indexing
        if idx < len(temp_arr):
            if temp_arr[idx] > 0:
                temp_arr[idx] = -1*temp_arr[idx]  # make it negative

    for idx in range(len(temp_arr)):
        if temp_arr[idx] > 0:
            return idx+1

    return len(temp_arr) + 1


def smartest(arr):
    """
    Allows for previous approach to work with negative numbers by separating the
    negative and positive numbers beforehand. Then apply previous procedure to the positive part of the array.
    O(n + n)
    """
    count = 0
    for idx in range(len(arr)):
        if arr[idx] <= 0:
            arr[idx], arr[count] = arr[count], arr[idx]
            count += 1

    pos_arr = arr[count:]

    for element in pos_arr:
        idx = abs(element)-1  # convert back to previously positive number and account for 0-indexing
        if idx < len(pos_arr):
            if pos_arr[idx] > 0:
                pos_arr[idx] = -1*pos_arr[idx]  # make it negative

    for idx in range(len(pos_arr)):
        if pos_arr[idx] > 0:
            return idx+1

    return len(arr) + 1
