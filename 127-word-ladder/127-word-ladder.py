class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        seen = set()
        wordList = set(wordList)

        q = deque([(beginWord, 0)])
        ans = float('inf')
        
        
        while q:
            beginWord, j = q.popleft()
            
            if beginWord == endWord:
                return j + 1
            
            seen.add(beginWord)
            
            for i in range(len(beginWord)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    w = beginWord[:i] + c + beginWord[i+1:]
                    if w in wordList:
                        q.append((w, j+1))
                        wordList.discard(w)
        
        return 0