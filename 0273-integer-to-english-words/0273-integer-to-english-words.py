class Solution:
    def numberToWords(self, num: int) -> str:
        p = ["Hundred", "Thousand", "Million", "Billion"]
        t = ["Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        o = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        d = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        
        if not num: return "Zero"
        num = str(num)[::-1]
        ans = deque()
        
        for i in range(0, len(num), 3):
            x = int(num[i+2]) if i+2 < len(num) else 0
            y = int(num[i+1]) if i+1 < len(num) else 0
            z = int(num[i]) if i < len(num) else 0
            section = []
            
            if x > 0: 
                section.append(o[x-1])
                section.append(p[0])
            
            if y == 1:
                section.append(d[z])
            elif y > 0:
                section.append(t[y-1])
            
            if y != 1 and z > 0:
                section.append(o[z-1])
            
            if i > 0 and any([x,y,z]):
                section.append(p[i//3])
            
            if section:
                ans.appendleft(' '.join(section))
            
        return ' '.join(ans).strip()