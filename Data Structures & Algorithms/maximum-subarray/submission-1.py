class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = 0
        maxRes = nums[0]
        for n in nums:
            if res < 0:
                res = 0
            res += n
            maxRes = max(maxRes, res)
            
            
        return maxRes
            
        