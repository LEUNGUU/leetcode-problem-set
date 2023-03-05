from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if (rest := a - c) >= 0:
                    dp[a] = min(dp[a], 1 + dp[rest])
        return dp[amount] if dp[amount] != amount + 1 else -1
