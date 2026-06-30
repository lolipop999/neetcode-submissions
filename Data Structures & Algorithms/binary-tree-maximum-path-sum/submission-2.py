# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # find max sum to the left and right
        self.res = -1001

        def dfs(node):
            if node is None:
                return 0
            max_left = max(0, dfs(node.left))
            max_right = max(0, dfs(node.right))
            self.res = max(self.res, max_left + max_right + node.val)
            return max(0, max(max_left, max_right) + node.val)
        
        dfs(root)
        return self.res
        