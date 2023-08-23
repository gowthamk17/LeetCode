# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key < root.val:
            if root.left:
                root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            if root.right:
                root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            min_val = root.right
            while min_val.left:
                min_val = min_val.left
            root.val = min_val.val
            root.right = self.deleteNode(root.right, root.val)
        return root
            
            