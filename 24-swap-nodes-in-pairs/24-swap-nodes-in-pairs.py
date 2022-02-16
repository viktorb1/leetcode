class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        one = head
        two = head.next if head else None
        save = two
        
        while one and two:
            save1 = two.next # save 3
            save2 = two.next.next if two.next else None # save 4
            
            one.next = two.next.next if two.next and two.next.next else two.next # make 1 point to 4
            two.next = one # make 2 point to 1
            
            one = save1 # update 1 to 3
            two = save2 # update 2 to 4
            
        return save if save else head