# Maximum Subarray
#
# [Easy] [AC:46.2% 1M of 2.2M]
# [filetype:python3]
#
# Given an integer array nums, find the
# contiguous subarray (containing at least one
# number) which has the largest sum and return
# its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
#
# Output: 6
#
# Explanation: [4,-1,2,1] has the largest sum
# = 6.
#
# Follow up:
#
# If you have figured out the O(n) solution,
# try coding another solution using the divide
# and conquer approach, which is more subtle.
#
# [End of Description]:
# divide and conquer
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         return self.helper(nums, 0, len(nums) - 1)

#     def helper(self, nums: List[int], left: int, right: int) -> int:
#         if left == right:
#             return nums[left]

#         p = (left + right) // 2

#         left_sum = self.helper(nums, left, p)
#         right_sum = self.helper(nums, p + 1, right)
#         cross_sum = self.cross_sum(nums, left, right, p)

#         return max(left_sum, right_sum, cross_sum)

#     def cross_sum(self, nums: List[int], left: int, right: int, p: int) -> int:
#         if left == right:
#             return nums[left]

#         left_subsum = float("-inf")
#         cur_sum = 0
#         for i in range(p, left - 1, -1):
#             cur_sum += nums[i]
#             left_subsum = max(cur_sum, left_subsum)

#         right_subsum = float("-inf")
#         cur_sum = 0
#         for i in range(p + 1, right + 1):
#             cur_sum += nums[i]
#             right_subsum = max(cur_sum, right_subsum)

#         return left_subsum + right_subsum
# greedy
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         cur_sum = max_sum = nums[0]

#         for i in range(1, len(nums)):
#             cur_sum = max(nums[i], cur_sum + nums[i])
#             max_sum = max(max_sum, cur_sum)
#         return max_sum
# dynamic programming
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            max_sum = max(nums[i], max_sum)
        return max_sum
