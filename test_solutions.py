import pytest

import first_missing_positive_integer
@pytest.mark.parametrize(("test_input, expected"), [
        ([1, 4, 3, 2], 5),
        ([1, 3, 7, 1, 2], 4),  # contains duplicates
        ([3, 4, -1, 1], 2),  # contains negatives
    ])
class TestFirstMissingPositiveInteger:
    def test_naive(self, test_input, expected):
        assert first_missing_positive_integer.naive(test_input) == expected

    def test_better_naive(self, test_input, expected):
        assert first_missing_positive_integer.better_naive(test_input) == expected

    def test_best_naive(self, test_input, expected):
        assert first_missing_positive_integer.best_naive(test_input) == expected

    def test_smart(self, test_input, expected):
        assert first_missing_positive_integer.smart(test_input) == expected

    ### smarter will fail on third input (and all inputs containing negative numbers)
    ### *skipping all tests here because I cannot figure out how to skip a specific testcase if class is decorated
    #def test_smarter(self, test_input, expected):
    #    assert first_missing_positive_integer.smarter(test_input) == expected

    def test_smartest(self, test_input, expected):
        assert first_missing_positive_integer.smartest(test_input) == expected


import array_products

class TestArrayProducts:
    pass

# TODO look into automatically generating tests?