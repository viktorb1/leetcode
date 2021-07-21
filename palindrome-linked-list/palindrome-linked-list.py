# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        curr = head
        nums = []
        
        while curr:
            nums.append(curr.val)
            curr = curr.next
        
        for i in range(len(nums)):
            if nums[i] != nums[len(nums)-i-1]:
                return False
            
        return True