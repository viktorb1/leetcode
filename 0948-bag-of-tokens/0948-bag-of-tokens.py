class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score, ans = 0, 0
        tokens = deque(tokens)
            
        while tokens:
            if power >= tokens[0] and tokens:
                power -= tokens[0]
                tokens.popleft()
                score += 1
                ans = max(ans, score)
            elif score > 0 and tokens:
                power += tokens[-1]
                tokens.pop()
                score -= 1
                ans = max(ans, score)
            else:
                ans = max(ans, score)
                break

        return ans