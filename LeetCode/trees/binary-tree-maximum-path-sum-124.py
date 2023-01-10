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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = root.val

        def dfs(root):

            if not root:
                return 0
            left_max = max(dfs(root.left), 0)
            right_max = max(dfs(root.right), 0)

            nonlocal result
            # with split
            result = max(result, root.val + left_max + right_max)

            # return result of without split
            return root.val + max(left_max, right_max)
        dfs(root)
        return result


tree = Solution()
print(tree.maxPathSum(root))
