# Merge Sorted Array
#
# [Easy] [AC:39.0% 569.4K of 1.5M] [filetype:python3]
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
#
# Note:
#
# The number of elements initialized in nums1 and nums2 are m and
# n respectively.
#
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
#
# Example:
#
# Input:
#
# nums1 = [1,2,3,0,0,0], m = 3
#
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]
#
# [End of Description]:

# Merge and Sorted(pretty bad time complexity)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:] = sorted(nums1[:m] + nums2)


# noted: two sorted arrays
# Two Pointer(start from beginning)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # make a copy of nums1
        nums1_copy = nums1[:m]
        nums1[:] = []

        # Two get pointers for nums1_copy and nums2
        p1 = 0
        p2 = 0

        # Compare elements from nums1_copy and nums2
        # and add the smallest one into nums1
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        # if there are still elements to add
        if p1 < m:
            nums1[(p1 + p2) :] = nums1_copy[1:]
        if p2 < n:
            nums1[(p1 + p2) :] = nums2[p2:]


# Two Pointer(start from end)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # two get pointers for nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        # set pointers for nums1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        # add missing elements from nums2
        nums1[: (p2 + 1)] = nums2[: (p2 + 1)]
