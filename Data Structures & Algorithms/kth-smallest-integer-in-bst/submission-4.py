# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# brute force method because I can't figure out other method
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # store all the value of nodes in array
        # sort it, then find
        arr = []
        
        def dfs(node):
            if node is None:
                return
            arr.append(node.val)
            dfs(node.right)
            dfs(node.left)

        dfs(root)
        arr.sort()
        return arr[k-1]

        