from evaluate_reverse_polish_notation import Solution

testcase = [{"testcase": ["2", "1", "+", "3", "*"], "result": 9}]


def test_evaluate_reverse_polish_notation():
    for tc in testcase:
        tokens = tc["testcase"]
        ans = Solution().evalRPN(tokens)
        assert ans == tc["result"]
