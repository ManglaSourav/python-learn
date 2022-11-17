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


root = TreeNode(3)
n2 = TreeNode(90)
n3 = TreeNode(20)
# n4 = TreeNode(1)
# n5 = TreeNode(3)
n6 = TreeNode(15)
n7 = TreeNode(7)
# [4, 2, 7, 1, 3, 6, 9]
root.left = n2
root.right = n3
# n2.left = n4
# n2.right = n5
n3.left = n6
n3.right = n7


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        if root:
            q.append(root)

        while q:
            val = []
            for i in range(len(q)):
                node = q.popleft()  
                val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(val)
            
        return res


    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #     res = []
    #     q = deque()
    #     if root:
    #             q.append(root)

    #     while q:
    #         val = []
    #         for i in range(len(q)):
    #             node = q.popleft()
    #             val.append(node.val)
    #             if node.left:
    #                 q.append(node.left)
    #             if node.right:
    #                 q.append(node.right)
    #         res.append(val)
    #     return res

tree = Solution()
print(tree.levelOrder(root))
