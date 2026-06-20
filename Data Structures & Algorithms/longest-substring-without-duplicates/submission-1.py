class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        values = {}
        max_length = 0
        for i, c in enumerate(s):
            if c in values:
                max_length = max(max_length, i-l)
                l = max(l, values[c] + 1)
            values[c] = i
        max_length = max(max_length, len(s)-l)
        return max_length

        