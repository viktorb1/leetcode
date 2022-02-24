class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        sol = []
        
        for i in range(1, len(searchWord)+1):
            for s, p in enumerate(products):
                if p[:i] == searchWord[:i]:
                    sol.append([p for p in products[s:s+3] if p[:i] == searchWord[:i]])
                    break
            else:
                sol.append([])
                    
        return sol