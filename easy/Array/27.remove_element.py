# Remove Element
#
# [Easy] [AC:47.7% 592.5K of 1.2M] [filetype:python3]
#
# Given an array nums and a value val, remove all instances of that value
# in-place and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond
# the new length.
#
# Example 1:
#
# Given nums = [3,2,2,3], val = 3,
#
# Your function should return length = 2, with the first two elements of nums
# being 2.
#
# It doesn't matter what you leave beyond the returned length.
#
# Example 2:
#
# Given nums = [0,1,2,2,3,0,4,2], val = 2,
#
# Your function should return length = 5, with the first five elements of nums
# containing 0, 1, 3, 0, and 4.
#
# Note that the order of those five elements can be arbitrary.
#
# It doesn't matter what values are set beyond the returned length.
#
# Clarification:
#
# Confused why the returned value is an integer but your answer is an array?
#
# Note that the input array is passed in by reference, which means modification
# to the input array will be known to the caller as well.
#
# Internally you can think of this:
#
# // nums is passed in by reference. (i.e., without making a copy)
#
# int len = removeElement(nums, val);
#
# // any modification to nums in your function would be known by the caller.
#
# // using the length returned by your function, it prints the first len
# elements.
#
# for (int i = 0; i < len; i++) {
#
#     print(nums[i]);
#
# }
#
# [End of Description]:

# Two Pointer(no changes to array)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        pointerA = 0
        for pointerB in range(0, n):
            if nums[pointerB] != val:
                # actually we copy values much more times than needed
                # in this algorithm
                nums[pointerA] = nums[pointerB]
                pointerA += 1
        return pointerB


# Two Pointer(modify the array by changing its values)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        pointerA = 0
        while pointerA < n:
            if nums[pointerA] != val:
                pointerA += 1
            else:
                nums[pointerA] = nums[n - 1]
                # reduce the size of the array
                n -= 1
        return n


# This is mine. It will changed the array by removing all the target values in array
# since I modify the array dynamically, then we need to calculate the length of array
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        else:
            index = 0
            while index < len(nums):
                if nums[index] == val:
                    nums.pop(index)
                else:
                    index += 1
            return len(nums)
