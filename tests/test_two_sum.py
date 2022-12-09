from two_sum import Solution


testcases = [
    {"testcase": [2, 7, 11, 15], "target": 9, "result": [0, 1]},
    {"testcase": [2, 4, 8], "target": 10, "result": [0, 2]},
]


def test_two_sum():
    for tc in testcases:
        target = tc["target"]
        nums = tc["testcase"]
        ans = Solution().twoSum(nums, target)
        assert ans == tc["result"]
