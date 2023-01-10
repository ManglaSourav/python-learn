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



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def reverseList_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList_recursive(head.next)

            head.next.next = head
        head.next = None
        return newHead


head = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5


# ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}
r_list = Solution()
# r_list.printing_ll(head)
printing_ll(r_list.reverseList_recursive(head))
