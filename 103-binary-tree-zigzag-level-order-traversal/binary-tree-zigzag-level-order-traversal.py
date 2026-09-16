# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        result = []
        que = deque()
        que.append(root)
        level = 0
        while que:
            c = []
            b = []
            for i in range(len(que)):
                a = que.popleft()
                c.append(a.val)

                if a.left:
                    b.append(a.left)
                    
                if a.right:
                    b.append(a.right)
                    
            
            if level%2==1:
                c.reverse()

            result.append(c)

            for i in range(len(b)):
                que.append(b[i])

            level+=1

        return result
            