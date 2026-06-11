# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = ListNode(-1001)
        while head:
            if head.next == seen:
                return True
            curr = head
            head = head.next
            curr.next = seen
        
        return False
