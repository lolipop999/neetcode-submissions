class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob current house or rob next house
        hashmap = {}
        def dfs(index):
            if index >= len(nums):
                return 0
            if index in hashmap:
                return hashmap[index]

            take = nums[index] + dfs(index+2)
            skip = dfs(index+1)
            hashmap[index] = take
            return max(take, skip)
        return dfs(0)
        