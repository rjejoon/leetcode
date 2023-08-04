class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = []
        longer = a if len(a) >= len(b) else b
        shorter = a if len(a) < len(b) else b
        i = len(shorter) - 1
        j = len(longer) - 1
        while i >= 0:
            s = int(shorter[i])
            l = int(longer[j])
            i -= 1
            j -= 1
            result.append(str((s+l+carry) % 2))
            carry = (s + l + carry) // 2

        while carry == 1 or j >= 0:
            l = int(longer[j]) if j >= 0 else 0
            j -= 1
            result.append(str((l+carry) % 2))
            carry = l & carry

        return ''.join(result[::-1])

    def addBinary2(self, a: str, b: str) -> str:
        '''
        This is a better solution from leetcode
        '''
        ret = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(a[j])
                j -= 1
            ret.append(str(carry % 2))
            carry //= 2

        return ''.join(reversed(ret))


if __name__ == '__main__':
    a = '1010'
    b = '1011'
    print(Solution().addBinary(a, b))

    a = '1010'
    b = '1011'
    # print(Solution().addBinary(a, b))
