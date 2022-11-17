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
n2 = TreeNode(3)
n3 = TreeNode(6)
n4 = TreeNode(2)
n5 = TreeNode(4)
n6 = TreeNode(1)
# n7 = TreeNode(9)
# [4, 2, 7, 1, 3, 6, 9]
root.left = n2
root.right = n3
n2.left = n4
n2.right = n5
n4.left = n6
# n3.right = n7


class Solution:
    def kthSmallest_in_order(self, root: Optional[TreeNode], k: int) -> int:

        arr = []

        def in_Order_travesal(root):
            if root:
                in_Order_travesal(root.left)
                arr.append(root.val)
                in_Order_travesal(root.right)

        in_Order_travesal(root)
        return arr[k-1]

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right


# print_tree(root)
tree = Solution()
print(tree.kthSmallest(root, 3))
