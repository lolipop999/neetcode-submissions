class Solution:
    def countBits(self, n: int) -> List[int]:
        # dynamic programming solution
        dp = [0] * (n+1)
        # if factor of 2, add to hashmap
        lastMult = 1
        for i in range(1, n+1):
            if lastMult * 2 == i:
                lastMult = i
            dp[i] = (1+ dp[i-lastMult])
        return dp
            
            