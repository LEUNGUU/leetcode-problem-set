from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            heaviest = heapq.heappop(stones)
            heavier = heapq.heappop(stones)
            if heaviest < heavier:
                heapq.heappush(stones, heaviest - heavier)
        return abs(stones[0]) if stones else 0


class Solution2:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while True:
            if not stones:
                return 0
            if len(stones) == 1:
                return stones[0]
            heaviest, heavier, pos = -1, -1, 0
            for index, value in enumerate(stones):
                if value > heaviest:
                    heaviest = value
                    pos = index
            stones = stones[:pos] + stones[pos + 1 :]
            for index, value in enumerate(stones):
                if value > heavier:
                    heavier = value
                    pos = index
            stones = stones[:pos] + stones[pos + 1 :]
            if heaviest > heavier:
                stones.append(heaviest - heavier)
        return -1
