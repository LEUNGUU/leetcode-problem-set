from typing import List, Union


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> Union[int, None]:
        cost.append(0)  # add the top floor
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])
