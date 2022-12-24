from longest_repeating_char_replacement import Solution

testcase = [{"testcase": "AABABBA", "k": 1, "result": 4}]


def test_longest_repeating_char_replacement():
    for tc in testcase:
        s = tc["testcase"]
        k = tc["k"]
        ans = Solution().characterReplacement(s, k)
        assert ans == tc["result"]
