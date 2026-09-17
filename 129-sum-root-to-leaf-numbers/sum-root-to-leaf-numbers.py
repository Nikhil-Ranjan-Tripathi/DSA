# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        result = []

        def dfs(root, s):
            if not root:
                return

            s = s*10 + root.val

            if not root.left and not root.right:
                result.append(s)
                return

            dfs(root.left, s)
            dfs(root.right, s)

            s//=10

        dfs(root, 0)

        return sum(result)