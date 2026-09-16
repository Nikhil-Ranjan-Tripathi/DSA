# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        a = []
        def solve(root):
            if not root:
                return

            solve(root.left)
            a.append(root.val)
            solve(root.right)
        
        solve(root)
        s = 0
        for i in a:
            if low<=i<=high:
                s+=i

        return s

"""
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    
        def sum_value(node,curr):
            if not node:
                return 0
            if node.val < low:
                curr = sum_value(node.right,curr)
            elif node.val > high:
                curr = sum_value(node.left,curr)
            else:
                curr = node.val + sum_value(node.left,curr) + sum_value(node.right,curr)
                  
            return curr
        return sum_value(root,0)            
"""
