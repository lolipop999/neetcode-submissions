# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        curr = TreeNode(preorder[0])

        index = inorder.index(curr.val)

        left_tree = preorder[1:index+1]
        curr.left = self.buildTree(left_tree, inorder[:index])
        right_tree = preorder[index+1:]
        curr.right = self.buildTree(right_tree, inorder[index+1:])

        return curr
        
        