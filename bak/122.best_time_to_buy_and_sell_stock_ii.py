# Best Time to Buy and Sell Stock II
#
# [Easy] [AC:56.4% 602.9K of 1.1M] [filetype:python3]
#
# Say you have an array prices for which the ith element is the price of
# a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (i.e., buy one and sell one share of the stock
# multiple times).
#
# Note: You may not engage in multiple transactions at the same time (i.e., you
# must sell the stock before you buy again).
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
#
# Output: 7
#
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit
# = 5-1 = 4.
#
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6),
#              profit = 6-3 = 3.
#
# Example 2:
#
# Input: [1,2,3,4,5]
#
# Output: 4
#
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit
# = 5-1 = 4.
#
#              Note that you cannot buy on day 1, buy on day 2 and sell them
#              later, as you are
#
#              engaging multiple transactions at the same time. You must sell
#              before buying again.
#
# Example 3:
#
# Input: [7,6,4,3,1]
#
# Output: 0
#
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
#
# Constraints:
#
# 1 <= prices.length <= 3 * 10 ^ 4
#
# 0 <= prices[i] <= 10 ^ 4
#
# [End of Description]:


# add (peak - valley) one by one
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        i, maxProfit, peak, valley = 0, 0, prices[0], prices[0]
        while i < n - 1:
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            while i < n - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            maxProfit += peak - valley
        return maxProfit


## a mathmatics trick here
## peak1 - valley1 + peak2 - valley2
## p1-p0+p2-p1+p3-p2+...+p(n)-p(n-1) = p(n) - p0
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxProfit += prices[i] - prices[i - 1]
        return maxProfit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i_0 = 0
        dp_i_1 = -float("inf")
        n = len(prices)
        for i in range(n):
            # markdown the previous one
            # which is different from the second dp_i_0
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i])
        return dp_i_0
