from daily_temperature import Solution

testcase = [
    {"testcase": [73, 74, 75, 71, 69, 72, 76, 73], "result": [1, 1, 4, 2, 1, 1, 0, 0]}
]


def test_daily_temperature():
    for tc in testcase:
        temperatures = tc["testcase"]
        ans = Solution().dailyTemperatures(temperatures)
        assert ans == tc["result"]
