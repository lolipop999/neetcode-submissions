class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for i in range(cols)] for j in range(rows)]
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] == "0":
                return
            if visited[r][c]:
                return
            visited[r][c] = True

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        res = 0
        for r in range(rows):
            for c in range(cols):
                if not visited[r][c] and grid[r][c] == "1":
                    dfs(r, c)
                    res += 1

        return res
        

