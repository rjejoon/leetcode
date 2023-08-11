from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        stop = min(m, n) // 2
        res = []
        step = 0
        while step <= stop:
            if step < m:
                for c in range(step, n):
                    res.append(matrix[step][c])

            if step < n:
                for r in range(step+1, m):
                    res.append(matrix[r][n-1])

            if step < m-1:
                for c in reversed(range(step, n-1)):
                    res.append(matrix[m-1][c])

            if step < n-1:
                for r in reversed(range(step+1, m-1)):
                    res.append(matrix[r][step])

            step += 1
            m -= 1
            n -= 1

        return res

    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        '''
        Uses 4 pointers to track the boundaries of the matrix
        '''
        m, n = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, n - 1, 0, m - 1
        res = []
        while left <= right and top <= bottom:
            #  top left to top right
            for col in range(left, right+1):
                res.append(matrix[top][col])
            top += 1
            # top right to right bottom
            for row in range(top, bottom+1):
                res.append(matrix[row][right])
            right -= 1
            # right bottom to right left
            for col in range(right, left-1, -1):
                res.append(matrix[bottom][col])
            bottom -= 1
            # left bottom to top left
            for row in range(bottom, top-1, -1):
                res.append(matrix[row][left])
            left += 1
        # just ignore the redundant and return length of m*n
        return res[:m*n]


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    print(Solution().spiralOrder(matrix))

    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(Solution().spiralOrder(matrix))

    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
    print(Solution().spiralOrder(matrix))

    matrix = [[2, 5, 8], [4, 0, -1]]
    print(Solution().spiralOrder(matrix))
