# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # we can do BFS or DFS for both and if any value is not the same return False
        stack1 = [p]
        stack2 = [q]

        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if node1 is None and node2 is None:
                continue
            if node1 is None or node2 is None: # since we already checked if both were none, if either are none return false
                return False
            if not node1.val == node2.val:
                return False
            stack1.append(node1.left)
            stack1.append(node1.right)
            stack2.append(node2.left)
            stack2.append(node2.right)
        return True