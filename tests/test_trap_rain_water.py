from trap_rain_water import Solution

testcase = [{"testcase": [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], "result": 6}]


def test_trap_rain_water():
    for tc in testcase:
        height = tc["testcase"]
        ans = Solution().trap(height)
        assert ans == tc["result"]
