# Search Insert Position
# 
# [Easy] [AC:41.7% 572.2K of 1.4M] [filetype:python3]
# 
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
# 
# You may assume no duplicates in the array.
# 
# Example 1:
# 
# Input: [1,3,5,6], 5
# 
# Output: 2
# 
# Example 2:
# 
# Input: [1,3,5,6], 2
# 
# Output: 1
# 
# Example 3:
# 
# Input: [1,3,5,6], 7
# 
# Output: 4
# 
# Example 4:
# 
# Input: [1,3,5,6], 0
# 
# Output: 0
# 
# [End of Description]:
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lenOfnums = len(nums)
        if lenOfnums == 0:
            return 0
        else:
            mid = len(nums) // 2
            while 0 <= mid <= (lenOfnums -1):
                if nums[mid] > target:
                    mid = (0 + mid) // 2
                elif nums[mid] < target:
                    mid = (mid + lenOfnums - 1) // 2
                else:
                    return mid


