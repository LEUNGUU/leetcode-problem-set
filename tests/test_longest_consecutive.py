from longest_consecutive_sequence import Solution

testcase = [{"testcase": [100, 200, 1, 2, 3, 4], "result": 4}]


def test_longest_consecutive_sequence():
    for tc in testcase:
        nums = tc["testcase"]
        ans = Solution().longestConsecutive(nums)
        assert ans == tc["result"]
