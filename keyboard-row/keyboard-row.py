class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        top = set(list("qwertyuiop"))
        middle = set(list("asdfghjkl"))
        bottom = set(list("zxcvbnm"))
        sol = []

        for w in words:
            curw = set(list(w.lower()))
            if curw.issubset(top):
                sol.append(w)
            elif curw.issubset(middle):
                sol.append(w)
            elif curw.issubset(bottom):
                sol.append(w)
            
        return sol
            
                