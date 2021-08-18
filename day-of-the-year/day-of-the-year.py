class Solution:
    def dayOfYear(self, date: str) -> int:
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])
        
        total_days = 0
        
        for i in range(1, month):
            if i == 2:
                if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
                    total_days += 29
                else:
                    total_days += 28
            elif i == 4 or i == 6 or i == 9 or i == 11:
                total_days += 30
            else:
                total_days += 31   
                
        total_days += day
                
        return total_days