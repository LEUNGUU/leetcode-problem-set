from typing import List

# QuickSort Method


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k  # Index of k largest element

        def quickSelect(start, end):
            pivot, pointer = nums[end], start
            for i in range(start, end):
                if nums[i] <= pivot:
                    nums[i], nums[pointer] = nums[pointer], nums[i]
                    pointer += 1
            nums[pointer], nums[end] = nums[end], nums[pointer]  # End is the pivot
            if k > pointer:
                return quickSelect(pointer + 1, end)
            elif k < pointer:
                return quickSelect(start, pointer - 1)
            else:
                return nums[pointer]

        return quickSelect(0, len(nums) - 1)
