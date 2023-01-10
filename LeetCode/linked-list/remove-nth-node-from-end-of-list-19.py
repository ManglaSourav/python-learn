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
    def removeNthFromEnd_reverse(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # wrong answer
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        count = 1
        node = prev
        node_prev = None
        while count != n:
            node_prev = node
            node = node.next
            count += 1

        if n > 1:
            node_prev.next = node_prev.next.next

        head, curr = None, prev
        while curr:
            nxt = curr.next
            curr.next = head
            head = curr
            curr = nxt

        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        left = dummy
        right = head
        i = 1
        while right and i <= n:
            right = right.next
            i += 1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next
        return dummy.next


head = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(3)
# n4 = ListNode(4)
# n5 = ListNode(5)

# head.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5


r_list = Solution()
# r_list.removeNthFromEnd(head, 1)
printing_ll(r_list.removeNthFromEnd(head, 1))
