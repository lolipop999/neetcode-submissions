class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        expectedTotal = 0
        for i in range(len(nums)):
            total += nums[i]
            expectedTotal += i + 1
        return expectedTotal - total