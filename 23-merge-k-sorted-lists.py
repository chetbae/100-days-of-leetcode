# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()
        current = dummy

        for k, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, k))
                node = node.next
        
        while heap:
            val, k = heapq.heappop(heap)
            current.next = ListNode(val=val)
            current = current.next

            node = lists[k]
            if node.next:
                heapq.heappush(heap, (node.next.val, k))
                lists[k] = node.next
        
        return dummy.next
