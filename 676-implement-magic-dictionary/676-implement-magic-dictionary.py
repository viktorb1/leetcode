class MagicDictionary:

    def __init__(self):
        self.word = defaultdict(set)

    def buildDict(self, dictionary: List[str]) -> None:
        for w in dictionary:
            self.word[len(w)].add(w)

    def search(self, searchWord: str) -> bool:
        
        for w in self.word[len(searchWord)]:            
            if sum(a != b for a, b in zip(w, searchWord)) == 1:
                return True
        
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)