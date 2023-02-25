# N-Queens
#
# [Hard] [AC:47.3% 214.3K of 453.5K] [filetype:python3]
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate
# a queen and an empty space respectively.
#
# Example:
#
# Input: 4
#
# Output: [
#
#  [".Q..",  // Solution 1
#
#   "...Q",
#
#   "Q...",
#
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#
#   "Q...",
#
#   "...Q",
#
#   ".Q.."]
#
# ]
#
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
#
# [End of Description]:
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(board: List[List[str]], row: int) -> None:
            # check if it is ended
            if len(board) == row:
                # change list to str to match the result
                copyOfboard = ["".join(item) for item in board]
                res.append(copyOfboard)
                return

            # every col in a row is choices
            for col in range(len(board[row])):
                # avoid illegal choice
                if not isValid(board, row, col):
                    continue
                # make decision
                board[row][col] = "Q"
                # go to next row
                backtrack(board, row + 1)
                # revoke decision
                board[row][col] = "."

        def isValid(board: List[List[int]], row: int, col: int) -> bool:
            n = len(board)
            # check in the same col
            for i in range(n):
                if board[i][col] == "Q":
                    return False

            # check upper right
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
                if board[i][j] == "Q":
                    return False

            # check upper left
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if board[i][j] == "Q":
                    return False
            return True

        res = []
        # initial empty board
        board = []
        for _ in range(n):
            inner = []
            for _ in range(n):
                inner.append(".")
            board.append(inner)
        backtrack(board, 0)
        return res
