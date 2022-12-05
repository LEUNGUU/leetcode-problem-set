from valid_anagram import Solution

testcases = [
    {"testcase": ["anagram", "nagaram"], "result": True},
    {"testcase": ["aacc", "ccac"], "result": False},
]


def test_valid_anagram():
    for tc in testcases:
        s = tc["testcase"][0]
        t = tc["testcase"][1]
        ans = Solution().isAnagram(s, t)
        assert ans is tc["result"]
