from minimum_window_substr import Solution

testcase = [{"testcase": ("ADOBECODEBANC", "ABC"), "result": "BANC"}]


def test_minimum_window_substr():
    for tc in testcase:
        s, t = tc["testcase"]
        ans = Solution().minWindow(s, t)
        assert ans == tc["result"]
