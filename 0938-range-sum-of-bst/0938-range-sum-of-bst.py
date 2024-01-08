# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
            res = 0
            if root.left and root.val > low:
                res += self.rangeSumBST(root.left, low, high)
            if root.right and root.val < high:
                res += self.rangeSumBST(root.right, low, high)
            if root.val >= low and root.val <= high:
                res += root.val
            return res