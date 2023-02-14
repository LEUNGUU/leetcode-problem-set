from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWs, COLs = len(board), len(board[0])

        def capture(r: int, c: int) -> None:
            if r < 0 or c < 0 or r >= ROWs or c >= COLs or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # (O -> T)
        for r in range(ROWs):
            for c in range(COLs):
                if board[r][c] == "O" and (r in [0, ROWs - 1] or c in [0, COLs - 1]):
                    capture(r, c)
        # (O -> X)
        for r in range(ROWs):
            for c in range(COLs):
                if board[r][c] == "O":
                    board[r][c] = "X"
        # (T -> O)
        for r in range(ROWs):
            for c in range(COLs):
                if board[r][c] == "T":
                    board[r][c] = "O"
