# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        s1 = []
        s2 = []

        def solve(root, s):
            if not root:
                return
            if not root.left and not root.right:
                s.append(root.val)
                return
            
            solve(root.left, s)
            solve(root.right, s)

        solve(root1, s1)
        solve(root2, s2)

        return s2==s1