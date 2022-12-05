# Find First and Last Position of Element in Sorted Array
#
# [Medium] [AC:36.4% 554.5K of 1.5M] [filetype:python3]
#
# Given an array of integers nums sorted in ascending order,
# find the starting and ending position of a given target
# value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
#
# Output: [3,4]
#
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
#
# Output: [-1,-1]
#
# Constraints:
#
# 0 <= nums.length <= 10^5
#
# -10^9 <= nums[i] <= 10^9
#
# nums is a non decreasing array.
#
# -10^9 <= target <= 10^9
#
# [End of Description]:
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left_bound(nums: List[int], target: int):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    right = mid - 1
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
            if left >= len(nums) or nums[left] != target:
                return -1
            return left

        def right_bound(nums: List[int], target: int):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
            if right < 0 or nums[right] != target:
                return -1
            return right

        if not nums:
            return [-1, -1]
        return [left_bound(nums, target), right_bound(nums, target)]
