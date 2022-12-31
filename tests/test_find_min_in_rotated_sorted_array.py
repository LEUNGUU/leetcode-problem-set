from find_min_in_rotated_sorted_array import Solution


testcase = [{"testcase": [3, 4, 5, 1, 2], "result": 1}]


def test_find_min_in_rotated_sorted_array():
    for tc in testcase:
        nums = tc["testcase"]
        ans = Solution().findMin(nums)
        assert ans == tc["result"]
