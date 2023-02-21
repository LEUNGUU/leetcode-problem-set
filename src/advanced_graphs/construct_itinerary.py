from typing import List
from collections import deque


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_map = {src: deque() for src, _ in tickets}
        tickets.sort()
        for src, dst in tickets:
            adj_map[src].append(dst)

        res: List[str] = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj_map:
                return False
            temp = list(adj_map[src])
            for v in temp:
                adj_map[src].popleft()
                res.append(v)
                if dfs(v):
                    return res
                res.pop()
                adj_map[src].append(v)
            return False

        dfs("JFK")
        return res
