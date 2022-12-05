# Fibonacci Number
#
# [Easy] [AC:67.2% 237.4K of 353.4K] [filetype:python3]
#
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
#
# F(0) = 0,   F(1) = 1
#
# F(N) = F(N - 1) + F(N - 2), for N > 1.
#
# Given N, calculate F(N).
#
# Example 1:
#
# Input: 2
#
# Output: 1
#
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
#
# Example 2:
#
# Input: 3
#
# Output: 2
#
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
#
# Example 3:
#
# Input: 4
#
# Output: 3
#
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
#
# Note:
#
# 0 ≤ N ≤ 30.
#
# [End of Description]:
# brute force(low efficient)
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        return self.fib(N - 1) + self.fib(N - 2)


# we use hashtable to mark the values
from typing import List


class Solution:
    def fib(self, N: int) -> int:
        if N < 1:
            return 0
        memo = [0] * (N + 1)
        return self.dp(memo, N)

    def dp(self, memo: List[int], N: int) -> int:
        if N in [1, 2]:
            return 1
        # check if in the memo
        if memo[N] != 0:
            return memo[N]
        # calculate the result of N
        memo[N] = self.dp(memo, N - 1) + self.dp(memo, N - 2)
        return memo[N]


# dptable
class Solution:
    def fib(self, N: int) -> int:
        if N < 1:
            return 0
        if N in [1, 2]:
            return 1
        prev, curr = 1, 1
        for _ in range(3, N + 1):
            sum = prev + curr
            prev = curr
            curr = sum
        return sum
