from two_sum_II import Solution


testcase = [{"testcase": [1, 2, 11, 12], "target": 3, "result": [1, 2]}]


def test_two_sum_II():
    for tc in testcase:
        numbers = tc["testcase"]
        target = tc["target"]
        ans = Solution().twoSum(numbers, target)
        assert ans == tc["result"]
