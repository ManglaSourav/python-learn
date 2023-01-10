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
    def hasCycle_usingset(self, head: Optional[ListNode]) -> bool:

        my_set = set()
        my_set.add(head)

        while head and head.next:
            head = head.next
            if not my_set.isdisjoint({head}):
                return True
            my_set.add(head)

        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


head = ListNode(3)
# n2 = ListNode(2)
# n3 = ListNode(0)
# n4 = ListNode(-4)

# head.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n2


r_list = Solution()
print(r_list.hasCycle(head))
