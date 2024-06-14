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

## divide and conquer approach

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists) // 2
        left, right = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(left, right)
    
    def merge(self, left, right):
        if not left:
            return right
        if not right: 
            return left
        
        if left.val <= right.val:
            left.next = self.merge(left.next, right)
            return left
        else:
            right.next = self.merge(left, right.next)
            return right