class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0
        numbers = set()
        for n in nums:
            numbers.add(n)
        for n in numbers:
            if n-1 not in numbers:
                i = 1
                while n+i in numbers:
                    i += 1
                maxLength = max(i, maxLength)
        return maxLength