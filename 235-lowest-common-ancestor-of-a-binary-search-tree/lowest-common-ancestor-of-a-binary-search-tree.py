# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(node):
            if not node:
                return
            
            if node.val > p.val and node.val > q.val:    
                return find(node.left)
            elif node.val < p.val and node.val < q.val:
                return find(node.right)
            else:
                return node


        return find(root)
