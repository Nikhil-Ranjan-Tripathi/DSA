# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def solve(a):
            if not a:
                return

            a.left, a.right = a.right, a.left

            solve(a.left)
            solve(a.right)

        solve(root)

        return root
        


            