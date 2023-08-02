from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        src_color = image[sr][sc]
        if src_color == color:
            # avoid inf loop
            return image

        self.dfs(image, sr, sc, src_color, color)

        return image

    def dfs(self, image, i, j, src_color, end_color):
        if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]):
            return
        if image[i][j] != src_color:
            return

        image[i][j] = end_color
        # visited[i][j] = True
        self.dfs(image, i - 1, j, src_color, end_color)
        self.dfs(image, i + 1, j, src_color, end_color)
        self.dfs(image, i, j - 1, src_color, end_color)
        self.dfs(image, i, j + 1, src_color, end_color)

        return


if __name__ == '__main__':
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2
    expected = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    actual = Solution().floodFill(image, sr, sc, color)
    print(expected == actual)

    image = [[0, 0, 0], [0, 0, 0]]
    sr = 0
    sc = 0
    color = 0
    expected = [[0, 0, 0], [0, 0, 0]]
    actual = Solution().floodFill(image, sr, sc, color)
    print(expected == actual)
