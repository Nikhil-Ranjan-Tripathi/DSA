# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        s = 0
        def solve(root, maxi):
            nonlocal s
            if not root:
                return

            if root.val>=maxi:
                s+=1
                maxi = root.val
            
            solve(root.left, maxi)
            solve(root.right, maxi)

        solve(root, -1*float('inf'))
        return s