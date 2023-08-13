from typing import List
from collections import Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = 0
        task_counts = Counter(tasks)
        pq = []
        for key in task_counts:
            heapq.heappush(pq, [-task_counts[key], key])

        while pq:
            cooldown = n
            tmp = []
            max_task = heapq.heappop(pq)
            max_task[0] += 1
            if max_task[0] < 0:
                tmp.append(max_task)

            res += 1

            i = 0
            while pq and i < cooldown:
                t = heapq.heappop(pq)
                t[0] += 1
                if t[0] < 0:
                    tmp.append(t)

                res += 1
                cooldown -= 1

            if tmp:
                for t in tmp:
                    heapq.heappush(pq, t)

            if pq:
                res += cooldown

        return res

    def leastInterval2(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_count = task_counts.most_common(1)[0][1]
        num_max_count_tasks = sum(
            1
            for task in task_counts
            if task_counts[task] == max_count
        )
        res = (max_count-1) * (n+1) + num_max_count_tasks
        # min possible time is len(tasks); take account of n = 0
        return max(res, len(tasks))


if __name__ == '__main__':
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    solution = Solution()
    # assert solution.leastInterval(tasks, n) == 8

    tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    n = 2
    solution = Solution()
    # assert solution.leastInterval(tasks, n) == 16

    tasks = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"]
    n = 2
    solution = Solution()
    assert solution.leastInterval(tasks, n) == 12
