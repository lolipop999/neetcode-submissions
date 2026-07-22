class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #hashmap store paths
        hashmap2d = {}
        hashmap2d[m-1, n-1] = 1

        # first use brute force
        def dfs(r, c):
            if r >= m or c >= n:
                return 0
            if (r, c) in hashmap2d:
                return hashmap2d[r, c]
            hashmap2d[r, c] = dfs(r+1, c) + dfs(r, c+1)
            return hashmap2d[r, c]
        return dfs(0, 0)
        
