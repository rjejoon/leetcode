from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        res = []

        def backtrack(curr_comb, digit_i, digit_len):
            if digit_i >= digit_len:
                res.append(curr_comb)
                return

            for ch in mapping[digits[digit_i]]:
                backtrack(curr_comb + ch, digit_i + 1, digit_len)

        backtrack('', 0, len(digits))
        return res


if __name__ == '__main__':
    digits = "23"
    print(Solution().letterCombinations(digits))
    digits = "2"
    print(Solution().letterCombinations(digits))
    digits = ''
    print(Solution().letterCombinations(digits))
