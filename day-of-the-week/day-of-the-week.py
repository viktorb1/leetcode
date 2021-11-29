class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        opt = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        a = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
        
        if month < 3:
            year -= 1
        
        dow = (year + year//4 - year//100 + year//400 + a[month-1] + day) % 7
        return opt[dow]

        