class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        most = 0
        
        for user in accounts:
            most = max(sum(user), most)
            
        return most