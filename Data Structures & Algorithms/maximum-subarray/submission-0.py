class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = 0
        maxRes = nums[0]
        for n in nums:
            res += n
            if res > maxRes:
                maxRes = res
            if res < 0:
                res = 0
            
        return maxRes
            
        