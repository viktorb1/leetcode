class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        
        d = defaultdict(list)
        add = True
        row = 1
        
        for c in s:
            d[row].append(c)
            
            if add:
                row += 1
            else:
                row -= 1
            
            if row == numRows:
                add = False
            elif row == 1:
                add = True
               
        ans = ""
        for i in range(1, numRows+1):
            ans += "".join(d[i])
        
        return ans