

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def getDecimalValue(self, head: ListNode) -> int:
        
        res = []
        while head:
            res.append(head.val)
            head = head.next 
        ans = 0
        for i in range(len(res)):
            ans += res[len(res)- 1 - i] * 2**i
        return ans
    
    
n1 = ListNode(1)
n2 = ListNode(0)
n3 = ListNode(1)

n1.next = n2
n2.next = n3
Solution().getDecimalValue(n1)

