from typing import List
from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        characterCount = Counter(tasks)
        maxHeap = [-cnt for cnt in characterCount.values()]
        heapq.heapify(maxHeap)

        queue = deque()
        time = 0

        while queue or maxHeap:
            time += 1
            if maxHeap:
                curr = 1 + heapq.heappop(maxHeap)
                if curr:
                    queue.append([curr, time + n])

            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
        return time
