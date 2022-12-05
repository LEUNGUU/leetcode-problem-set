# Best Time to Buy and Sell Stock IV
#
# [Hard] [AC:28.1% 139.6K of 496.7K] [filetype:python3]
#
# Say you have an array for which the i-th element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most k transactions.
#
# Note:
#
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#
# Example 1:
#
# Input: [2,4,1], k = 2
#
# Output: 2
#
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
#
# Example 2:
#
# Input: [3,2,6,5,0,3], k = 2
#
# Output: 7
#
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
#
#              Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
#
# [End of Description]:
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k > n // 2:
            return self.maxProfit_k_inf(prices)
        # initialize dp
        dp = []
        for _ in range(n):
            inner1 = []
            for _ in range(k + 1):
                inner2 = []
                for i in range(2):
                    inner2.append(i)
                inner1.append(inner2)
            dp.append(inner1)

        for i in range(n):
            for j in range(k, 0, -1):
                # base case
                if i - 1 == -1:
                    dp[0][j][0] = 0
                    dp[0][j][1] = -prices[i]
                    # we need to continue here, since this time of loop is done
                    continue
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        return dp[n - 1][k][0]

    def maxProfit_k_inf(self, prices: List[int]) -> int:
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = -float("inf")
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i])
        return dp_i_0
