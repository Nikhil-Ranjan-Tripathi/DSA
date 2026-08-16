class Solution:
    def diameter(self, root):
        self.dia = 0

        def height(node):
            if node is None:
                return 0

            left = height(node.left)
            right = height(node.right)

            self.dia = max(self.dia, left + right)

            return 1 + max(left, right)

        height(root)

        return self.dia
        