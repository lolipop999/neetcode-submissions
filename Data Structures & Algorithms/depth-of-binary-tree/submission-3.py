# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # try DFS iteratively, no recursion (using stack)
        if not root:
            return 0
        ans = 1
        stack = [[root, 1]]
        while stack:
            node, depth = stack.pop(0)
            ans = max(ans, depth)
            if (node.left):
                stack.append([node.left, depth+1])
            if node.right:
                stack.append([node.right, depth+1])
        return ans
        