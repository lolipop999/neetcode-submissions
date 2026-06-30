# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # we need to use DFS instead or BFS
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return "N,"
        
        add = self.serialize(root.left) + self.serialize(root.right)
        return str(root.val) + "," + add
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")

        self.index = 0

        def dfs():
            if vals[self.index] == "N":
                self.index += 1
                return None
            root = TreeNode(int(vals[self.index]))
            self.index += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()

                
