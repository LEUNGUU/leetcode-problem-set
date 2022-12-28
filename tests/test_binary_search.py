from binary_search import Solution

testcase = [{"testcase": [-1, 0, 3, 5, 9, 12], "target": 9, "result": 4}]


def test_binary_search():
    for tc in testcase:
        nums = tc["testcase"]
        target = tc["target"]
        ans = Solution().search(nums, target)
        assert ans == tc["result"]
