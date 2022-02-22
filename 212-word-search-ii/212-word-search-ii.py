class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
                
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        output = set()
        cur = self.root
        
        for word in words:
            self.insert(word)
        
        def dfs(i, j, cur, word):
            if cur.isWord:
                output.add(word)
            
            save = board[i][j]
            board[i][j] = '#'
            
            for x, y in ((i+1,j), (i,j+1), (i-1, j), (i, j-1)):
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] in cur.children:
                    dfs(x, y, cur.children[board[x][y]], word + board[x][y])
                    
            board[i][j] = save
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in cur.children:
                    dfs(i, j, cur.children[board[i][j]], board[i][j])
                
                if len(output) == len(words):
                    return output
        
        return output