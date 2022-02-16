class MagicDictionary:

    def __init__(self):
        self.word = defaultdict(set)

    def buildDict(self, dictionary: List[str]) -> None:
        for w in dictionary:
            for i in range(len(w)):
                self.word[w].add(w[:i] + "*" + w[i+1:])

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            for w in self.word.keys():
                if searchWord[:i] + "*" + searchWord[i+1:] in self.word[w] and searchWord != w:
                    return True
        
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)