from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWs, COLs = len(grid), len(grid[0])
        time, fresh = 0, 0
        q = deque()

        for r in range(ROWs):
            for c in range(COLs):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    nrow, ncol = row + dr, col + dc
                    if (
                        nrow < 0
                        or nrow >= ROWs
                        or ncol < 0
                        or ncol >= COLs
                        or grid[nrow][ncol] in [0, 2]
                    ):
                        continue
                    fresh -= 1
                    grid[nrow][ncol] = 2
                    q.append((nrow, ncol))
            time += 1
        return time if fresh == 0 else -1
