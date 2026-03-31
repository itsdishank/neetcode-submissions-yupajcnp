class Solution:
    def simplifyPath(self, path: str) -> str:
        l = path.split('/')
        # print(l)
        stack = deque()

        for i in l:
            if not i or i == '.':
                continue
            elif i == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return '/'+'/'.join(stack)
            
        