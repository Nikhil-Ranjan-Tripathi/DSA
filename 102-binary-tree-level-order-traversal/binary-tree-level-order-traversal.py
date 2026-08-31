# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que = deque([root])
        ans = [[root.val]]
        b = []
        while que:
            for i in range(len(que)):
                a = que.popleft()
                if a.left:
                    b.append(a.left)
                if a.right:
                    b.append(a.right)
            pus = []
            for i in range(len(b)):
                pus.append(b[i].val)
                que.append(b[i])
            if pus:
                ans.append(pus)
                
            b = []
        return ans

