from three_sum import Solution

testcase = [{"testcase": [-1, 0, 1, 2, -1, -4], "result": [[-1, -1, 2], [-1, 0, 1]]}]


def test_three_sum():
    for tc in testcase:
        nums = tc["testcase"]
        ans = Solution().threeSum(nums)
        assert ans == tc["result"]
