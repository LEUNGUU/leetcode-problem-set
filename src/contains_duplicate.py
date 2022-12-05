from typing import List


def containsDuplicate_set(nums: List[int]) -> bool:
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    return False


def containsDuplicate_twopointer(nums: List[int]) -> bool:
    sorted_nums = sorted(nums)
    for i in range(len(nums)):
        if i + 1 <= len(nums) and sorted_nums[i] == sorted_nums[i + 1]:
            return True
    return False
