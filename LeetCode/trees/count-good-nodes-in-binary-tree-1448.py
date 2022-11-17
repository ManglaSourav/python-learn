from typing import Optional, List
from collections import deque


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
n2 = TreeNode(3)
# n3 = TreeNode(4)
n4 = TreeNode(4)
n5 = TreeNode(2)
# n6 = TreeNode(5)
# n7 = TreeNode(9)
# [4, 2, 7, 1, 3, 6, 9]
root.left = n2
# root.right = n3
n2.left = n4
n2.right = n5
# n3.right = n6
# n3.right = n7


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        count = 1

        def dfs(root, curr_max):
            if not root:
                return
            nonlocal count
            curr_max_left = curr_max_right = curr_max
            if root.left and curr_max <= root.left.val:
                count += 1
                curr_max_left = max(curr_max, root.left.val)
            dfs(root.left, curr_max_left)

            if root.right and curr_max <= root.right.val:
                count += 1
                curr_max_right = max(curr_max, root.right.val)
            dfs(root.right, curr_max_right)

        dfs(root, root.val)

        return count


tree = Solution()
print(tree.goodNodes(root))
