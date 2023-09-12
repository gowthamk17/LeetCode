# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_queue = deque()
        levels = []
        if root:
            level_queue.append(root)
        while level_queue:
            level = []
            qLen = len(level_queue)
            for i in range(qLen):
                node = level_queue.popleft()                
                if node is not None:
                    level.append(node.val)
                    level_queue.append(node.left)
                    level_queue.append(node.right)
            if level:
                levels.append(level)
        return levels