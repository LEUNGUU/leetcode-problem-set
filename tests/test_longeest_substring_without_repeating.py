from longest_substring_without_repeating import Solution

testcase = [{"testcase": "abcabcbb", "result": 3}]


def test_longest_substring_without_repeating():
    for tc in testcase:
        s = tc["testcase"]
        ans = Solution().lengthOfLongestSubstring(s)
        assert ans == tc["result"]
