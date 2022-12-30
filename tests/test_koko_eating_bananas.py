from koko_eating_bananas import Solution


testcase = [{"testcase": [3, 6, 7, 11], "h": 8, "result": 4}]


def test_koko_eating_bananas():
    for tc in testcase:
        piles = tc["testcase"]
        h = tc["h"]
        ans = Solution().minEatingSpeed(piles, h)
        assert ans == tc["result"]
