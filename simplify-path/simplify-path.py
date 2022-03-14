class Solution:
    def simplifyPath(self, path):
        stack = []
        st = [p for p in path.split("/") if p != '' and p != '.']

        for elem in st:
            if elem == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(elem)
                
        return "/" + "/".join(stack)