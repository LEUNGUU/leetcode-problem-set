from sliding_window_maximum import Solution

testcase = [
    {"testcase": [1, 3, -1, -3, 5, 3, 6, 7], "k": 3, "result": [3, 3, 5, 5, 6, 7]}
]


def test_sliding_window_maximum():
    for tc in testcase:
        nums = tc["testcase"]
        k = tc["k"]
        ans = Solution().maxSlidingWindow(nums, k)
        assert ans == tc["result"]
