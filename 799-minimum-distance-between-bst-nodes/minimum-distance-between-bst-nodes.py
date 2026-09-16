# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDiffInBST(self, root: TreeNode | None) -> int:
        mini = []
        m = float('inf')
        def solve(root, ):
            if not root:
                return

            solve(root.left)
            mini.append(root.val)
            solve(root.right)
        solve(root)

        for i in range(1, len(mini)):
            m = min(m, mini[i]-mini[i-1])

        return m


            