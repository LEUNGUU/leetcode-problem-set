class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_map = {}
        for ch in s:
            if ch in char_map.keys():
                char_map[ch] += 1
            else:
                char_map[ch] = 1
        for ch in t:
            if ch in char_map.keys():
                char_map[ch] -= 1
                if char_map[ch] == 0:
                    del char_map[ch]
            else:
                # There is a character not in s
                return False
        return True
