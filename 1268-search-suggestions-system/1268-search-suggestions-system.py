class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                cur.children[c] = TrieNode()
                cur = cur.children[c]
        cur.isWord = True
        
    def getWordsWithPrefix(self, prefix):
        cur = self.root
        
        for c in prefix:
            if c not in cur.children:
                return []
            else:
                cur = cur.children[c]
        
        res = []
        self.dfs(cur, res, prefix)
        return res
    
    def dfs(self, cur, res, word):
        if len(res) == 3:
            return
        if cur.isWord:
            res.append(word)
        
        for c in sorted(cur.children):
            self.dfs(cur.children[c], res, word + c)
        
        

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        
        for word in products:
            trie.insert(word)
        
        sol = []
        for i in range(1, len(searchWord)+1):
            sol.append(trie.getWordsWithPrefix(searchWord[:i]))
        return sol
        