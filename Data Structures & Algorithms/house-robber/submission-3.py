class Solution:
    def rob(self, nums: List[int]) -> int:
        maxAtIndex = {}
        self.maxPrev = 0
        self.maxBefore = 0

        for i in range(len(nums)):
            if i >= 2:
                self.maxPrev = maxAtIndex[i-2]
            if i >= 1:
                self.maxBefore = maxAtIndex[i-1]
            maxAtIndex[i] = max(nums[i] + self.maxPrev, self.maxBefore)
        return maxAtIndex[len(nums)-1]