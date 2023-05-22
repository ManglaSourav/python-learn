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
    print()
    
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow
        
        print("curr", curr.val)
        print("prev", prev)
        while curr:
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp
        
        res = 0
        while prev:
            res = max(res, prev.val+head.val)
            prev = prev.next
            head = head.next
        
        return res        
        
    


n1 = ListNode(1)
n2 = ListNode(2)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n4
n4.next = n5

printing_ll(n1)
print(Solution().pairSum(n1))