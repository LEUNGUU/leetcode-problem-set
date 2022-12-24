from permutation_in_string import Solution

testcase = [{"testcase": ("ab", "eidbaooo"), "result": True}]


def test_permutation_in_string():
    for tc in testcase:
        s1 = tc["testcase"][0]
        s2 = tc["testcase"][1]
        ans = Solution().checkInclusion(s1, s2)
        assert ans == tc["result"]
