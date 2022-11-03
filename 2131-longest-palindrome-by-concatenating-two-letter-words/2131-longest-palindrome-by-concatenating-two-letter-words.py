class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        total = 0
        word_count = Counter(words)
        both_same = {w: word_count[w] for w in word_count if w[0] == w[1]}
        seen = set(both_same.keys())
        
        for w in word_count:
            if w not in seen and w[::-1] in word_count:
                seen.add(w)
                seen.add(w[::-1])
                total += min(word_count[w], word_count[w[::-1]]) * 4
        
        at_least_one_odd = 0
        for w in both_same:
            if both_same[w] % 2 == 1:
                total += 2 * (both_same[w] - 1)
                at_least_one_odd = 2
            else:
                total += 2 * both_same[w]
                        
        return total + at_least_one_odd