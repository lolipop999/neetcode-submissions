class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sort = sorted(nums)
        print(sort)
        maxLength = 0
        length = 1
        for i in range(len(sort)-1):
            if (sort[i] + 1 == sort[i+1]):
                length += 1
            elif (sort[i] == sort[i+1]):
                continue
            else:
                maxLength = max(maxLength, length)
                length = 1
        return max(length, maxLength)