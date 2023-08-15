from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                _, j = stack.pop()
                ans[j] = i - j
            stack.append((t, i))

        return ans


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution().dailyTemperatures(temperatures))

    temperatures = [30, 40, 50, 60]
    print(Solution().dailyTemperatures(temperatures))

    temperatures = [30, 60, 90]
    print(Solution().dailyTemperatures(temperatures))
