class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search_letter(w, i, j):
            if not w:
                return True
            if not isInBounds(i, j) or board[i][j] != w[0]:
                return False

            z = False
            board[i][j] = "#"
            
            for x, y in ((i-1, j), (i, j-1), (i, j+1), (i+1, j)):
                z |= search_letter(w[1:], x, y)
            
            board[i][j] = w[0]
            return z
            
        def isInBounds(i, j):
            return i >= 0 and i < len(board) and j >= 0 and j < len(board[0])
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if search_letter(word, i, j):
                        return True