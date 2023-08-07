from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ret = []
        for interval in intervals:
            if not ret or ret[-1][1] < interval[0]:
                ret.append(interval)
            else:
                ret[-1][1] = max(ret[-1][1], interval[1])
        return ret

if __name__ == '__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    expected = [[1,6],[8,10],[15,18]]
    actual = Solution().merge(intervals)
    print(f'expected: {expected}, actual: {actual}')
                
    intervals = [[1,0], [0,1]]
    expected = [[0,1]]
    actual = Solution().merge(intervals)
    print(f'expected: {expected}, actual: {actual}')
