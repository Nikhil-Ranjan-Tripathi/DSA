# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}

        def find_parent(node, par):
            if not node:
                return

            parent[node] = par

            find_parent(node.left, node)
            find_parent(node.right, node)

        find_parent(root, None)
        que = deque([target])
        visited = {target}

        for _ in range(k):
            for _ in range(len(que)):
                node = que.popleft()
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    que.append(node.left)

                if node.right and node.right not in visited:
                    visited.add(node.right)
                    que.append(node.right)

                if parent[node] and parent[node] not in visited:
                    visited.add(parent[node])
                    que.append(parent[node])
                

        return [node.val for node in que]
        

            
                