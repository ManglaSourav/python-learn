from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_tree(root):
    print(root.val)
    if root.left:
        print_tree(root.left)
    if root.right:
        print_tree(root.right)
    return


root = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
# n6 = TreeNode(6)
# n7 = TreeNode(9)
# [4, 2, 7, 1, 3, 6, 9]
root.left = n2
root.right = n3
n3.left = n4
n3.right = n5
# n3.left = n6
# n3.right = n7


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        result = []

        def dfs(root):
            nonlocal result
            if not root:
                result.append("N")
                return
            result.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(',')
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()


# print_tree(root)
tree = Codec()
encoded_str = tree.serialize(root)
print(encoded_str)
print_tree(tree.deserialize(encoded_str))
