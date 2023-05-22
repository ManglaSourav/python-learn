

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
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        i = 1
        temp = head
        curr1 = head
        while i != k and curr1:
            curr1 = curr1.next
            i+=1
        
        curr2 = curr1
        while curr2 and curr2.next:
            curr2 = curr2.next
            head = head.next
        head.val, curr1.val = curr1.val, head.val
        
        return temp

        
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
printing_ll(Solution().swapNodes(n1, 2))


# head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]