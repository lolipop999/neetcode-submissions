class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLength = 0

        def expand(left, right):
            if left < 0 or right >= len(s):
                return left, right
            if s[left] == s[right]:
                return expand(left - 1, right + 1)
            else:
                return left, right

        for i in range(0, len(s)):
            l, r = expand(i, i+1)
            l2, r2 = expand(i-1, i+1)
            l += 1
            r -= 1
            l2 += 1
            r2 -= 1
            if r - l + 1 > resLength:
                resLength = r-l+1
                res = s[l:r+1]
            if r2 - l2 + 1 > resLength:
                resLength = r2-l2+1
                res = s[l2:r2+1]
        return res

        