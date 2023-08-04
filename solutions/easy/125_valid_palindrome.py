class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned_s = []
        for ch in s:
            if ch.isalnum():
                cleaned_s.append(ch.lower())

        print(cleaned_s)
        for i in range(len(cleaned_s) // 2):
            if cleaned_s[i] != cleaned_s[len(cleaned_s) - 1 - i]:
                return False
        return True

    def isPalindrome2(self, s: str) -> bool:
        '''
        Uses O(1) space with two pointers
        '''
        i, j = 0, len(s) - 1
        while i < j:
            a, b = s[i].lower(), s[j].lower()
            if a.isalnum() and b.isalnum():
                if a != b:
                    return False
                i += 1
                j -= 1

            if not a.isalnum():
                i += 1
            if not b.isalnum():
                j -= 1

        return True


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    sol = Solution()
    # print(sol.isPalindrome(s))
    print(sol.isPalindrome2(s))

    s = "race a car"
    sol = Solution()
    # print(sol.isPalindrome(s))
    print(sol.isPalindrome2(s))

    s = "0P"
    sol = Solution()
    # print(sol.isPalindrome(s))
    print(sol.isPalindrome2(s))
