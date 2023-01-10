from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printing_ll(head):
    curr = head
    while curr:
        print(curr.val, end="->")
        curr = curr.next


head1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(4)
head1.next = n2
n2.next = n3

head2 = ListNode(1)
n4 = ListNode(3)
n5 = ListNode(4)
n6 = ListNode(6)
n7 = ListNode(7)
head2.next = n4
n4.next = n5
n5.next = n6
n6.next = n7


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode("dummy")
        new_head = dummy
        head1 = list1
        head2 = list2

        while head1 and head2:
            if head1.val < head2.val:
                new_head.next = head1
                head1 = head1.next
            else:
                new_head.next = head2
                head2 = head2.next
            new_head = new_head.next

        if head1:
            new_head.next = head1
        if head2:
            new_head.next = head2

        return dummy.next


l_list = Solution()
# printing_ll(head2)
printing_ll(l_list.mergeTwoLists(head1, head2))
