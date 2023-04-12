from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head3 = ListNode(0)  #dummy node
        temp = head3
        while list1 and list2:
            
            if list1.val >= list2.val:
                temp.next = ListNode(list2.val)
                list2 = list2.next
            else:
                 temp.next = ListNode(list1.val)
                 list1 = list1.next
            temp = temp.next
        
        temp.next = list1 or list2
        
        
        return head3.next
head1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(4)

head1.next = n2
n2.next = n3

head2 = ListNode(1)
n22 = ListNode(3)
n33 = ListNode(4)

head2.next = n22
n22.next = n33
    

def printing_ll(head):
    curr = head
    while curr:
        print(curr.val, end="->")
        curr = curr.next



def mergeTwoLists2(l1, l2):
    if not l1 or not l2:
        
        return l1 or l2
    if l1.val < l2.val:
        l1.next = mergeTwoLists2(l1.next, l2)
        printing_ll(l1)
    
        return l1
    else:
        l2.next = mergeTwoLists2(l1, l2.next)
        return l2
    
printing_ll(mergeTwoLists2(head1, head2))
# list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]



