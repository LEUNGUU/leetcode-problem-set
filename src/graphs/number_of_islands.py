from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r: int, c: int) -> None:
            q = deque()
            visit.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in direction:
                    r, c = row + dr, col + dc
                    if (
                        r in range(rows)
                        and c in range(cols)
                        and (r, c) not in visit
                        and grid[r][c] == "1"
                    ):
                        visit.add((r, c))
                        q.append((r, c))

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands
