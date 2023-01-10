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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        first, second = l1, l2
        carry = 0
        dummy = ListNode()
        my_list = dummy
        while first or second:
            val1 = 0
            val2 = 0
            if first:
                val1 = first.val
                first = first.next
            if second:
                val2 = second.val
                second = second.next
            # print(val2, "-", val1, "-", carry)
            total = val2 + val1 + carry
            carry = total//10
            # if total > 9:
            #     carry = int(str(total)[:-1])

            my_list.next = ListNode(total % 10)
            my_list = my_list.next

        if carry > 0:
            my_list.next = ListNode(carry)

        return dummy.next


head1 = ListNode(9)
n2 = ListNode(9)
n3 = ListNode(9)
n33 = ListNode(9)
n34 = ListNode(9)
n35 = ListNode(9)
n36 = ListNode(9)

head1.next = n2
n2.next = n3
n3.next = n33
n33.next = n34
n34.next = n35
n35.next = n36


head2 = ListNode(9)
n4 = ListNode(9)
n5 = ListNode(9)
n6 = ListNode(9)

head2.next = n4
n4.next = n5
n5.next = n6


# [9, 9, 9, 9, 9, 9, 9]
# [9, 9, 9, 9]
# [8, 9, 9, 9, 0, 0, 0, 1]
r_list = Solution()
printing_ll(r_list.addTwoNumbers(head1, head2))
