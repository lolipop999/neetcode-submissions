class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        # count the length of the window and the most frequent character
        charCount = [0] * 26
        ans = 0
        maxFreq = 0
        l = 0

        for i in range(len(s)):
            charCount[ord(s[i])-65] += 1
            maxFreq = max(maxFreq, charCount[ord(s[i])-65])
            while (i - l + 1) - maxFreq > k:
                charCount[ord(s[l])-65] -= 1
                l += 1
            ans = max(ans, i-l+1)
        return ans
        