# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        r = []

        def dfs(root):
            if not root:
                return
            
            r.append(root)
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        for i in range(len(r)-1):
            r[i].left = None
            r[i].right = r[i+1]

        return r
