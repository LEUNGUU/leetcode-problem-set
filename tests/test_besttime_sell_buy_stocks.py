from besttime_sell_buy_stocks import Solution


testcase = [{"testcase": [7, 1, 5, 3, 6, 4], "result": 5}]


def test_besttime_sell_buy_stock():
    for tc in testcase:
        prices = tc["testcase"]
        ans = Solution().maxProfit(prices)
        assert ans == tc["result"]
