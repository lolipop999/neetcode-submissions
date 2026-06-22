# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the midpoint using fast-slow
        fast, slow = head.next, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        
        # reverse the second half
        prev = None
        while second:
            nextVal = second.next
            second.next = prev
            prev = second
            second = nextVal
        second = prev

        # combine the list
        while second:
            tmp1 = head.next
            tmp2 = second.next
            head.next = second
            second.next = tmp1
            head, second = tmp1, tmp2