# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # recusive DFS
        # at each level check if it contains first part of subroot
        if subRoot is None:
            return True
        if root is None:
            return False
        if root.val == subRoot.val:
            if self.isSametree(root, subRoot):
                return True
        return (self.isSubtree(root.left, subRoot)
        or self.isSubtree(root.right, subRoot))

    def isSametree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]):
        
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        if root.val != subRoot.val:
            return False
        return self.isSametree(root.left, subRoot.left) and self.isSametree(root.right, subRoot.right) 