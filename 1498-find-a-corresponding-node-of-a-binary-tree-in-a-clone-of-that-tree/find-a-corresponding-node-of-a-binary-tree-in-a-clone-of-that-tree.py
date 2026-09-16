# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def solve(a, b):
            if not a:
                return
            if a==target:
                return b

            left = solve(a.left, b.left)
            if left:
                return left
            return solve(a.right, b.right)

        return solve(original, cloned)