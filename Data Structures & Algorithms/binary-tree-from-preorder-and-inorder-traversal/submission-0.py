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
        dummy = TreeNode(0)
        curr = dummy
        curr.val = preorder[0]
        del preorder[0]
        hashmap = {}
    
        for i in range(len(inorder)):
            hashmap[inorder[i]] = i
        
        index = hashmap.get(curr.val)
        inorder.pop(index)

        left_tree = preorder[:index]
        curr.left = self.buildTree(left_tree, inorder)
        right_tree = preorder[index:]
        curr.right = self.buildTree(right_tree, inorder)

        return dummy
        
        