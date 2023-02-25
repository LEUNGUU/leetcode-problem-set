# Remove Duplicates from Sorted Array
#
# [Easy] [AC:44.4% 939.9K of 2.1M]
# [filetype:python3]
#
# Given a sorted array nums, remove the
# duplicates in-place such that each element
# appear only once and return the new length.
#
# Do not allocate extra space for another
# array, you must do this by modifying the
# input array in-place with O(1) extra memory.
#
# Example 1:
#
# Given nums = [1,1,2],
#
# Your function should return length = 2, with
# the first two elements of nums being 1 and
# 2 respectively.
#
# It doesn't matter what you leave beyond the
# returned length.
#
# Example 2:
#
# Given nums = [0,0,1,1,1,2,2,3,3,4],
#
# Your function should return length = 5, with
# the first five elements of nums being
# modified to 0, 1, 2, 3, and 4 respectively.
#
# It doesn't matter what values are set beyond
# the returned length.
#
# Clarification:
#
# Confused why the returned value is an
# integer but your answer is an array?
#
# Note that the input array is passed in by
# reference, which means modification to the
# input array will be known to the caller as
# well.
#
# Internally you can think of this:
#
# // nums is passed in by reference. (i.e.,
# without making a copy)
#
# int len = removeDuplicates(nums);
#
# // any modification to nums in your function
# would be known by the caller.
#
# // using the length returned by your
# function, it prints the first len elements.
#
# for (int i = 0; i < len; i++) {
#
#     print(nums[i]);
#
# }
#
# [End of Description]:

# Two Pointers(in case of the array is already sorted)


# while loop version
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) in [0, 1]:
            return len(nums)
        else:
            i, j = 0, 1
            while j <= len(nums) - 1:
                if nums[i] != nums[j]:
                    i += 1
                    # if not equal, there are two cases:
                    # 1. i + 1 = j, then value is not changed
                    # 2. i + 1 < j, then values are swapped.
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
            return i + 1


# for loop version
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n in [0, 1]:
            return n
        else:
            i = 0
            for j in range(1, n):
                if nums[i] != nums[j]:
                    i += 1
                    # if not equal, there are two cases:
                    # 1. i + 1 = j, then value is not changed
                    # 2. i + 1 < j, then values are swapped.
                    nums[i], nums[j] = nums[j], nums[i]
            return i + 1
