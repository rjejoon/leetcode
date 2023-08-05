from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for interval in intervals:
            if newInterval[0] < interval[0]:
                if newInterval[1] < interval[0]:
                    # newInterval is before interval
                    result.append(newInterval)
                    newInterval = interval
                else:
                    newInterval[1] = max(newInterval[1], interval[1])
            else:
                if newInterval[0] <= interval[1]:
                    newInterval[0] = interval[0]
                    newInterval[1] = max(newInterval[1], interval[1])
                else:
                    result.append(interval)

        result.append(newInterval)

        return result


if __name__ == '__main__':
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    print(Solution().insert(intervals, newInterval))

    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    print(Solution().insert(intervals, newInterval))

    intervals = [[1, 5]]
    newInterval = [6, 8]
    print(Solution().insert(intervals, newInterval))

    intervals = [[2, 6], [7, 9]]
    newInterval = [15, 18]
    print(Solution().insert(intervals, newInterval))
