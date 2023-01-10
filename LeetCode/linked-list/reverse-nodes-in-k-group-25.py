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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy  # to store the prev link

        while True:
            kth = self.get_kth_node(group_prev, k)

            if not kth:  # last group that does not have k element
                break
            group_next = kth.next

            # reversing the group
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp

        return dummy.next

    def get_kth_node(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


head = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5


r_list = Solution()
printing_ll(r_list.reverseKGroup(head, 2))
