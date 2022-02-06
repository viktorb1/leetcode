class Solution:
    def alienOrder(self, words):
        adj = self.generateGraph(words)
        if adj == '':
            return ''

        l = self.splitDisconnected(adj)
        return self.mergeKStrings(l)

    def generateGraph(self, words):
        adj = {c:set() for word in words for c in word}

        for cur, nex in zip(words, words[1:]):
            if len(cur) > len(nex) and cur[:len(nex)] == nex:
                return ''
            i = 0
            while i < min(len(cur), len(nex)) and cur[i] == nex[i]:
                i += 1

            if i < min(len(cur), len(nex)) and cur[i] != nex[i]: 
                adj[cur[i]].add(nex[i])

        return adj

    def splitDisconnected(self, graph):
        visited = {c:0 for c in graph}
        ans = []

        def dfs(g, connectedg):
            if visited[g] == 1:
                return True
            
            visited[g] = 1
            connectedg.append(g)

            for i in graph[g]:
                if dfs(i, connectedg):
                    return True

            visited[g] = 2

        for g in graph:
            if visited[g] == 0:
                x = []
                if dfs(g,x):
                    return ''
                else:
                    ans.append(''.join(x))

        return ans

    def mergeKStrings(self, ans):
        sol = []
        quit = False
        while not quit:
            quit = True
            smallest = '~'
            smallest_idx = float('inf')

            for k in range(len(ans)):
                if ans[k] != '':
                    if ans[k][0] < smallest:
                        smallest = ans[k][0]
                        smallest_idx = k
                    
                    quit = False

            if not quit:
                ans[smallest_idx] = ans[smallest_idx][1:]   
                sol.append(smallest)

        return ''.join(sol)


lol = Solution()
print(lol.alienOrder(["ab", "abc"]))