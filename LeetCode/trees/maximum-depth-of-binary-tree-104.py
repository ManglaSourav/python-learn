
from typing import Optional
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
n2 = TreeNode(9)
n3 = TreeNode(20)
# n4 = TreeNode(1)
# n5 = TreeNode(3)
n6 = TreeNode(15)
n7 = TreeNode(7)
root.left = n2
root.right = n3
# n2.left = n4
# n2.right = n5
n3.left = n6
n3.right = n7


class Solution:
    # all of them takes memory and time of O(n)

    # recursive dfs
    def maxDepth_using_dfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_dept = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_dept, right_depth)

    # BFS: counting the levels in the tree
    def maxDepth_bfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = deque([root])
        level = 0
        while q:

            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return level

    # DFS: iterative preorder DFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []  # node and depth

        stack.append([root, 1])
        d = 0
        while stack:

            node, depth = stack.pop()
            if node:
                if node.right:  # we want left on the top so we inserted right first
                    stack.append([node.right, depth + 1])
                if node.left:
                    stack.append([node.left, depth + 1])
                d = max(d, depth)

        return d


# print_tree(root)
tree = Solution()
print(tree.maxDepth(root))
