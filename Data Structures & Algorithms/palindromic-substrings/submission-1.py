class Solution:
    def countSubstrings(self, s: str) -> int:
        self.res = 0

        def expand(left, right):
            if left >= 0 and right < len(s):
                if s[left] == s[right]:
                    self.res += 1
                    expand(left-1, right+1)
        for i in range(len(s)):
            self.res += 1
            expand(i, i+1)
            expand(i-1, i+1)
        return self.res
        