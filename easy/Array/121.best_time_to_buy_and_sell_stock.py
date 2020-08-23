# Best Time to Buy and Sell Stock
#
# [Easy] [AC:50.2% 859.9K of 1.7M] [filetype:python3]
#
# Say you have an array for which the ith element is the price of
# a given stock on day i.
#
# If you were only permitted to complete at most one transaction
# (i.e., buy one and sell one share of the stock), design an algorithm
# to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
#
# Output: 5
#
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6),
# profit = 6-1 = 5.
#
#              Not 7-1 = 6, as selling price needs to be larger than
#              buying price.
#
# Example 2:
#
# Input: [7,6,4,3,1]
#
# Output: 0
#
# Explanation: In this case, no transaction is done, i.e. max profit
# = 0.
#
# [End of Description]:

# brute force(Not Accepted, Timeout)
# In formal terms, we need to find max(prices[j]−prices[i]), for every i and j such that j > i.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]
        return max_profit


# one pass(We need to find the largest peak following the smallest valley)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        min_price = float("inf")
        for i in range(n):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - min_price)
        return max_profit
