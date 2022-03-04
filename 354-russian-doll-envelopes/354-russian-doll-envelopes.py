class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        print(envelopes)
        dp = []
        
        for _, height in envelopes:
            left = bisect_left(dp, height)
            print(left)
            if left == len(dp):
                dp.append(height)
            else:
                dp[left] = height
                
        return len(dp)
