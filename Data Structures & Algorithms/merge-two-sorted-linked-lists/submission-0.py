# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node_1 = list1
        node_2 = list2
        if node_1 == None:
            return list2
        elif node_2 == None:
            return list1
        else:
            if node_1.val <= node_2.val:
                head = ListNode(node_1.val)
                node_1 = node_1.next
            else:
                head = ListNode(node_2.val)
                node_2 = node_2.next
        tail = head
        while node_1 != None or node_2 != None:
            if node_1 == None:
                tail.next = ListNode(node_2.val)
                node_2 = node_2.next
            elif node_2 == None:
                tail.next = ListNode(node_1.val)
                node_1 = node_1.next
            elif node_1.val <= node_2.val:
                tail.next = ListNode(node_1.val)
                node_1 = node_1.next
            else: # node_2.val < node_1.val
                tail.next = ListNode(node_2.val)
                node_2 = node_2.next
            tail = tail.next

        return head
