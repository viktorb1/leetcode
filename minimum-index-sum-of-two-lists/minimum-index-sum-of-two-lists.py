class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash1 = {ele:i for i, ele in enumerate(list1)}
        hash2 = {ele:i for i, ele in enumerate(list2)}
        smallest = []
        
        for val in hash1:
            if val in hash2:
                total = hash2[val] + hash1[val]
                if not smallest or total < hash1[smallest[0]] + hash2[smallest[0]]:
                    smallest = [val]
                elif total == hash1[smallest[0]] + hash2[smallest[0]]:
                    smallest.append(val)
        
        return smallest