# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        count = 0
        node_a, node_b = None, None

        cur = list1
        while cur and count < b + 2:
            count += 1
            if count == a:
                node_a = cur
            elif count == b+2:
                node_b = cur
            cur = cur.next
        
        first = list2
        last = list2
        while last and last.next:
            last = last.next
        
        node_a.next = first
        last.next = node_b
        return list1