from typing import List, Set


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWs, COLs = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r: int, c: int, visit: Set, prev_height: int) -> None:
            if (
                r < 0
                or c < 0
                or r >= ROWs
                or c >= COLs
                or heights[r][c] < prev_height
                or (r, c) in visit
            ):
                return
            visit.add((r, c))
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])

        for c in range(COLs):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWs - 1, c, atl, heights[ROWs - 1][c])

        for r in range(ROWs):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLs - 1, atl, heights[r][COLs - 1])

        res = []
        for r in range(ROWs):
            for c in range(COLs):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
