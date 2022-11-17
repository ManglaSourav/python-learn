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


root = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(5)
n5 = TreeNode(4)
# n6 = TreeNode(6)
# n7 = TreeNode(9)
# [4, 2, 7, 1, 3, 6, 9]
root.left = n2
root.right = n3
n2.right = n4
n3.right = n5
# n3.left = n6
# n3.right = n7


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        q = deque()
        if root:
            q.append(root)
        while q:
            q_len = len(q)
            right_node = None
            for i in range(q_len):
                node = q.popleft()
                if not right_node:
                    right_node = node
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

            result.append(right_node.val)

        return result


# print_tree(root)
tree = Solution()
print(tree.rightSideView(root))
