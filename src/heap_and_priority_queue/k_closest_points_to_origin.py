from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_pts = []
        res = []
        for x, y in points:
            dist = (x**2) + (y**2)
            dist_pts.append([dist, x, y])

        heapq.heapify(dist_pts)
        while k > 0:
            dist, x, y = heapq.heappop(dist_pts)
            res.append([x, y])
            k -= 1
        return res


class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        dist_pts = []
        for x, y in points:
            dist = (x**2) + (y**2)
            dist_pts.append([dist, x, y])

        point = []
        while k > 0:
            closest = float("INF")
            for dist, x, y in dist_pts:
                if dist < closest:
                    closest = dist
                    point = [x, y]

            dist_pts.remove([closest, point[0], point[1]])
            res.append(point)
            k -= 1
        return res
