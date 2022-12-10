from product_except_self import Solution

testcases = [{"testcase": [1, 2, 3, 4], "result": [24, 12, 8, 6]}]


def test_product_except_self():
    for tc in testcases:
        nums = tc["testcase"]
        ans = Solution().productExceptSelf(nums)
        assert ans == tc["result"]
