class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # BFS
        adjList = {i: [] for i in range(n)}

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        visited = set()
        q = deque()
        q.append([0, -1])
        visited.add(0)
        while q:
            node, parent = q.popleft()
            for child in adjList[node]:
                if child == parent:
                    continue
                if child in visited:
                    return False
                else:
                    q.append([child, node])
                visited.add(child)

        return len(visited) == n
                