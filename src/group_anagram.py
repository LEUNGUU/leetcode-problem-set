from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            letter_counter = [0] * 26
            for c in s:
                letter_counter[ord(c) - ord("a")] += 1
            hashmap[tuple(letter_counter)].append(s)

        return hashmap.values()
