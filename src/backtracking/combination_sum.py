from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i: int, curr: List[int], total: int) -> None:
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res
