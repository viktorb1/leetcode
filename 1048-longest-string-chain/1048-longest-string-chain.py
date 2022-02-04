class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        s = set(words)
        
        @cache
        def dfs(w):           
            m_val = 0
            
            for i in range(len(w)):
                if w[:i] + w[i+1:] in s:
                    m_val = max(m_val, 1 + dfs(w[:i] + w[i+1:]))
                    
            return m_val
        
        m_val = 0
        for w in words:
            m_val = max(1 + dfs(w), m_val)
            
        return m_val
            