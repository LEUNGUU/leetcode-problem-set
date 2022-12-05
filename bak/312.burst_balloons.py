# Burst Balloons
#
# [Hard] [AC:52.2% 103.9K of 198.9K] [filetype:python3]
#
# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You
# are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins.
# Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.
#
# Find the maximum coins you can collect by bursting the balloons wisely.
#
# Note:
#
# You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
#
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
#
# Example:
#
# Input: [3,1,5,8]
#
# Output: 167
#
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#
#              coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
#
# [End of Description]:
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # we create array first
        sz = len(nums)
        # add two virtual balloons
        points = [None] * (sz + 2)
        points[0] = points[sz + 1] = 1
        for i in range(1, sz + 1):
            points[i] = nums[i - 1]

        # initialize dp array
        dp = []
        for _ in range(sz + 2):
            inner = []
            for _ in range(sz + 2):
                inner.append(0)
            dp.append(inner)
        # according to dp table
        for i in range(sz, -1, -1):
            for j in range(i + 1, sz + 2):
                for k in range(i + 1, j):
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i][k] + dp[k][j] + points[i] * points[j] * points[k],
                    )
        return dp[0][sz + 1]
