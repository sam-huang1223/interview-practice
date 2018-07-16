"""
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
"""


def naive(inp):
    """
    O(n^2) time, O(1) space
    """
    max_count = 0
    for idx, lecture in enumerate(inp):
        count = 1
        for other_lecture in [l for l in inp if l != lecture]:
            if other_lecture[0] <= lecture[0] < other_lecture[1]:
                count += 1
        if count > max_count:
            max_count = count

    return max_count


def smart(inp):
    """
    O(nlogn + n) time, O(1) space
    """
    starts = sorted([i[0] for i in inp])
    ends = sorted([i[1] for i in inp])

    classes_req = 0
    ends_tracker = 0

    for i in starts:
        if i < ends[ends_tracker]:
            classes_req += 1
        else:
            ends_tracker += 1
    return classes_req


if __name__ == '__main__':
    inp1 = [(30, 75), (0, 50), (60, 150)]
    inp2 = [(55, 105), (15, 55), (140, 200), (110, 120)]
    inp3 = [(10, 50), (60, 75), (5, 100), (70, 110), (50, 60), (95, 150), (35, 85)]

    assert naive(inp1) == 2, "naive solution fails on inp1"
    assert naive(inp2) == 1, "naive solution fails on inp2"
    assert naive(inp3) == 4, "naive solution fails on inp3"

    assert smart(inp1) == 2, "smart solution fails on inp1"
    assert smart(inp2) == 1, "smart solution fails on inp2"
    assert smart(inp3) == 4,  "smart solution fails on inp3"
