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

# Recursion with Memorization
# It is like a tree, and i represents the level of the tree
from collections import defaultdict
from typing import Dict


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = defaultdict(int)
        return self.climb_stairs(0, n, memo)

    def climb_stairs(self, i: int, n: int, memo: Dict[int, int]) -> int:
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] > 0:
            return memo[i]
        memo[i] = self.climb_stairs(i + 1, n, memo) + self.climb_stairs(i + 2, n, memo)
        return memo[i]


# Dynamic Programming
# As we can see this problem can be broken into subproblems,
# and it contains the optimal substructure property i.e.
# its optimal solution can be constructed efficiently from optimal solutions of its subproblems,
# we can use dynamic programming to solve this problem.
# One can reach i step in one of the two ways:
#
# Taking a single step from (i−1)
#
# Taking a step of 2 from (i−2)
#
# Let dp[i] denotes the number of ways to reach on i step:
#
# dp[i]=dp[i-1]+dp[i-2]


class Solution:
    def climbStairs(self, n: int) -> int:
        # n+1 means we need to include number n
        dp = [0] * (n + 1)
        if n == 1:
            return 1
        # we begin from 1 means we at least take 1 step
        dp[1] = 1
        dp[2] = 2
        for item in range(3, len(dp)):
            # len(dp) already include number n
            dp[item] = dp[item - 1] + dp[item - 2]
        return dp[n]


# Fibonacci Number
# It is clearly that the number n is the nth fibonacci number
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first = 1
        second = 2
        for _ in range(3, n + 1):
            third = first + second
            first = second
            second = third
        return second
