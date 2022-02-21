class WordDictionary:
    class PrefixTree():
        def __init__(self):
            self.next = dict()
            self.isWord = False
    
    def __init__(self):
        self.tree = self.PrefixTree()

    def addWord(self, word: str) -> None:
        cur = self.tree
    
        for c in word:
            if c not in cur.next:
                cur.next[c] = self.PrefixTree()

            cur = cur.next[c]
            
        cur.isWord = True
                
    def search(self, word: str, d = None) -> bool:
        cur = self.tree if d == None else d
        
        for i, c in enumerate(word):
            if c == '.':
                for key, tre in cur.next.items():
                    if self.search(word[i+1:], tre):
                        return True
                
                return False
            elif c not in cur.next:
                return False
            else:
                cur = cur.next[c]
        
        return cur.isWord


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)