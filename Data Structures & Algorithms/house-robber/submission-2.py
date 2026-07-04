class Solution:
    def rob(self, nums: List[int]) -> int:
        maxAtIndex = {}
        self.maxPrev = 0
        self.maxBefore = 0

        def dfs(index):
            if index == len(nums):
                return maxAtIndex[index-1]
            if index >= 2:
                self.maxPrev = maxAtIndex[index-2]
            if index >= 1:
                self.maxBefore = maxAtIndex[index-1]
            maxAtIndex[index] = max(nums[index] + self.maxPrev, self.maxBefore)
            return dfs(index + 1)
        return dfs(0)