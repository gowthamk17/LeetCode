# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root):
            leafs = []
            if root:
                if not root.left and not root.right:
                    leafs.append(root.val)
                if root.left:
                    leafs += dfs(root.left)
                if root.right:
                    leafs += dfs(root.right)
            return leafs
        return dfs(root1) == dfs(root2)
        