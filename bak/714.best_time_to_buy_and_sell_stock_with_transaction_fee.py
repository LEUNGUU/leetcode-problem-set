# Best Time to Buy and Sell Stock with Transaction Fee
#
# [Medium] [AC:55.1% 75.2K of 136.6K] [filetype:python3]
#
# Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and
# a non-negative integer fee representing a transaction fee.
#
# You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.  You
# may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)
#
# Return the maximum profit you can make.
#
# Example 1:
#
# Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
#
# Output: 8
#
# Explanation: The maximum profit can be achieved by:
#
# Buying at prices[0] = 1Selling at prices[3] = 8Buying at prices[4] = 4Selling at prices[5] = 9The total profit is ((8
# - 1) - 2) + ((9 - 4) - 2) = 8.
#
# Note:
#
# 0 < prices.length <= 50000.
#
# 0 < prices[i] < 50000.
#
# 0 <= fee < 50000.
#
# [End of Description]:
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = -float("inf")
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i] - fee)
        return dp_i_0
