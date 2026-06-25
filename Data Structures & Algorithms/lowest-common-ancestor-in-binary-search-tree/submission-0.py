# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # BFS, using queue
        queue = deque()
        queue.append(root.left)
        queue.append(root.right)
        res = root
        while queue:
            node = queue.popleft()
            if self.containsVals(node, p) and self.containsVals(node, q):
                res = node
                queue.append(node.left)
                queue.append(node.right)
        return res
        # does left or right contain, if yes, continue going down left or right, store lowest val
    def containsVals(self, root: TreeNode, p: TreeNode):
        if root is None:
            return False
        if root.val == p.val:
            return True
        return self.containsVals(root.left, p) or self.containsVals(root.right, p)
            
