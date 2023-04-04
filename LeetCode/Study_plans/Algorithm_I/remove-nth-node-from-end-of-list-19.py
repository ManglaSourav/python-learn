from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        
        
        
        while n > 0 and fast:
            fast = fast.next
            n -= 1
        
        # Now we maintain distance of n between both pointers
        while fast:
            slow = slow.next
            fast = fast.next
        
        # slow pointer is exactly at the position where we want it
        slow.next = slow.next.next
        
        
        return dummy.next
    
def print_list(node):
    
    while node:
        print(node.val)
        node = node.next
        
    
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

print(Solution().removeNthFromEnd(node1, 2))