# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l, r = head, head
        for i in range(n):
            r = r.next
        prev = None
        nextVal = None
        if r is None:
            return head.next
        while r:
            r = r.next
            if r is None:
                prev = l
                nextVal = l.next.next
                prev.next = nextVal
            l = l.next
        return head
        