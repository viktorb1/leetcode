# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        currA = headA
        currB = headB
        
        diff = self.getLength(headA) - self.getLength(headB)
        
        if diff > 0 or diff < 0:
            for i in range(abs(diff)):
                if currA == currB:
                    return currA
                else:
                    if diff > 0:
                        currA = currA.next
                    else:
                        currB = currB.next
        
        while currA and currB:
            if currA == currB:
                return currA
            else:
                currA = currA.next
                currB = currB.next
        
        return None
    
    def getLength(self, head: ListNode) -> int:
        length = 0
        
        while head:
            length += 1
            head = head.next
            
        return length
        