class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        sol = []
        row = ""
        for w1, w2 in zip(words, words[1:] + [""]):
            row += w1 + (" " if len(row) < maxWidth else "")
            
            if len(row) + len(w2) > maxWidth or w2 == "":
                sol.append(row)
                row = ""
        
        for i in range(len(sol)):
            char_count = len(sol[i].strip())
            sol[i] = sol[i].strip().split()
            char_count -= (len(sol[i]) - 1)
            rem = maxWidth - char_count
            
            if i == len(sol) - 1:
                sol[i] = ' '.join(sol[i]) + ' '*(rem-len(sol[i])+1)
                break
            
            j = 0
            while rem:
                j %= len(sol[i])-1 if len(sol[i]) > 1 else len(sol[i])
                sol[i][j] = sol[i][j] + " "
                rem -= 1
                j += 1
            
            sol[i] = ''.join(sol[i])
        
        return sol