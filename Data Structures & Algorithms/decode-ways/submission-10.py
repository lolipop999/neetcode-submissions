class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}

        def dps(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            res = dps(i+1)
            if i < len(s) - 1 and int(s[i]) * 10 + int(s[i+1]) <= 26:
                res += dps(i+2)
            dp[i] = res
            return res
        return dps(0)
            