# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #BFS
        if root is None:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            numNodes = len(q)
            curLevel = []
            for i in range(numNodes):
                node = q.popleft()

                if node:
                    curLevel.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if curLevel:
                res.append(curLevel)
        
        return res

