from search_in_rotated_sorted_array import Solution


testcase = [{"testcase": [4, 5, 6, 7, 0, 1, 2], "target": 0, "result": 4}]


def test_search_in_rotated_sorted_array():
    for tc in testcase:
        nums = tc["testcase"]
        target = tc["target"]
        ans = Solution().search(nums, target)
        assert ans == tc["result"]
