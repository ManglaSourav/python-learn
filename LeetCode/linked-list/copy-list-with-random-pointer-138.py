

from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def printing_ll(head):
    curr = head
    while curr:
        print(curr.val, end="->")
        curr = curr.next


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {None: None}

        curr = head
        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            oldToNew[curr].next = oldToNew[curr.next]
            oldToNew[curr].random = oldToNew[curr.random]
            curr = curr.next

        return oldToNew[head]


head = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5


r_list = Solution()
printing_ll(r_list.copyRandomList(head))
