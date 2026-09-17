# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0

        queue = deque([(root, 0)])
        result = 0

        while queue:
            size = len(queue)

            first = queue[0][1]
            last = queue[-1][1]

            result = max(result, last - first + 1)

            for i in range(size):
                node, index = queue.popleft()

                if node.left:
                    queue.append((node.left, 2 * index + 1))

                if node.right:
                    queue.append((node.right, 2 * index + 2))

        return result