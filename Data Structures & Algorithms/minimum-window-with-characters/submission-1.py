class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        minWindow = 1001
        charFreq = {}
        for i in range(len(t)):
            charFreq[t[i]] = charFreq.get(t[i], 0) + 1
        # find the initial substring w/ all values
        l = 0
        required_matches = len(charFreq)
        for i in range(len(s)):
            if s[i] in charFreq:
                charFreq[s[i]] -= 1
                if (charFreq[s[i]]) == 0:
                    required_matches -= 1
            while required_matches == 0:
                if minWindow > i-l+1:
                    minWindow = i-l+1
                    res = s[l:i+1]
                # start making window smaller from left, then continue until value found
                if s[l] in charFreq:
                    charFreq[s[l]] += 1
                    if charFreq[s[l]] > 0:
                        required_matches += 1
                l += 1
        return res
        

            


