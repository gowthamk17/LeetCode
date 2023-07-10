# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        # leaf node with no children
        if root.left is None and root.right is None:
            return 1
        
        # if no right subtree
        if root.right is None:
            return self.minDepth(root.left) + 1
        
        # if no left subtree
        if root.left is None:
            return self.minDepth(root.right) + 1
        
        # both subree is there return the minimum minDept of either
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        
        