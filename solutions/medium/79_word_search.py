from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited = [[False] * len(board[0]) for _ in range(len(board))]

        def dfs(r, c, word_i, length):
            if word_i >= length:
                return True

            visited[r][c] = True

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                    if not visited[nr][nc] and board[nr][nc] == word[word_i]:
                        if dfs(nr, nc, word_i + 1, length):
                            return True

            visited[r][c] = False
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if dfs(r, c, 1, len(word)):
                        return True
        return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(Solution().exist(board, word))
    word = "SEE"
    print(Solution().exist(board, word))
    word = "ABCB"
    print(Solution().exist(board, word))
