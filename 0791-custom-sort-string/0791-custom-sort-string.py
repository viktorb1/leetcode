class Solution:
    def customSortString(self, order: str, s: str) -> str:
        chars = Counter(s)
        order_chars = set(order)
        ans = []
        
        
        for c in order:
            if c in chars:
                ans.append(c*chars[c])
        
        for c in chars:
            if c not in order_chars:
                ans.append(c*chars[c])
        
        return ''.join(ans)