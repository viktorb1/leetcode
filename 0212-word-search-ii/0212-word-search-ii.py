class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.count = 1
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            else:
                cur.children[c].count += 1
            cur = cur.children[c]
        cur.isWord = True
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for w in words:
            self.insert(w)
        
        sol = set()
        cur = self.root
        
        def dfs(i, j, cur, word):
            if cur[-1].isWord:
                for l in cur: l.count -= 1
                sol.add(word)
                cur[-1].isWord = False
            
            save = board[i][j]
            board[i][j] = "#"
            
            for x, y in ((i+1, j), (i, j+1), (i-1, j), (i, j-1)):
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] in cur[-1].children and cur[-1].count > 0:
                    dfs(x, y, cur + [cur[-1].children[board[x][y]]], word + board[x][y])
        
            board[i][j] = save
        
        for i in range(len(board)):
            for j in range((len(board[0]))):
                if board[i][j] in cur.children:
                    dfs(i, j, [cur.children[board[i][j]]], board[i][j])
        
        return sol