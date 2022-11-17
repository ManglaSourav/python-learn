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
n2 = TreeNode(4)
n3 = TreeNode(5)
n22 = TreeNode(1)
n33 = TreeNode(2)

root2 = TreeNode(4)
n5 = TreeNode(1)
n6 = TreeNode(2)

root.left = n2
root.right = n3
n2.left = n22
n2.right = n33

root2.left = n5
# root2.right = n6


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def isSameTree(self, p, q):
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))


# print_tree(root)
# print_tree(root2)
tree = Solution()
print(tree.isSubtree(root, root2))
