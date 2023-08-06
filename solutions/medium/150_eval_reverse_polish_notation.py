from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                if t == '+':
                    stack.append(a+b)
                elif t == '-':
                    stack.append(a-b)
                elif t == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))

        return stack.pop()


if __name__ == '__main__':
    tokens = ["10", "6", "9", "3", "+", "-11",
              "*", "/", "*", "17", "+", "5", "+"]
    print(Solution().evalRPN(tokens))
