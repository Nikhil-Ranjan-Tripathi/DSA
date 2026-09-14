# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a = []

        def solve(root):
            if root is None:
                return

            solve(root.left)
            a.append(root.val)
            solve(root.right)

        solve(root)

        return a