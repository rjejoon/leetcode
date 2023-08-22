from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        dp = [0] * int(2e5+1)

        for i in reversed(range(len(questions))):
            dp[i] = max(dp[i+1],
                        questions[i][0] + dp[i + questions[i][1] + 1])

        return dp[0]


if __name__ == '__main__':
    questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
    print(Solution().mostPoints(questions))
