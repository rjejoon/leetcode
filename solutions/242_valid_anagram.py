class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Assume ascii
        '''
        if len(s) != len(t):
            return False

        dat_s = [0] * 256
        dat_t = [0] * 256

        for i in range(len(s)):
            dat_s[ord(s[i])] += 1
            dat_t[ord(t[i])] += 1

        for i in range(256):
            if dat_s[i] != dat_t[i]:
                return False

        return True


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    sol = Solution()
    print(sol.isAnagram(s, t))

    s = "rat"
    t = "car"
    sol = Solution()
    print(sol.isAnagram(s, t))
