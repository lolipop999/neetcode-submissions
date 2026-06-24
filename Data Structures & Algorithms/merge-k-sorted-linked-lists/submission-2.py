# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        dummy = ListNode(0)
        curr = dummy
        for i in range(len(lists)):
            heapq.heappush(values, (lists[i].val, i, lists[i]))
        while values:
            val, k, node = heapq.heappop(values)
            curr.next = node
            curr = curr.next
            if lists[k].next:
                lists[k] = lists[k].next
                heapq.heappush(values, (lists[k].val, k, lists[k]))

        return dummy.next
        


