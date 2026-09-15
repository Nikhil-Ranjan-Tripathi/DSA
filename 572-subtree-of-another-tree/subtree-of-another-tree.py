class Solution:
    def isSubtree(self, root: Optional[TreeNode],
                  subRoot: Optional[TreeNode]) -> bool:

        def same(a, b):

            if not a and not b:
                return True

            if not a or not b:
                return False

            if a.val != b.val:
                return False

            return same(a.left, b.left) and same(a.right, b.right)

        def search(node):

            if not node:
                return False

            if node.val == subRoot.val:
                if same(node, subRoot):
                    return True

            return search(node.left) or search(node.right)

        return search(root)


"""
class Solution:
    def isSubtree(self, root: Optional[TreeNode],
                  subRoot: Optional[TreeNode]) -> bool:

        def serialize(node):
            if not node:
                return ",#"

            return ("," + str(node.val) +
                    serialize(node.left) +
                    serialize(node.right))

        root_str = serialize(root)
        sub_str = serialize(subRoot)

        return sub_str in root_str
"""
