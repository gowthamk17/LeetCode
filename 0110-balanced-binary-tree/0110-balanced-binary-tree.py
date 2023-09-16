# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if self.height(root) == -1:
            return False
        return True
        
    def height(self, root) -> int:
        if root is None:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        if left == -1 or right == -1 or abs(left-right) > 1:
            return -1
        return max(left, right)+1
            