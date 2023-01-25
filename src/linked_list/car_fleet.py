from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars: List[List[int, int]] = [[p, s] for p, s in zip(position, speed)]

        stack: List[float] = []
        for car in sorted(cars)[::-1]:
            stack.append((target - car[0]) / car[1])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
