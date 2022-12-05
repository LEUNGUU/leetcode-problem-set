# Coin Change 2
#
# [Medium] [AC:50.6% 148.7K of 294.1K] [filetype:python3]
#
# You are given coins of different denominations and a total amount of money. Write a function to compute the number of
# combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
#
# Example 1:
#
# Input: amount = 5, coins = [1, 2, 5]
#
# Output: 4
#
# Explanation: there are four ways to make up the amount:
#
# 5=5
#
# 5=2+2+1
#
# 5=2+1+1+1
#
# 5=1+1+1+1+1
#
# Example 2:
#
# Input: amount = 3, coins = [2]
#
# Output: 0
#
# Explanation: the amount of 3 cannot be made up just with coins of 2.
#
# Example 3:
#
# Input: amount = 10, coins = [10]
#
# Output: 1
#
# Note:
#
# You can assume that
#
# 0 <= amount <= 5000
#
# 1 <= coin <= 5000
#
# the number of coins is less than 500
#
# the answer is guaranteed to fit into signed 32-bit integer
#
# [End of Description]:
# bag
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        sz = len(coins)
        dp = []
        for _ in range(sz + 1):
            inner = []
            for _ in range(amount + 1):
                inner.append(0)
            dp.append(inner)
        # base case
        for i in range(sz + 1):
            dp[i][0] = 1

        for i in range(1, sz + 1):
            for j in range(1, amount + 1):
                if j - coins[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[sz][amount]


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        sz = len(coins)
        dp = [0] * (amount + 1)
        # base case
        dp[0] = 1
        for i in range(sz):
            for j in range(1, amount + 1):
                if j - coins[i] >= 0:
                    dp[j] = dp[j] + dp[j - coins[i]]
        return dp[amount]
