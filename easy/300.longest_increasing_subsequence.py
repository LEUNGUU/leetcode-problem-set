# Longest Increasing Subsequence
#
# [Medium] [AC:42.8% 421.8K of 986.2K] [filetype:python3]
#
# Given an unsorted array of integers, find the length of longest increasing subsequence.
#
# Example:
#
# Input: [10,9,2,5,3,7,101,18]
#
# Output: 4
#
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
#
# Note:
#
# There may be more than one LIS combination, it is only necessary for you to return the length.
#
# Your algorithm should run in O(n2) complexity.
#
# Follow up: Could you improve it to O(n log n) time complexity?
#
# [End of Description]:
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sz = len(nums)
        dp = [1] * sz
        for i in range(sz):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
