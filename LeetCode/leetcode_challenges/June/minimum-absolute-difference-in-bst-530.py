
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        inorderNodes = []
        
        def inOrder(node):
            if node:
                inOrder(node.left)
                inorderNodes.append(node.val)
                inOrder(node.right)
                
        
        inOrder(root)
        minDifference = 1e9
        for i in range(1, len(inorderNodes)):
            minDifference = min(minDifference, inorderNodes[i] - inorderNodes[i-1])
        return minDifference
    

n = TreeNode(4)
n1 = TreeNode(2)
n2 = TreeNode(6)
n3 = TreeNode(1)
n4 = TreeNode(3)
# n5 = TreeNode(1)
# n6 = TreeNode(1)

n.left = n1
n.right = n2

n1.left = n3
n1.right = n4

# n3.right = n5

# n4.right = n6

def print_tree(root):
    if root:
        print(root.val)
        print_tree(root.left)
        print_tree(root.right)

print(Solution().getMinimumDifference(n))