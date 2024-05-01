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


# one-pass solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = node = head
        prev = None

        # send end to explore, then when n steps in, increment node and prev to find target
        # ()->(prev)->(node)->...n-2 steps...->(end)->...

        # run for n times
        for i in range(n):
            end = end.next
        
        # increment all pointers until end
        while end:
            prev, node, end = node, node.next, end.next

        # if target is the head node, return the next node i.e. cutting head out
        if node == head:
            return head.next

        # otherwise cut out target node and return
        prev.next = node.next
        return head
