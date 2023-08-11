class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        i = 0
        n = 0
        while i < len(s) and s[i] == ' ':
            i += 1

        is_neg = False
        if i < len(s) and s[i] in ['+', '-']:
            is_neg = s[i] == '-'
            i += 1

        start = i
        while i < len(s) and s[i].isdigit():
            i += 1
            n += 1

        i = start
        res = 0
        while i < len(s) and s[i].isdigit():
            res = 10 * res + (ord(s[i]) - ord('0'))
            i += 1

        if is_neg:
            res = -res
        if res < -2**31:
            res = -2**31
        elif res > 2**31-1:
            res = 2**31-1
        return res


if __name__ == '__main__':
    s = '  -42'
    s = '+-12'
    print(Solution().myAtoi(s))
