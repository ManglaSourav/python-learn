from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def printing_ll(head):
    curr = head
    while curr:
        print(curr.val, end="->")
        curr = curr.next
  
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(next=head)
        # 1->2->3->4->5
        prev = temp
        while prev.next and prev.next.next:

            a = prev.next
            b = prev.next.next
            c = prev.next.next.next
            prev.next = b
            prev.next.next = a
            prev.next.next.next = c
            prev = prev.next.next
            
        return temp.next
    
    
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

printing_ll(n1)
print()
printing_ll(Solution().swapPairs(n1))
