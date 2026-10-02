# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode | None) -> list[TreeNode | None]:
        seen = {}
        count = defaultdict(int)
        ans = []

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            key = (node.val, left, right)

            if key not in seen:
                seen[key] = len(seen)+1

            ids = seen[key]

            count[ids]+=1

            if count[ids]==2:
                ans.append(node)

            return ids

        dfs(root)

        return ans
