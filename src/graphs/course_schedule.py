from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        def dfs(crs: int) -> bool:
            if crs in visit:
                return False

            if pre_map[crs] == []:
                return True
            visit.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            pre_map[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
