from valid_parentheses import Solution

testcase = [{"testcase": "()[]{}", "result": True}]


def test_valid_parentheses():
    for tc in testcase:
        s = tc["testcase"]
        ans = Solution().isValid(s)
        assert ans == tc["result"]
