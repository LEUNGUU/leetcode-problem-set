from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWs, COLs = len(grid), len(grid[0])
        visit = set()

        def dfs(r: int, c: int) -> int:
            if (
                r < 0
                or r == ROWs
                or c < 0
                or c == COLs
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        area = 0
        for r in range(ROWs):
            for c in range(COLs):
                area = max(area, dfs(r, c))
        return area
