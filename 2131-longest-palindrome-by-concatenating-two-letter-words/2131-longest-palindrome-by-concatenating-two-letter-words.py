class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        total = 0
        word_count = Counter(words)
        both_different = {w: word_count[w] for w in word_count if w[0] != w[1]}
        both_same = {w: word_count[w] for w in word_count if w[0] == w[1]}
        
        for w in list(both_different):
            if w[::-1] in both_different:
                total += min(both_different[w], both_different[w[::-1]]) * 4
                del both_different[w]
                del both_different[w[::-1]]
        
        at_least_one_odd = 0
        for w in both_same:
            if both_same[w] % 2 == 1:
                total += 2 * (both_same[w] - 1)
                at_least_one_odd = 2
            else:
                total += 2 * both_same[w]
                        
        return total + at_least_one_odd