# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

class Codec:

    def serialize(self, root):
        
        ans = []

        def solve(node):
            if not node:
                ans.append("#")
                return

            ans.append(str(node.val))

            solve(node.left)
            solve(node.right)

        solve(root)

        return ",".join(ans)


    def deserialize(self, data):

        values = data.split(",")
        i = 0

        def solve():
            nonlocal i

            if values[i] == "#":
                i += 1
                return None

            node = TreeNode(int(values[i]))
            i += 1

            node.left = solve()
            node.right = solve()

            return node

        return solve()