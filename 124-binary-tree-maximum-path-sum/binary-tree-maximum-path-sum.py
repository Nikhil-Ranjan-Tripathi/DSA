# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        m = float('-inf')

        def solve(node):
            nonlocal m

            if not node:
                return 0
            
            l = max(solve(node.left), 0)
            r = max(solve(node.right), 0)

            curr = node.val+l+r

            m = max(m, curr)

            return node.val+max(l, r)


        solve(root)

        return m