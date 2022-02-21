class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.trie
        
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                cur.children[c] = TrieNode()
                cur = cur.children[c]
        
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.trie
        
        for c in word:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c]
        
        return cur.isWord
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        
        for c in prefix:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)