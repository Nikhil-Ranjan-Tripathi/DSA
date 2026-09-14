# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        c = []
        b = []

        def solve(root, a):
            if not root:
                a.append('null')
                return 
            
            a.append(root.val)
            solve(root.left, a)
            solve(root.right, a)

        solve(p,c)
        solve(q,b)

        return True if c==b else False

