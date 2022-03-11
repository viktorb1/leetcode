class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        path = path[:-1] if path[-1] == '' else path
        path = list(filter(lambda x: x != "" and x != ".", path))

        i = 0
        while i < len(path):
            if path[i] == '..' and i != 0:
                path = path[:i-1] + path[i+1:]
                i -= 1
            elif path[i] == '..':
                path = path[:i] + path[i+1:]
            else:
                i += 1
                    
        path = [''] + path
        return '/'.join(path) if len(path) > 1 else '/'