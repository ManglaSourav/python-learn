from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_tree(root):
    if not root:
        return
    print(root.val)
    if root.left:
        print_tree(root.left)
    if root.right:
        print_tree(root.right)
    return


root = TreeNode(6)
n2 = TreeNode(2)
n3 = TreeNode(8)
n4 = TreeNode(0)
n5 = TreeNode(4)
n6 = TreeNode(7)
n7 = TreeNode(9)
n8 = TreeNode(3)
n9 = TreeNode(5)

root.left = n2
root.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n5.left = n8
n5.right = n9


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        curr = root

        while curr:
            if (p.val < curr.val and q.val < curr.val):
                curr = curr.left
            elif (p.val > curr.val and q.val > curr.val):
                curr = curr.right
            else: # splitting the nodes here 
                return curr
        return


# print_tree(root)
tree = Solution()
print_tree(tree.lowestCommonAncestor(root, n2, n3))
