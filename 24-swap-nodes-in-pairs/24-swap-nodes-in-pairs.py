class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        one = head
        two = head.next
        save_for_return = two
        
        while one and two:
            three = two.next # save 3
            four = three.next if three else None # save 4
            
            one.next = four if three and four else three # make 1 point to 4
            two.next = one # make 2 point to 1
            
            one = three # update 1 to 3
            two = four # update 2 to 4
            
        return save_for_return