# Paint House
#
# [Easy] [AC:52.0% 86.7K of 166.8K] [filetype:python3]
#
# There are a row of n houses, each house can be painted with one of
# the three colors: red, blue or green. The cost of painting each
# house with a certain color is different. You have to paint all the
# houses such that no two adjacent houses have the same color.
#
# The cost of painting each house with a certain color is represented
# by a n x 3 cost matrix. For example, costs[0][0] is the cost of
# painting house 0 with color red; costs[1][2] is the cost of painting
# house 1 with color green, and so on... Find the minimum cost to
# paint all houses.
#
# Note:
#
# All costs are positive integers.
#
# Example:
#
# Input: [[17,2,17],[16,16,5],[14,3,19]]
#
# Output: 10
#
# Explanation: Paint house 0 into blue, paint house 1 into green,
# paint house 2 into blue.
#
#              Minimum cost: 2 + 5 + 3 = 10.
#
# [End of Description]:

# Brute force with a recursive tree(Plus Memoization)
from functools import lru_cache


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        @lru_cache(maxsize=None)
        def paint_cost(n, color):
            total_cost = costs[n][color]
            if n == len(costs) - 1:
                pass
            elif color == 0:  # Red
                total_cost += min(paint_cost(n + 1, 1), paint_cost(n + 1, 2))
            elif color == 1:  # Green
                total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 2))
            else:  # Blue
                total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 1))
            return total_cost

        if costs == []:
            return 0
        return min(paint_cost(0, 0), paint_cost(0, 1), paint_cost(0, 2))


# Dynamic Programming
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        for n in reversed(range(len(costs) - 1)):
            # Total cost of painting nth house red
            costs[n][0] += min(costs[n + 1][1], costs[n + 1][2])
            # Total cost of painting nth house green
            costs[n][1] += min(costs[n + 1][0], costs[n + 1][2])
            #  Total cost of painting nth house blue
            costs[n][2] += min(costs[n + 1][0], costs[n + 1][1])
        if len(costs) == 0:
            return 0
        return min(costs[0])  # return the minimum in the first row


# Dynamic Programming with Optimized Space Complexity
from copy import deepcopy


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0
        previous_row = costs[-1]
        for n in reversed(range(len(costs) - 1)):
            # since we dont want to modify the input array
            current_row = deepcopy(costs[n])
            # Total cost of painting nth house red
            current_row[0] += min(previous_row[1], previous_row[2])
            # Total cost of painting nth house green
            current_row[1] += min(previous_row[0], previous_row[2])
            # Total cost of painting nth house blue
            current_row[2] += min(previous_row[0], previous_row[1])
            previous_row = current_row

        return min(previous_row)
