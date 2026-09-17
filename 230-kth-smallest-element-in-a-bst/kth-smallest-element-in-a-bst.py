# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        a = []

        def solve(root):
            nonlocal a
            if not root:
                return

            solve(root.left)
            a.append(root.val)
            solve(root.right)

        solve(root)

        return a[k-1]