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
        curLevel = []
        numNodes = 1
        while q:
            temp = 0
            for i in range(numNodes):
                node = q.popleft()
                curLevel.append(node.val)
                if node.left:
                    q.append(node.left)
                    temp += 1
                if node.right:
                    q.append(node.right)
                    temp += 1
            res.append(curLevel)
            curLevel = []
            numNodes = temp
        return res

