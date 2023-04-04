from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
    
root1 = TreeNode(1)
n2 = TreeNode(3)
n3 = TreeNode(2)
n4 = TreeNode(5)

root2 = TreeNode(2)
n22 = TreeNode(1)
n23 = TreeNode(3)
n24 = TreeNode(4)
n25 = TreeNode(7)


root1.left = n2
root1.right = n3
n2.left = n4

root2.left = n22
root2.right = n23
n22.right = n24
n23.right = n25


def print_tree(root):
    if root:
        print(root.val)
        print_tree(root.left)
        print_tree(root.right)
    

# root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
        
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(r1, r2):
            
            if not r1:
                return r2
            if not r2:
                return r1
            
            node = TreeNode((r1.val or 0) + (r2.val or 0))

            node.left = dfs(r1.left, r2.left)
            node.right = dfs(r1.right, r2.right)
            
            return node
        
        return dfs(root1, root2)
        
        
        
    
print_tree(Solution().mergeTrees(root1, root2))