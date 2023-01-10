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


head = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5


class Solution:

    # Linear time without using extra space
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next

        # finding second half of the list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None  # this will be the last node in reordered list

        # reversing second half of the list
        prev, curr = None, second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # merge the two half
        first, second = head, prev

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

        printing_ll(head)


r_list = Solution()
r_list.reorderList(head)
