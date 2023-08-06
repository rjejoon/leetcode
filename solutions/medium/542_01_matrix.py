from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    continue
                left = mat[r][c-1] if c > 0 else float('inf')
                up = mat[r-1][c] if r > 0 else float('inf')
                mat[r][c] = min(left, up) + 1

        for r in reversed(range(len(mat))):
            for c in reversed(range(len(mat[0]))):
                if mat[r][c] == 0:
                    continue
                bottom = mat[r+1][c] if r+1 < len(mat) else float('inf')
                right = mat[r][c+1] if c+1 < len(mat[0]) else float('inf')
                mat[r][c] = min(mat[r][c], min(bottom, right)+1)

        return mat


if __name__ == '__main__':
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    Solution().updateMatrix(mat)

    mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    Solution().updateMatrix(mat)

    mat = [[0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [
        0, 0, 0, 1, 0], [1, 0, 1, 1, 1], [1, 0, 0, 0, 1]]
    out = Solution().updateMatrix(mat)
    expected = [[0, 1, 0, 1, 2],
                [1, 1, 0, 0, 1],
                [0, 0, 0, 1, 0],
                [1, 0, 1, 1, 1],
                [1, 0, 0, 0, 1]]
    assert out == expected, (out, expected)

    mat = [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [
        0, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 0], [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]
    out = Solution().updateMatrix(mat)
    expected = [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [
        0, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 2, 1, 1, 0, 1], [2, 1, 1, 1, 1, 2, 1, 0, 1, 0], [3, 2, 2, 1, 0, 1, 0, 0, 1, 1]]
    assert out == expected, (out, expected)

    mat = [[1, 1, 0, 0, 1, 0, 0, 1, 1, 0], [1, 0, 0, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1, 1, 0], [
        1, 1, 1, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 0, 0, 1, 1, 1], [0, 1, 0, 1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 0, 1, 0, 1, 1, 1, 1]]
    out = Solution().updateMatrix(mat)
