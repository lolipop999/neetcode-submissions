class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax = nums[0]
        curMin = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                curMax, curMin = curMin, curMax
             
            curMax = max(nums[i], curMax * nums[i])
            curMin = min(nums[i], curMin * nums[i])
            print(curMax, curMin)
            res = max(res, curMax)
        return res