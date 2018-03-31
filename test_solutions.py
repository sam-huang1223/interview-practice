import pytest
import numpy as np

import p1_first_missing_positive_integer as p1
@pytest.mark.parametrize(("test_input, expected"), [
        ([1, 4, 3, 2], 5),
        ([1, 3, 7, 1, 2], 4),  # contains duplicates
        ([3, 4, -1, 1], 2),  # contains negatives
    ])
class TestFirstMissingPositiveInteger:
    """ (1) 3*5=15 tests """

    def test_naive(self, test_input, expected):
        assert p1.naive(test_input) == expected

    def test_better_naive(self, test_input, expected):
        assert p1.better_naive(test_input) == expected

    def test_best_naive(self, test_input, expected):
        assert p1.best_naive(test_input) == expected

    def test_smart(self, test_input, expected):
        assert p1.smart(test_input) == expected

    ### smarter will fail on third input (and all inputs containing negative numbers)
    ### *skipping all tests here because I cannot figure out how to skip a specific testcase if class is decorated
    #def test_smarter(self, test_input, expected):
    #    assert first_missing_positive_integer.smarter(test_input) == expected

    def test_smartest(self, test_input, expected):
        assert p1.smartest(test_input) == expected


import p2_non_consecutive_sum as p2
@pytest.mark.parametrize(("test_input, expected"), [
    ([2, 4, 6, 8], 12),
    ([5, 1, 1, 0, 5], 11),  # contains duplicates and 0
    ([-4, 5, 9, -3, 2, 1, 2], 13),  # contains duplicates and negatives
    ([4, 6, -3, -3, 0, 4, 10], 16)  # contains duplicates and negatives and 0
    ])
class TestMaxNonConsecutiveSum:
    """ (2) 4*3=12 tests """

    ### naive will fail on all inputs past the first (and all input arrays of size >4 as it only identifies 2 elements)
    #def test_naive(self, test_input, expected):
    #    assert non_adjacent_sum.naive(test_input) == expected

    def test_smart(self, test_input, expected):
        assert p2.smart(test_input, len(test_input)-1) == expected

    def test_smarter(self, test_input, expected):
        assert p2.smarter(test_input, len(test_input)-1, mem=np.zeros(len(test_input))) == expected

    def test_smartest(self, test_input, expected):
        assert p2.smartest(test_input) == expected


import p3_array_products as p3
@pytest.mark.parametrize(("test_input, expected"), [
    ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
    ([3, 0, 1, 6], [0, 18, 0, 0]),  # contains 0
    ([3, 5, 2, -3, 3], [-90, -54, -135, 90, -90])  # contains negatives and duplicates
    ])
class TestArrayProducts:
    """ (3) 4*3=12 tests """

    def test_naive(self, test_input, expected):
        assert p3.naive(test_input) == expected

    def test_better_naive(self, test_input, expected):
        assert p3.better_naive(test_input) == expected

    def test_smart(self, test_input, expected):
        assert p3.smart(test_input) == expected

    def test_smartest(self, test_input, expected):
        assert p3.smartest(test_input) == expected


import message_decoding as p4
@pytest.mark.parametrize(("test_input, expected"), [
    ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
    ([3, 0, 1, 6], [0, 18, 0, 0]),  # contains 0
    ([3, 5, 2, -3, 3], [-90, -54, -135, 90, -90])  # contains negatives and duplicates
    ])
class TestMessageDecoding:
    """ (4) x*x=x tests """

    def test_naive(self, test_input, expected):
        pass


# TODO look into automatically generating tests?
