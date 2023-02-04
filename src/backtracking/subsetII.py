from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        nums.sort()

        def backtrack(i: int, subset: List[int]) -> None:
            if i == len(nums):
                res.append(subset[::])
                return

            # Include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # Not include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res


class Solution2:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        nums.sort()

        subset: List[int] = []

        def dfs(i: int) -> None:
            if i == len(nums):
                res.append(subset[::])
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return res
