class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)
        stsum, ans = 0, 0
        for dish in satisfaction:
            stsum += dish
            if stsum < 0:
                break
            ans += stsum
        return ans