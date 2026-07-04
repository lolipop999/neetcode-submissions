class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums1 = nums[:-1]
        nums2 = nums[1:]
        
        def maxRob(nums):
            hashmap = {}
            skip = 0
            prev = 0
            for i in range(len(nums)):
                if i == 0:
                    hashmap[i] = nums[i]
                if i >= 2:
                    skip = hashmap[i-2]
                if i >= 1:
                    prev = hashmap[i-1]
                hashmap[i] = max(nums[i] + skip, prev)
            return hashmap[len(nums)-1]
        return max(maxRob(nums1), maxRob(nums2))
        