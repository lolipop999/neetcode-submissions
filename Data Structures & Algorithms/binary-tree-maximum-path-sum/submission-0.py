# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -1001
        
        def dfs(root):
            # DFS of the tree
            if root is None:
                return 0

            # at each root, compute max value to split
            max_right = dfs(root.right)
            max_left = dfs(root.left)

            self.res = max(self.res, max_right + max_left + root.val)

            return max(0, root.val + max(max_right, max_left))
        dfs(root)
        return self.res
