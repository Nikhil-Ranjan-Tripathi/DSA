# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.l = []

        def tra(node, k):
            if not node:
                return False
            
            if k-node.val in self.l:
                return True
            self.l.append(node.val)
            return tra(node.left, k) or tra(node.right, k)

        return tra(root, k)


