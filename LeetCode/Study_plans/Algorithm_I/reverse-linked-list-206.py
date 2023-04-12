from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:  
        left = None
        right = head
        
        while right:
            temp = right.next
            right.next = left
            left = right
            right = temp
        return left
    

def printing_ll(head):
    curr = head
    while curr:
        print(curr.val, end="->")
        curr = curr.next

head1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

head1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

printing_ll(Solution().reverseList(head1))