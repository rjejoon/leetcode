from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for pt in points:
            heapq.heappush(pq, (self.dist_to_origin(pt), pt))

        return [heapq.heappop(pq)[1] for _ in range(k)]

    def dist_to_origin(self, point: List[int]) -> int:
        return point[0]**2 + point[1]**2
