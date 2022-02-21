class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.trie
        
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                cur.children[c] = TrieNode()
                cur = cur.children[c]
        cur.isWord = True

    def search(self, word: str, cur=None) -> bool:
        if not cur:
            cur = self.trie
        
        for i, c in enumerate(word):
            if c == '.':
                for opt in cur.children:
                    if self.search(word[i+1:], cur.children[opt]):
                        return True
                
                return False
            elif c not in cur.children:
                return False
            else:
                cur = cur.children[c]
        
        return cur.isWord


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)