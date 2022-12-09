from top_k_frequent import Solution

testcase = [{"testcase": [1, 1, 2, 2, 3, 1], "k": 2, "result": [1, 2]}]


def test_top_k_frequest():
    for tc in testcase:
        nums = tc["testcase"]
        k = tc["k"]
        ans = Solution().topKFrequent(nums, k)
        assert ans == tc["result"]
