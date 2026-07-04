class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob current house or rob next house
        hashmap = {}
        def dfs(index):
            if index >= len(nums):
                return 0
            if (index+2) in hashmap:
                i2 = hashmap[index+2]
            else:
                i2 = dfs(index + 2)
            if (index+1) in hashmap:
                i1 = hashmap[index+1]
            else:
                i1 = dfs(index+1)
            hashmap[index] = nums[index] + i2

            return max(hashmap[index], i1)
        return dfs(0)
        