class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        secret_c = Counter(secret)
        guess_c = Counter(guess)
        
        for a, b in zip(secret, guess):
            if a == b:
                bulls += 1
                secret_c[a] -= 1
                guess_c[a] -= 1
                    
        for l in secret_c:
            if l in guess_c:
                cows += min(secret_c[l], guess_c[l])
        
        return str(bulls) + 'A' + str(cows) + 'B'
        
        
        
        
        