
from typing import Optional, List


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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):  # Cutting the length of lists by half everytime
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                merged_lists.append(self.merge_lists(l1, l2))

            lists = merged_lists

        return lists[0]

    def merge_lists(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:

            if l1.val > l2. val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next

            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next


head1 = ListNode(1)
n2 = ListNode(4)
n3 = ListNode(5)

head1.next = n2
n2.next = n3

head2 = ListNode(1)
n22 = ListNode(3)
n33 = ListNode(4)

head2.next = n22
n22.next = n33

head3 = ListNode(2)
n222 = ListNode(6)
head3.next = n222

# [1,4,5],[1,3,4],[2,6]
r_list = Solution()
printing_ll(r_list.mergeKLists([head1, head2, head3]))
