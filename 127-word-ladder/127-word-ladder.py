class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        seen = set()
        
        q = deque([(beginWord, 0)])
        ans = float('inf')
        
        matches = defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                matches[word[:i] + "*" + word[i+1:]].append(word)
        
        while q:
            beginWord, j = q.popleft()
            
            if beginWord == endWord:
                return j + 1
            
            seen.add(beginWord)
            
            for i in range(len(beginWord)):
                for w in matches[beginWord[:i] + "*" + beginWord[i+1:]]:
                    if w not in seen:
                        q.append((w, j+1))
        
        return 0