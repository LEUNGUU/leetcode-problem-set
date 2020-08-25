# Contains Duplicate
#
# [Easy] [AC:55.8% 564K of 1M] [filetype:python3]
#
# Given an array of integers, find if the array contains any
# duplicates.
#
# Your function should return true if any value appears at least twice
# in the array, and it should return false if every element is
# distinct.
#
# Example 1:
#
# Input: [1,2,3,1]
#
# Output: true
#
# Example 2:
#
# Input: [1,2,3,4]
#
# Output: false
#
# Example 3:
#
# Input: [1,1,1,3,3,4,3,2,4,2]
#
# Output: true
#
# [End of Description]:

# brute-force(Not Accepted, Time Exceeded)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


# Hash Table
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = set()
        for item in nums:
            if item in check:
                return True
            check.add(item)
        return False


# Sorting
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


# 1-line Sorting
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
