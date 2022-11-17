
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
# n6 = TreeNode(15)
# n7 = TreeNode(7)
root.left = n2
root.right = n3
n2.left = n4
n2.right = n5
# n3.left = n6
# n3.right = n7


class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            if not root:
                return -1

            left = dfs(root.left)
            right = dfs(root.right)
            nonlocal res
            #  2 is because we have 2 edge (1 for left and 1 for right)
            # calculating diameter of current node
            res = max(res, 2 + left + right)

            return 1 + max(left, right)  # returing height of the subtree

        dfs(root)
        return res


tree = Solution()
print(tree.diameterOfBinaryTree(root))
