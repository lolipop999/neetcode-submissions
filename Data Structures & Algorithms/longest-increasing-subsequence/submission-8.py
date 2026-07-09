class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dynamic programming, bottom up solution
        dp = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            maxVal = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    maxVal = max(maxVal, 1+dp[j])
            dp[i] = maxVal
        return max(dp)