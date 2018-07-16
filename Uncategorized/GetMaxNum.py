"""
Given a sequence of float numbers, generate the maximum value that can be obtained by inserting 1 operator
(+, -, *, /) between the numbers in an expression (ignoring general arithmetic rules (i.e. BEDMAS) for simplicity)

For example, input [1, 12, -3] can be evaluated to equal 33 (1-12*-3) = (-11*-3) = 33
"""


def get_max_num_iterative(nums):
    """ Optimal Solution, implemented iteratively """
    min_branch = nums[0]
    max_branch = nums[0]

    for idx in range(1, len(nums)):
        min_branches = [min_branch + nums[idx],
                        min_branch - nums[idx],
                        min_branch * nums[idx],
                        min_branch / nums[idx]]

        max_branches = [max_branch + nums[idx],
                        max_branch - nums[idx],
                        max_branch * nums[idx],
                        max_branch / nums[idx]]

        min_branch = min(min(min_branches), min(max_branches))
        max_branch = max(max(max_branches), max(min_branches))

    return max(min_branch, max_branch)


def get_max_num_recursive(nums):
    """ Optimal Solution, implemented recursively (based on previous iterative solution """
    def loop(min_branch, max_branch, n):
        if n == len(nums):
            return max(min_branch, max_branch)

        min_branches = _helper(min_branch, nums[n])
        max_branches = _helper(max_branch, nums[n])

        min_branch = min(min(min_branches), min(max_branches))
        max_branch = max(max(max_branches), max(min_branches))

        return loop(min_branch, max_branch, n+1)

    def _helper(branch, num):
        return [branch + num,
                branch - num,
                branch * num,
                branch / num]

    return loop(nums[0], nums[0], 1)


if __name__ == '__main__':
    # define test cases
    test1 = [1.1, 6, 9, 2]
    ans1 = 127.8
    test2 = [1.1, 6, -9, 15]
    ans2 = 661.5
    test3 = [1, 12, -3]
    ans3 = 33

    # run tests
    assert get_max_num_iterative(test1) == ans1
    assert get_max_num_iterative(test2) == ans2
    assert get_max_num_iterative(test3) == ans3

    assert get_max_num_recursive(test1) == ans1
    assert get_max_num_recursive(test2) == ans2
    assert get_max_num_recursive(test3) == ans3

