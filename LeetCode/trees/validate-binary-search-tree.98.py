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


root = TreeNode(5)
n2 = TreeNode(1)
n3 = TreeNode(6)
n4 = TreeNode(3)
n5 = TreeNode(7)
# n6 = TreeNode(6)
# n7 = TreeNode(9)
# [4, 2, 7, 1, 3, 6, 9]
root.left = n2
root.right = n3
n3.left = n4
n3.right = n5
# n3.left = n6
# n3.right = n7


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def is_valid(node, left, right):

            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False

            return is_valid(node.left, left, node.val) and is_valid(node.right, node.val, right)
        return is_valid(root, float("-inf"), float("inf"))


tree = Solution()
print(tree.isValidBST(root))
