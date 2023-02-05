from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res: List[List[int]] = []

        def backtrack(pos: int, curr: List[int], total: int) -> None:
            if total == 0:
                res.append(curr[::])
                return
            if total < 0:
                return
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                curr.append(candidates[i])
                backtrack(i + 1, curr, total - candidates[i])
                curr.pop()
                prev = candidates[i]

        backtrack(0, [], target)
        return res
