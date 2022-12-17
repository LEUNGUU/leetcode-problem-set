from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1]:
                continue

            left, right = index + 1, len(nums) - 1
            while left < right:
                currSum = value + nums[left] + nums[right]
                if currSum < 0:
                    left += 1
                elif currSum > 0:
                    right -= 1
                else:
                    res.append([value, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res
