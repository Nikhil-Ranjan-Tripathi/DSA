# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        result = []
        if root:
            result.append([root.val])
        que = deque()
        que.append(root)

        while que:
            a = []
            b = []
            for i in range(len(que)):
                c = que.popleft()
                if c and c.left:
                    a.append(c.left)
                    b.append(c.left.val)
                if c and c.right:
                    a.append(c.right)
                    b.append(c.right.val)

            result.append(b)
            for i in a:
                que.append(i)
            
        result.pop()

        return result[::-1]