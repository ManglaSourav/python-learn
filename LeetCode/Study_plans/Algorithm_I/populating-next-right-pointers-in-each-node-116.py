from typing import Optional
from collections import deque
"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

root1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

root1.left = n2
root1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

def print_tree(root):
    if root:
        print(root.val)
        print_tree(root.left)
        if root.next:
            print("next", root.next.val)
        print_tree(root.right)
        

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return root
        
        q = deque()
        q.append(root)
        
        while q:
            
            l = len(q)
            n1 = q.popleft()
            
            if n1:  
                q.append(n1.left)
                q.append(n1.right)     
                for i in range(1, l):
                    
                    n2 = q.popleft()
                    q.append(n2.left)
                    q.append(n2.right)     
                
                    n1.next = n2
                    n1 = n2
            
        return root
                
        
         

print_tree(Solution().connect(root1))