class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            l = r = i
            res += self.countPalindrome(s, l, r)
            l, r = i, i + 1
            res += self.countPalindrome(s, l, r)
        return res

    def countPalindrome(self, s: str, l: int, r: int) -> int:
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count
