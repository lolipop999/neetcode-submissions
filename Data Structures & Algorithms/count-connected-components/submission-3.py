class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #DFS
        #create adj list

        adj = {i: [] for i in range(n)}

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        res = 0
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for child in adj[node]:
                dfs(child)
            del adj[node]
        
        # remove those from a list, keep going until list is empty
        # everytime need to run dfs is an unconnected node
        while adj:
            res += 1
            node = next(iter(adj), None)
            dfs(node)
        return res
        