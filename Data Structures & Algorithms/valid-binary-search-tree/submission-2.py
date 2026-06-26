# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, 1001, -1001)
        
    def valid(self, root: Optional[TreeNode], upper, lower):
        if root is None:
            return True
        if root.val >= upper or root.val <= lower:
            return False

        return (self.valid(root.left, root.val, lower)
                and self.valid(root.right, upper, root.val))
    
    
        
