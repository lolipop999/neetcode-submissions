class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        if not edges:
            return True
        # building adj list 
        visited = set()

        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for child in adj[node]:
                if child == parent:
                    continue
                if not dfs(child, node):
                    return False
            return True
        return dfs(edges[0][0], -1) and len(visited) == n
            
            
        

