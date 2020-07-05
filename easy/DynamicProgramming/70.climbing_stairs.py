# Climbing Stairs
#
# [Easy] [AC:46.9% 657.7K of 1.4M] [filetype:python3]
#
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
#
# Note: Given n will be a positive integer.
#
# Example 1:
#
# Input: 2
#
# Output: 2
#
# Explanation: There are two ways to climb to the top.
#
# 1. 1 step + 1 step
#
# 2. 2 steps
#
# Example 2:
#
# Input: 3
#
# Output: 3
#
# Explanation: There are three ways to climb to the top.
#
# 1. 1 step + 1 step + 1 step
#
# 2. 1 step + 2 steps
#
# 3. 2 steps + 1 step
#
# [End of Description]:
from typing import Any


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        if n == 1:
            return 1
        dp[1] = 1
        dp[2] = 2
        for item in range(3, len(dp)):
            dp[item] = dp[item - 1] + dp[item - 2]
        return dp[n]
