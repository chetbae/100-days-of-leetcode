# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        node = head

        # find length of list

        while node:
            node = node.next
            length += 1

        # get prev and next node of target
        node = head
        target = length-n

        if target == 0:
            return head.next
        
        for i in range(target-1):
            node = node.next
        
        prev = node
        
        prev.next = node.next.next if node.next else node.next

        return head