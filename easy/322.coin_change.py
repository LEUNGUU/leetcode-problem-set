# Coin Change
#
# [Medium] [AC:35.9% 459K of 1.3M] [filetype:python3]
#
# You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
#
# Example 1:
#
# Input: coins = [1, 2, 5], amount = 11
#
# Output: 3
#
# Explanation: 11 = 5 + 5 + 1
#
# Example 2:
#
# Input: coins = [2], amount = 3
#
# Output: -1
#
# Note:
#
# You may assume that you have an infinite number of each kind of coin.
#
# [End of Description]:
# Memorization
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def dp(n):
            if n in memo:
                return memo[n]
            # base case
            if n == 0:
                return 0
            if n < 0:
                return -1
            # we set res to an infinite number in order to contain the solutions
            res = float("INF")
            for coin in coins:
                subproblem = dp(n - coin)
                # subproblem cannot have solutions
                if subproblem == -1:
                    continue
                res = min(res, 1 + subproblem)
            memo[n] = res if res != float("INF") else -1
            return memo[n]

        return dp(amount)


# make a dptable
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [amount + 1] * (amount + 1)
        memo[0] = 0
        for idx in range(amount + 1):
            for coin in coins:
                if (idx - coin) < 0:
                    continue
                memo[idx] = min(memo[idx], 1 + memo[idx - coin])
        return memo[amount] if memo[amount] != amount + 1 else -1
