from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res: List[List[str]] = []
        partition: List[str] = []

        def backtrack(pos: int) -> None:
            if pos >= len(s):
                res.append(partition.copy())
                return
            for index in range(pos, len(s)):
                if self.isPalindrome(s, left=pos, right=index):
                    partition.append(s[pos : index + 1])
                    backtrack(index + 1)
                    partition.pop()

        backtrack(0)
        return res

    def isPalindrome(self, s: str, *, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left + 1, right - 1
        return True
