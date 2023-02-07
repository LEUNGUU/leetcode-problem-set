from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res: List[str] = []
        digitCharMapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(pos: int, curStr: str) -> None:
            if pos == len(digits):
                res.append(curStr)
                return
            for c in digitCharMapping[digits[pos]]:
                backtrack(pos + 1, curStr + c)

        if digits:
            backtrack(0, "")
        return res
