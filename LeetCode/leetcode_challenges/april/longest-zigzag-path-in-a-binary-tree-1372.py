from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
# [1,1,1,null,1,null,null,1,1,null,1]
n = TreeNode(1)
n1 = TreeNode(1)
n2 = TreeNode(1)
n3 = TreeNode(1)
n4 = TreeNode(1)
n5 = TreeNode(1)
n6 = TreeNode(1)

# n.left = n1
# n.right = n2

# n1.right = n3

# n3.left = n4
# n3.right = n5

# n4.right = n6

def print_tree(root):
    if root:
        print(root.val)
        print_tree(root.left)
        print_tree(root.right)
          
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, count, direction):
            nonlocal res
            res = max(res, count)
            if not node:
                return
            
            if direction == "L":
                if node.left:
                    count += 1
                dfs(node.left, count, "R")
                if node.right:
                    dfs(node.right, 1, "L")
            elif direction == "R":
                if node.right:
                    count += 1
                dfs(node.right, count, "L")
                if node.left:
                   dfs(node.left, 1, "R")
            
            return
            
            
        # dfs(root, 0, "L")
        dfs(root, 0, "R")
        return res
# print_tree(n)
print(Solution().longestZigZag(n))