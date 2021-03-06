# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
                
#         counts = {}
        
#         for i in t:
#             if i not in counts:
#                 counts[i] = 1
#             else:
#                 counts[i] += 1
        
#         for i in s:
#             counts[i] -= 1
        
#         for i in counts:
#             if counts[i] == 1:
#                 return i
         
    
# Cleaner solution
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
    
        sum = 0

        for i in t:
            sum += ord(i)

        for i in s:
            sum -= ord(i)
        
        return chr(sum)
