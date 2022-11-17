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


root = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
# n4 = TreeNode(1)
# n5 = TreeNode(3)
n6 = TreeNode(15)
n7 = TreeNode(7)
# [4, 2, 7, 1, 3, 6, 9]
root.left = n2
root.right = n3
# n2.left = n4
# n4.right = n5
n3.left = n6
n3.right = n7


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):  # True/False: Subtree is balanced or not, int: height of the subtree

            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balance = (left[0] and right[0]) and abs(left[1] - right[1]) <= 1

            return [balance, 1+max(left[1], right[1])]

        return dfs(root)[0]


tree = Solution()
print(tree.isBalanced(root))
