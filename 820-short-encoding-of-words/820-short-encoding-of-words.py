class Solution:
    def dfs(self, tree):
        if tree.children == {}:
            return tree.length+1
        
        total = 0
        for _, node in tree.children.items():
            total += self.dfs(node)
        
        return total
        
    
    def minimumLengthEncoding(self, words: List[str]) -> int:
        tree = Trie()
        
        for word in words:
            tree.insert(word[::-1])
        
        return self.dfs(tree.tree)
        

        

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.length = 0
    

class Trie:
    def __init__(self):
        self.tree = TrieNode()
        
    def insert(self, word):
        node = self.tree
        
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            
            node = node.children[c]
        
        node.isEnd = True
        print(len(word))
        node.length = len(word)