from contain_most_water import Solution

testcase = [{"testcase": [1, 8, 6, 2, 5, 4, 8, 3, 7], "result": 49}]


def test_contain_most_water():
    for tc in testcase:
        height = tc["testcase"]
        ans = Solution().maxArea(height)
        assert ans == tc["result"]
