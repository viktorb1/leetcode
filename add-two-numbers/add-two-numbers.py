# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode(0)
        curr = head
        
        while l1 or l2 or carry: 
            total = 0
            
            if l1:
                total += l1.val
            if l2:
                total += l2.val
            if carry == 1:
                total += carry
                
            curr.next = ListNode(total % 10)
            carry = total // 10
            curr = curr.next
            
            if l1:
                l1 = l1.next
                
            if l2:
                l2 = l2.next
        
        return head.next