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

root2 = TreeNode(1)
n5 = TreeNode(2)
n6 = TreeNode(3)

root.left = n2
root.right = n3

root2.left = n5
root2.right = n6


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))


# print_tree(root)
# print_tree(root2)
tree = Solution()
print(tree.isSameTree(root, root2))
