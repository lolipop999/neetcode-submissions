class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 1
        hashmap = {}
        def dfs(i, j): # j is previously stored
            if i == len(nums):
                return 0
            if (i, j) in hashmap:
                return hashmap[(i, j)]
            
            skip = dfs(i+1, j)

            take = 0
            if j == -1 or nums[i] > nums[j]:
                take = 1 + dfs(i+1, i)
            hashmap[(i, j)] = max(take, skip)
            return hashmap[(i, j)]
        return dfs(0, -1)
